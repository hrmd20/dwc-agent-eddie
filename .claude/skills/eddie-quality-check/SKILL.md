---
name: eddie-quality-check
description: Audit EDDIE video exports for speech cuts, repeats, gaps, caption timing and technical defects; generate timestamped review clips and an evidence-bound release report. Use before final delivery or to investigate editing errors. Does not publish or automatically remove speech.
---

# EDDIE Quality Check

Preserve the approved edit and style. Run this stage after speech editing and again on the actual encoded export. A successful render or an ASR transcript cannot certify a natural edit.

## Run

1. Preserve source ranges and export-timeline join positions in the private project. Use a corrected source transcript with aligned words to check boundaries. Do not substitute export times for source times.
2. Use `scripts/align_words.py` to align source segments (`--transcript`) and independently transcribe/align the final export (omit `--transcript`). It runs locally; initial package/model downloads need internet. Install the pinned `requirements.txt` in an isolated venv. Discover FFmpeg/FFprobe locally or pass `--runner '/path/to/wrapper'`.
3. Create the manifest described in [the input and review contract](references/contract.md). Run `scripts/quality_check.py manifest.json --out qa --clips`. Exit 2 means REVIEW, not a crashed render. Nonzero exceptions are execution failures, never passes.
4. Review each finding in source context and listen across every join. Repetition can be emphasis; silence can be a useful breath; freezes may be intentional graphics. Inspect numbers, units, negations, medical terms and the complete first/last words. Low-confidence or missing alignments need review, not invented timing.
5. Inspect the full encoded video at normal speed. Confirm hook placement/duration, caption readability, face clearance, picture timing and approved style. Compare denoised speech with the source at matched loudness. Confirm 150% gain was applied once, not stacked. Technical peak measurements do not certify absence of clicks or denoising artifacts.
6. Record actual review evidence and reviewer identity against the report fingerprint. Mark intentional candidates with a reason. If a defect is fixed, rerender and rerun QC; never mark the old file fixed. A changed input invalidates old reviews.

Only all-Passed checks and zero unresolved findings permit FINAL_ELIGIBLE. Any unavailable listening, missing provenance or omitted check keeps REVIEW. Report skipped checks honestly. User authorization to upload a review file does not make its QC status final.

## Scope and limitations

The scanner implements technical signal checks, word-boundary candidates, repeats/gaps, ASS caption timing/text checks and independent export-transcript comparison. Face placement, semantic accuracy, audible clicks, lip sync and full naturalness currently require recorded review. It does not claim automatic visual understanding or perfect error detection.

Keep private footage, transcripts, reports and test excerpts out of Git. Reusable synthetic regression tests belong in `tests/`. Build additional private benchmarks from user-corrected before/after examples with exact source/export hashes and reviewer labels; historical timestamps from another revision are insufficient evidence.
