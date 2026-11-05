# Speech cleanup and delivery gate

Use for recorded speech in every Master Editor mode. This is an editorial workflow, not model fine-tuning or a guarantee of error-free output. Layout-only revisions preserve approved speech. User instructions override defaults.

## Pass 1 — establish the exact source and issues

Identify the exact file/version the user reviewed. User timestamps belong to that export, not the raw recording. Save a reversible source-to-output keep-range map. Add every user-reported issue to a private issue ledger with source time, review time, evidence, action and verification status. Do not mark a complaint resolved merely because the main transcript omits it.

Transcribe with word timestamps, then independently transcribe overlapping short excerpts (start with 6–10 seconds and 2 seconds of overlap). Deduplicate overlap in the analysis; never mistake overlap copies for spoken repetition. At each suspected restart, use a tighter 2–4-second excerpt with context. Full-length ASR can silently collapse repeated takes and stretch a word across the missing speech. An apparently fluent transcript is not evidence of a clean recording.

## Conditional review rules

| Signal | Required action |
|---|---|
| Adjacent repeated word, or repeated 2–8-word opening within about 5 seconds | Inspect the recording; retain the complete intended take and remove the abandoned one. When the user explicitly identifies back-to-back repetition as their mistake marker, prioritize it accordingly. Preserve deliberate quotations, emphasis and later recaps. |
| Silence over 0.4 seconds | Flag for contextual review. Shorten accidental delays; preserve intentional breathing, emphasis, reaction timing and interviewer response windows. This threshold is a configurable review trigger, never an automatic cut rule. |
| Word duration over 0.8 seconds, zero/negative timing, overlap, or ASR disagreement | Review waveform and short excerpt. Long medical terms may be valid. Do not trust that timestamp as a cut boundary. |
| Repeated lead-in such as “remember most,” “you're going to have,” or “because the peaks and troughs” | Check the whole surrounding sentence for multiple false starts, including a second restart hidden in the replacement take. |
| Stray syllable, “the,” “going,” filler or clipped ending at a join | Reopen the clean/raw source, restore enough audio to retain the complete word, then remove the actual error. Do not trim progressively tighter based only on ASR. |
| Clinical number, unit, drug name or negation touches a cut | Confirm the entire phrase remains audible and unchanged, including endings such as “14 days.” Never change medical meaning to improve fluency. |

Use `scripts/audit_speech.py` on each word-timestamp transcript to generate candidates. It finds text/timing issues only; it cannot discover words ASR omitted or prove that silence contains no quiet speech. Independently run a waveform/silence detector with a noise threshold appropriate to that recording. Keep these findings in the same ledger. Review the entire recording, not just user timestamps.

## Pass 2 — cut speech before decorating

Prefer a complete good take over assembling fragments. Choose cut boundaries from playback and waveform with a small natural margin, not exactly at an ASR boundary. Keep initial consonants, final plural sounds, complete CTA and meaningful pauses. Very short audio fades may remove clicks; they cannot repair a clipped word.

Make a clean intermediate without burned-in overlays. Freshly transcribe it; repeat the overlapping excerpt scan and inspect each cut with roughly two seconds on each side. Compare against the ledger. If a repeat, clipped syllable or gap remains, revise and recheck the affected neighborhood. A changed cut invalidates earlier checks for that neighborhood.

### Boundary repairs learned from review

- Treat reports of a sound error at a timestamp separately from wording mistakes. Identify the exact version and listen around the join; a fluent transcript does not clear clicks, clipped consonants or abrupt noise changes.
- When revisions cut an already concatenated master, map back through every edit layer. Check whether the boundary accidentally retains a few frames or milliseconds from the next discarded take. Replace the damaged neighborhood from the raw recording when necessary; use the same documented audio treatment once on restored raw sections.
- After removing a lead-in, check both sides for a leftover syllable from the removed phrase and preserve the full first retained word. Do not cut blindly at rounded seconds or at an ASR timestamp. Tiny fades can suppress clicks but cannot recover missing speech.
- For a clipped closing phrase such as “I'll send it over,” reopen the raw source and include the full final word plus a short natural trailing pause (often 0.3–0.6 seconds). Do not substitute a freeze frame or silence for missing word audio. If the raw source itself lacks the ending, disclose that rather than claim it restored.
- Compare the retained audio words with the rebuilt captions after each repair: include short words such as “here's,” “you're,” and “popping”; exclude words from deleted phrases. Clamp caption intervals to the kept speech without dropping an entire retained word merely because its timestamp straddles a cut.

## Pass 3 — rebuild timing and visuals

Regenerate captions from the retained speech. Do not map a three-word caption across a removed phrase while keeping its deleted words. Correct medical spelling against the recording. Reject empty, negative, overlapping or out-of-range caption intervals.

Retime images, hooks, censor beeps, motion and other audio cues using the same edit map. Preserve user-approved framing and style. Apply 150% gain once to the clean source, with peak protection; never double an already processed export. Check the complete profanity mute and beep when requested.

## Pass 4 — actual export review

Review the encoded export, not only the intermediate:
- Play the entire export at normal speed with audio; inspect every changed join, first word and last word.
- Check the hook, images and captions at entry/exit frames and at mobile size. Check full-screen crops, transparent edges and any requested slide/sound synchronization.
- Verify full-file decode, duration, dimensions, audio/video sync, peaks and caption bounds.
- Run focused short-transcript checks on the encoded problem sections; automated checks supplement listening, not replace it.

## Gate before final delivery

Every ledger item must be `fixed-and-rechecked` or `intentional-and-reviewed`, with a reason and checked output timestamp. No unresolved user issue, repeat, clipped word, accidental gap, stale caption or failed technical check may be called final.

Keep a private review record bound to the exact output filename/hash: source ranges, findings, resolutions, fresh transcript, join checks, full playback, visual checks, decode and audio checks. Rerendering invalidates output verification; repeat checks relevant to the change.

If audio playback is unavailable, do all available checks, state that limitation, and label the result **provisional review — listening check pending**, not final/fully verified/perfect. Do not mark a listening check passed from transcription, waveform or a successful render. If a known defect cannot be resolved, report its timestamp and blocker rather than delivering it as completed.

## Regression cases before changing the workflow

Use synthetic/public fixtures in the repository; keep private footage/transcripts out of GitHub. Verify that the workflow detects a repeated two-word lead-in, a restart hidden inside a long ASR token, a one-second pause, and a clipped final consonant; also verify that it preserves intentional emphasis and Q&A pauses. Scanner success alone cannot certify the audio cases. Use previously troublesome private excerpts locally for playback checks when available.
