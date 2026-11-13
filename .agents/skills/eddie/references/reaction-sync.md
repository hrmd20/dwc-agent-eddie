# EDDIE Sync Reaction

Use the user's original clip, separate reaction recording and output folder. Ask for missing files; do not borrow another user's media. Identify which recording is the source and which is the presenter before editing. Discover local FFmpeg, FFprobe, a word-timestamp transcriber and caption renderer. No paid service is required.

## Playback and commentary

Use the doctor’s recording as the full-frame base. Start the source excerpt as a moving overlay while the doctor watches. Align visible reactions using a playback cue or matching audio when available. Check for drift at the beginning and end. Keep the source at its original speed and retain enough context to complete the thought.

While the overlay plays, use the source clip's original audio alone. Mute the doctor's microphone during this interval, including any recorded source bleed. At the source's end, remove the overlay and bring in the doctor's audio on the first complete word of their response. Trim setup and pauses at the handoff without clipping either speaker. Record the edit points and retime captions after cuts.

## Layout

Use a 2160 × 3840 canvas at 30 fps. Preserve the source aspect ratio. Mask the moving source overlay to rounded corners and put a subtle, soft drop shadow behind it. At 4K, start with a 48 px corner radius and a soft black shadow at about 25% opacity, with a 12 px downward offset and 24 px blur. Scale the treatment for the card size. Keep the shadow outside the clip and avoid a hard outline.

Choose the overlay position for the actual shot. Keep it clear of the doctor's face, important gestures, source captions and the top hook. Use the tracked doctor cutout as a foreground layer when needed for the composition. Keep the doctor’s recording as the full-frame base. Preserve an explicitly requested or approved layout.

Place the [approved Master Editor hook](text-hook.md) in the top safe area. Use a single snug translucent charcoal rounded box, bold white text and one yellow keyword. Default to the first three seconds. Keep the overlay and text stable in canvas coordinates through camera reframes. Use the uploaded reference for the overlay treatment and the source-to-commentary sequence.

## Captions

Match this reaction-specific treatment: Arial Bold or a similar licensed sans-serif, uppercase white with warm gold #F1D688 highlighting the currently spoken word, dark outline and subtle shadow. Short chunks: usually 1–3 words, about 23 characters maximum. Captions remain stationary within each layout; word color changes, position does not.

At 1080 × 1920, using ASS/libass coordinates and center alignment:
- Source speech: about 62 px at (540,1260), in a clear region. Preserve embedded source captions and add source captions only when needed.
- Full-screen presenter commentary: about 68 px at (540,930), calibrated below the neckline for the actual footage.
- Outline about 3 px, shadow 1 px. Split overlong chunks before reducing type size.

Use separate caption tracks for the source and the doctor, switching at the audio handoff. Show actual spoken words, correct obvious transcription errors and topic spellings against the audio, and do not invent speech. Preserve profanity unless the user requests censoring.

## Audio

Use the original source audio during the overlay and the doctor's recorded audio after it. Balance the two segments and apply the Master Editor's measured −14 LUFS target and −1 dBTP ceiling. Review the handoff for an intact first word, echo and abrupt level changes. Add a click only when explicitly requested.

## Deliver and verify

Render a new H.264 MP4 (yuv420p, CRF 18 or comparable quality), AAC 48 kHz, fast-start metadata. Keep originals and earlier exports intact. Inspect the encoded beginning, synchronized reaction moments, rounded mask and shadow, caption bounds, every edited commentary join, final word and consecutive frames around the full-screen transition. Check full decode, duration, frame count, A/V sync and loudness. Automated correlation/transcription supplements listening; label any unperformed listening review honestly.

Save the completed version in the requested folder. Keep recordings, transcripts, synchronization notes, exports and click audio in ignored projects/. The public package contains reusable instructions and presets only. Current user directions override defaults.
