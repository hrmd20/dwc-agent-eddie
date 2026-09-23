---
name: eddie-reaction
description: "Edit paired source and presenter reaction videos in EDDIE Reaction style: continuous source playback, a synchronized bottom-left presenter inset, captions and a click, followed by full-screen commentary."
---

# EDDIE Reaction

Use the user's original clip, separate reaction recording, supplied click sound and output folder. Ask for missing files; do not borrow another user's media. Identify which recording is the source and which is the presenter before editing. Discover local FFmpeg, FFprobe, a word-timestamp transcriber and caption renderer. No paid service is required.

## Synchronize before cutting

Inspect both recordings and measure where source playback begins in the reaction recording. Correlate shared audio across several separated windows. If room reflections defeat waveform correlation, compare 10 ms RMS audio envelopes and verify the result visually. Check beginning and end for drift; never assume a prior project's offset or source duration. Record the offset, evidence and confidence. If the recordings have no reliable shared cue, inspect playback gestures or ask for the start marker instead of claiming exact sync.

Keep the original clip playing continuously at normal speed. Remove the presenter's recording setup before the synchronized start. Do not remove pauses from the reaction track during source playback: that would break sync. Preserve spontaneous laughter and interjections. After playback, remove abandoned takes, coughs and excessive dead air while retaining complete words, intentional pauses, qualifications and the closing phrase. Record source ranges and retime captions after cuts.

## Layout

Default output: 1080 × 1920, 30 fps. Original clip is the main picture; the presenter appears in the bottom-left inset during playback, then becomes full-screen when the source finishes. Preserve aspect ratios and faces. Adapt framing to each user's footage and avoid covering source captions.

Approved portrait reference coordinates, to calibrate rather than blindly force:
- Original: contain inside a 960 × 1706 rectangle at (60,32), on dark background #080C12.
- Reaction inset: 324 × 432 at (24,1464), with a subtle 3 px white border. Crop around the presenter's face and upper body; never stretch.
- Inset appears two frames after the opening click. Its position stays fixed.
- Switch to full-screen commentary at the frame-aligned source end. Pad the final source frame through that boundary if needed so it cannot disappear a frame before the inset. Remove the inset in the same frame as the full-screen switch; avoid a duplicate presenter flash.

## Captions

Match this reaction-specific treatment: Arial Bold or a similar licensed sans-serif, uppercase white with warm gold #F1D688 highlighting the currently spoken word, dark outline and subtle shadow. Short chunks: usually 1–3 words, about 23 characters maximum. Captions remain stationary within each layout; word color changes, position does not.

At 1080 × 1920, using ASS/libass coordinates and center alignment:
- Source speech: about 62 px at (540,1260), above the inset. Skip or reposition when existing embedded captions would conflict.
- Presenter interjections during playback: about 46 px at (720,1810), beside the inset.
- Full-screen presenter commentary: about 68 px at (540,930), calibrated below the neckline for the actual footage.
- Outline about 3 px, shadow 1 px. Split overlong chunks before reducing type size.

Build separate caption tracks for the original and presenter so overlapping speech does not truncate either track. Show actual spoken words, correct obvious transcription errors and topic spellings against the audio, and do not invent speech. Preserve profanity unless the user requests censoring.

## Audio

Use the clean original audio during playback. Mute redundant microphone bleed to avoid echo, but retain actual laughter and spoken interjections. For overlaps, mix intelligibly with gentle ducking; do not silence the source punchline or the presenter's response. Bring the presenter to normal speech level for full-screen commentary. Confirm no doubled source audio at the transition.

Play the user's click once, two frames before inset entry; no other effects, music, graphics or stock images by default. Normalize speech around -16 LUFS and target true peak at or below -1.5 dBTP; measure the encoded mix. Never synthesize or clone speech to repair a cut.

## Deliver and verify

Render a new H.264 MP4 (yuv420p, CRF 18 or comparable quality), AAC 48 kHz, fast-start metadata. Keep originals and earlier exports intact. Inspect the encoded beginning, synchronized reaction moments, caption bounds, every edited commentary join, final word and consecutive frames around the full-screen transition. Check full decode, duration, frame count, A/V sync and loudness. Automated correlation/transcription supplements listening; label any unperformed listening review honestly.

Save the completed version in the requested folder. Keep recordings, transcripts, synchronization notes, exports and click audio in ignored projects/. The public package contains reusable instructions and presets only. This style is separate from EDDIE Classic, Motion, Carousel and Landscape; current user directions override defaults.
