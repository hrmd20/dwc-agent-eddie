# Default quality pass — all Master Editor modes

Apply these defaults to new videos for every practice. A supplied reference, explicit override or approved edit takes precedence. Do not insert optional images, sound effects or iPhone messages into a captions-only brief.

## Speech and pacing
- Review the entire recording for abandoned takes, stutters, accidental repeated words/phrases and disruptive fillers. Keep the cleanest complete take. Preserve intentional emphasis, quotations, clinical qualifiers, numbers, units, negations and a complete CTA.
- Follow speech-cleanup.md: full word-timestamp transcript AND overlapping short excerpts, waveform/silence checks, issue ledger, clean intermediate, independent second pass, then encoded-output review. ASR often collapses repeated takes; a clean-looking transcript alone cannot clear the edit.
- Treat a pause over 0.4 seconds, a repeated 2–8-word opening, unusually long word timing or transcript disagreement as a REVIEW trigger, not an automatic delete. Keep natural breaths and interviewer response windows. Remove opening setup delays while retaining the complete first word.
- Check every join with surrounding speech. Rebuild caption and visual timing after cuts. A revised join must be checked again; never rely on the prior version's review.

## Voice isolation, denoise and −14 LUFS loudness
- Start from the unprocessed source or documented unamplified clean intermediate. Default to conservative speech-focused noise suppression/voice isolation and gentle residual denoise, reducing or bypassing stages when the source is already clean. Discover a locally available speech model/tool; document any unavailable capability rather than describing ordinary gain/EQ as voice isolation.
- Compare processed and original speech at matched loudness. Preserve quiet consonants, breaths, interviewer questions and natural tone. Lower the strength if processing causes metallic, watery or gated speech. Do not stack a noise gate and several denoisers without a demonstrated need.
- Balance speakers/source clips, then use measured two-pass normalization to −14 LUFS integrated (±0.5 LUFS), encoded true peak ≤ −1 dBTP. This replaces fixed 150% gain. Never stack gain on processed exports. For visual-only revisions, preserve approved audio if it meets the current target; report conflicts rather than silently changing an explicitly approved treatment.
- Measure the encoded AAC output, including true peaks when supported. A limiter before encoding does not prove the encoded file is safe: codec overshoot can introduce clipping. Leave headroom, inspect peaks and rerender audio if needed. Record actual settings and any peak limiting.

## Framing and overlays
- Inspect opening, middle, ending, each shot scale and large gestures for accidental black edge strips. Confirm a strip is unwanted padding, not a dark part of the actual scene or an intentional reaction layout.
- Use the smallest proportional crop that removes the strip without cutting hair, useful gestures or source content. Crop the clean footage BEFORE overlays so captions, hooks and images retain their screen positions. Measure each source; never reuse a fixed pixel crop across unrelated recordings.
- Center direct-to-camera presenters at both base and restrained punch-in scales. Preserve intentional side-angle/interview layouts. Cut in/out at natural emphasis or edit points; avoid constant zooms and head jumps.
- Use the shared 0–3 second hook: maximum two lines, translucent charcoal background, bold white text and selected yellow emphasis, positioned a little above the actual head, centered visible glyphs and equal tight padding. User-requested duration/placement/reference overrides this. Keep faces clear.
- Verify medical caption spelling against the audio and supplied script. Images appear only for the matching topic and leave when it ends, below captions and clear of the face. Prefer supplied assets and relevant actual ingredient images over unrelated product packaging. Pop/left-slide/whoosh treatments are available when requested; do not add automatic effects to every practice's video.

- For picture-enabled modes, follow [image selection and rounded cards](image-selection.md): Google topic search, relevant landscape photos near 16:9, rounded rectangular cards and subtle shadows. Preserve supplied aspect ratios and transparent cutouts.

## Export and release
- Default portrait output is 2160×3840 (4K); preserve requested landscape as 3840×2160. Scale overlay geometry with the canvas. Disclose when footage is upscaled; 4K export does not restore source detail.
- Save a separately named review copy; preserve originals and prior approvals. Inspect actual encoded frames, not just layout previews. Verify full-file decode, timing, dimensions, A/V sync, captions, visual cues, peak levels and every revised join.
- Watch AND listen to the entire export at normal speed before calling it final. Bind the review record to the exact output file/hash. If listening is unavailable, clearly label it provisional review with listening pending. Never mark a failed or unchecked gate passed based on ASR or a successful render.
- Return usable review links first. Do not move to the posting folder or upload unless authorized for that destination. Publish only reusable instructions/presets; keep footage, transcripts, personal assets and review ledgers private.

## Third polishing layer
Apply [third-polish.md](third-polish.md) to every video before delivery. Missing listening or any unresolved checklist item blocks delivery, including a provisional export unless explicitly requested. Internal QC renders remain allowed.
