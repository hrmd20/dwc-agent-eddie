# Inputs and evidence

Paths resolve relative to the manifest. Never reuse transcripts from a different cut.

```json
{
  "media": "export.mp4",
  "dimensions": [2160, 3840],
  "export_words": "export-aligned.json",
  "source_media": "original.mp4",
  "source_words": "source-aligned.json",
  "source_ranges": [[0.2, 10.8], [12.1, 20.4]],
  "cuts": [10.6],
  "captions": "captions.ass",
  "one_word": true,
  "expected_text": "intended-edited-transcript.txt",
  "gap_seconds": 0.6
}
```

`cuts` are seconds on the export timeline. `source_ranges` are start/end seconds on the source transcript timeline; this simple schema supports one source. Multi-source projects need separate source audits, then aggregate evidence. Source alignment must include a matching hash of `source_media` and describe the actual source, not an independent export transcription. `expected_text` is the approved edited speech, not a transcript freshly copied from the same export ASR. `export_words` from align_words.py includes exact-media hash and transcription method. An existing transcript aligned to the export does not count as independent ASR.

ASS Caption/Captions/Default styles are spoken captions; keep hooks separate. One-word timing checks use 150 ms start / 200 ms end disagreement as advisory limits. Gap and peak limits are QC defaults, not automatic cut instructions. Scanner thresholds for silence (-40 dB, 0.6 seconds), freeze (-50 dB, 0.7 seconds), black (0.1 seconds), and true peak (-1 dBFS) require contextual review.

Installation and invocation:

```sh
python3 -m venv .venv-qc
.venv-qc/bin/python -m pip install -r path/to/eddie-quality-check/requirements.txt
.venv-qc/bin/python path/to/scripts/align_words.py export.mp4 --cache local-models --out export-aligned.json
python3 path/to/scripts/quality_check.py manifest.json --out qa --clips
```

Pass `--runner '/absolute/path/work/run-kit'` to both scripts when needed. Files remain local; models download to the supplied cache. First-run compute may take longer on CPU. No paid API or cloud footage upload is required.

Report statuses are Passed / Needs review / Not checked. `report.json` and `report.md` retain findings and a fingerprint binding the media and all declared input files. Up to 30 four-second review clips are generated, centered around cuts/findings where possible; these excerpts do not replace full playback.

Optional review file:

```json
{
  "fingerprint": "copy-from-current-report",
  "checks": {
    "every_join_listening": {
      "status": "Passed",
      "reviewer": "actual reviewer name",
      "evidence": "List the joins listened to, source comparisons and outcome."
    }
  },
  "findings": {
    "id-from-report": {
      "resolution": "intentional",
      "reviewer": "actual reviewer name",
      "evidence": "Explain why this specific finding is intentional or a verified false positive."
    }
  }
}
```

Rerun with `--reviews review.json`. Do not manufacture review evidence, self-certify unperformed playback or silence all findings. Tool version/threshold changes also require a new review. If a correction changes media, the former review is stale.

External foundation: WhisperX (https://github.com/m-bain/whisperX), faster-whisper, and local FFmpeg. The bundled scanner is EDDIE-owned code; it does not install third-party agent instructions or replace EDDIE's visual style.
