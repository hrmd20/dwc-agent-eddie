#!/usr/bin/env python3
"""Flag word-timestamp candidates; never cut media or certify audio quality.

Input: JSON word list, segment list with words, or {segments: [...]}.
Usage: python3 audit_speech.py transcript.json --out review.json
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re


def flatten(data):
    if isinstance(data, dict):
        data = data.get('segments', data.get('words', []))
    if not isinstance(data, list):
        raise ValueError('Expected words or segments as a JSON list')
    words = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError('Each entry must be an object')
        words.extend(item['words'] if 'words' in item else [item])
    if not words:
        raise ValueError('No word timestamps found; segment-only text is insufficient')
    result = []
    for w in words:
        a, b = float(w['start']), float(w['end'])
        if not math.isfinite(a) or not math.isfinite(b):
            raise ValueError('Non-finite timestamp')
        token = str(w.get('word', w.get('text', ''))).strip()
        if not token:
            raise ValueError('Empty word')
        result.append({'start': a, 'end': b, 'word': token})
    return result  # Preserve order so timestamp errors are not hidden by sorting.


def audit(words, gap=0.4, long_word=0.8, repeat_window=5.0):
    findings = []
    def add(kind, a, b, evidence):
        findings.append({'id': f'F{len(findings)+1:04}', 'kind': kind,
                         'start': round(a, 3), 'end': round(b, 3),
                         'evidence': evidence, 'status': 'open'})
    tokens = [re.sub(r'[^\w\d]+', '', w['word'].lower()) for w in words]
    if words[0]['start'] > gap:
        add('leading_gap', 0, words[0]['start'], 'Verify opening against audio')
    for i, w in enumerate(words):
        duration = w['end'] - w['start']
        if w['start'] < 0 or duration <= 0:
            add('invalid_timing', w['start'], w['end'], w['word'])
        elif duration > long_word:
            add('long_word', w['start'], w['end'], w['word'])
        if i:
            previous = words[i-1]
            pause = w['start'] - previous['end']
            if pause > gap:
                add('gap', previous['end'], w['start'],
                    previous['word'] + ' → ' + w['word'])
            elif pause < -0.02:
                add('overlap_or_order', w['start'], previous['end'],
                    previous['word'] + ' → ' + w['word'])
        # Prefer longest matching phrase; allow up to three intervening words.
        for n in range(min(8, (len(words)-i)//2), 0, -1):
            phrase = tokens[i:i+n]
            if not all(phrase):
                continue
            found = False
            for j in range(i+n, min(i+n+4, len(words)-n+1)):
                elapsed = words[j]['start'] - words[i+n-1]['end']
                if 0 <= elapsed <= repeat_window and phrase == tokens[j:j+n]:
                    add('repeat_candidate', words[i]['start'], words[j+n-1]['end'],
                        ' '.join(w['word'] for w in words[i:j+n]))
                    found = True
                    break
            if found:
                break
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('transcript', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--gap', type=float, default=0.4)
    parser.add_argument('--long-word', type=float, default=0.8)
    parser.add_argument('--repeat-window', type=float, default=5.0)
    args = parser.parse_args()
    if min(args.gap, args.long_word, args.repeat_window) <= 0:
        parser.error('Thresholds must be positive')
    raw = args.transcript.read_bytes()
    try:
        words = flatten(json.loads(raw))
    except (KeyError, TypeError, ValueError) as e:
        parser.error(str(e))
    findings = audit(words, args.gap, args.long_word, args.repeat_window)
    report = {
        'transcript_sha256': hashlib.sha256(raw).hexdigest(),
        'thresholds': {'gap': args.gap, 'long_word': args.long_word,
                       'repeat_window': args.repeat_window},
        'findings': findings,
        'release_status': 'pending_audio_and_export_review',
        'required_manual_checks': {
            name: 'pending' for name in ['user_issues', 'short_excerpt_comparison',
            'waveform_silences', 'every_join', 'full_export_playback',
            'captions_and_visuals', 'decode_sync_and_peaks']},
        'limitations': 'Text candidates only. ASR may omit repeats. No findings is not approval.'
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + '\n')
    print(f'{len(findings)} candidates; audio/export review still required. Report: {args.out}')


if __name__ == '__main__':
    main()
