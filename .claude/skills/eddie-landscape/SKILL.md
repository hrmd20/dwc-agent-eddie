---
name: eddie-landscape
description: Edit talking-head videos in EDDIE Landscape style with 16:9 4K framing, stationary outlined white captions and natural, tightly cleaned speech cuts. Use when the user requests EDDIE Landscape or the approved V1 landscape style.
---

# EDDIE Landscape

Reproduce the approved V1 Revision 3 treatment: full landscape presenter footage, readable stationary captions, and clean conversational cuts. Current user instructions override defaults. Preserve the other EDDIE styles as separate choices.

## Inputs and tools

Use the user's own source video, optional script and output folder. The script guides content; the recording determines actual words, delivery and closing remarks. Ask only for missing inputs. Inspect available FFmpeg/FFprobe, a word-timestamp transcriber and caption renderer. Discover local paths; do not assume a particular workstation or cloud account. No pictures, click sound or paid service is required.

## Picture and captions

- Export 3840 × 2160, 16:9, 30 fps by default. Preserve the full landscape framing and natural presenter appearance. If the source is lower resolution, state that the 4K output is upscaled. Do not stretch a portrait source; agree framing when a material crop is needed.
- Use Arial Bold or a metrically similar licensed sans-serif when unavailable. At 3840 × 2160: font size 172, white fill, black outline 7, subtle shadow 3, character spacing -3. These are ASS/libass units with PlayResX 3840 and PlayResY 2160, not interchangeable CSS sizes.
- Fixed caption center (1920,1870), ASS alignment 5 (middle-center). Keep position and font size stationary throughout the edit. Do not track the face, bounce, scale or animate individual words. Scale coordinates proportionally for other approved output sizes.
- Show short phrase chunks, normally no more than 5 words and 34 characters. Break earlier at natural punctuation or gaps above 0.3 seconds. Keep phrases inside 200-pixel side margins; split phrases before shrinking type. No colored keyword highlighting.
- Start each phrase at its first spoken word. End at its last word plus at most 0.06 seconds, clamped to the next phrase and video end. Regenerate all caption timings after cuts. Export an SRT alongside the burned-in MP4.
- Keep this a presenter-and-captions style by default: no added images, motion graphics, zoom effects, music or click effects unless requested.

## Clean speech editing

1. Map word timestamps and candidate edits against the original footage. Preserve originals and record source ranges in an edit decision list.
2. Start promptly on the complete first spoken word. Remove long pre-roll, coughs, abandoned takes, unintentional repeated starts and dead air. Keep the clean completed take. Preserve purposeful repetition and natural breathing.
3. Review each join in context. Transcription timestamps can include silence; silence thresholds can miss quiet consonants. Inspect waveform and listen before choosing boundaries. Preserve whole words and short natural lead/tail margins, especially greetings, 'thank you' and final closing words.
4. Use clean frame-aligned jump cuts. Do not cut mid-word, mechanically remove every breath, or join phrases that change meaning. If a quiet word is intact, use a small smooth gain adjustment instead of synthesizing speech.
5. Apply identical source ranges to audio and video; retime captions to the new timeline. Small audio edge fades (about 3 ms) can prevent clicks without covering speech.
6. End just after the complete closing phrase, with a short natural tail. Do not truncate the last syllable merely to remove trailing silence.

## Export and review

Use H.264 MP4, yuv420p, CRF 18 or equivalent high quality, AAC 48 kHz around 320 kbps, and fast-start metadata. Target clear speech around -16 LUFS and true peak at or below -1.5 dBTP; measure the final mix. Keep natural vocal delivery.

Review opening, all revised joins, captions, quiet word endings and closing in the encoded result. Check frame count, duration, audio/video sync, full-file decode, no clipped peaks, caption bounds and non-overlap. An ASR check supplements listening; it does not prove a join sounds natural.

Save a newly named version in the requested output folder, leaving the raw video and earlier versions intact. For a preview request, deliver only the requested preview; otherwise finish the authorized full edit. Keep footage, transcripts, reference screenshots, exports and personal settings in ignored projects/. Publish only reusable skill instructions and presets.
