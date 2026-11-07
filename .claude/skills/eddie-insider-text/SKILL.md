---
name: eddie-insider-text
description: Edit EDDIE INSIDER TEXT videos with a persistent charcoal/yellow hook, raised speech captions and supplied message screenshots. Use for this named style or doctor commentary on supplied messages; publishing belongs to EDDIE MANAGER.
---

# EDDIE INSIDER TEXT — 1.0.0

A named Master Editor variant for commentary on supplied messages. Keep its defaults scoped to this style. Read the sibling `../eddie/SKILL.md` for speech cleanup and export review; the layout and duration overrides below take precedence. Use `presets/eddie-insider-text.json` from the repository root.

## Approved treatment

- Export portrait 4K (2160 × 3840). Preserve the original and save a separate review version; disclose upscaling when source resolution is lower.
- Keep the doctor visible. Preserve approved framing, cuts and message timing during visual-only revisions.
- Show the hook throughout the complete video, including the last frame. Use large Arial Bold, white text, selected emphasis in golden yellow #FFC400, and snug translucent charcoal rounded boxes. Maximum two lines; measure visible glyph bounds with small equal padding. Keep each colored run on the same baseline.
- Place the hook close above the hairline, with a small clearance, not at the distant top edge. Choose a stable position from the full clip, checking head movement and cut-ins. Recalculate placement for each subject rather than applying a fixed screen percentage. The approved 2160 × 3840 example uses 156px type, 28px horizontal padding, 20px vertical padding and 32px corner radius. Those are reference sizes, not a universal position.
- Use stationary bold white speech captions, black outline and subtle shadow, in short 1–3 word phrases. In this variant, place them in the beard/chin area below the lips as requested, above supplied message screenshots. Keep lips unobstructed through the complete video. Reference size is 134px at 4K, outline 8px, shadow 3px; calibrate a stable position to actual footage.
- Preserve supplied message screenshots below captions with their original wording and proportions. Do not fabricate messages or add iPhone animations, extra pictures or sounds by default.
- For newly processed source audio, use conservative voice isolation/denoise as needed and 150% gain once with peak protection. Never reapply gain when revising an already processed export.

## Censoring and ending

When requested, locate each specified spoken word against the actual audio. Mute the entire word and replace it with a short moderate-level beep with tiny edge fades. Blur that word wherever it is visible in a message screenshot for its entire visible duration. Render the speech caption as [BEEP]; do not reintroduce the word in subtitles. Preserve adjacent syllables. Censoring is opt-in and scoped to requested words.

For a requested ending phrase, retain its complete final word, then a short natural tail before the next phrase. Inspect the audio boundary instead of cutting at the nominal transcript timestamp. If the next utterance begins immediately, use only the available pause; never append the next sentence. Do not bake a specific video's phrase or timestamp into the general preset.

## Review and delivery

Check the exported opening, middle, end, all cuts and screenshot changes for caption/hook collisions, complete words, readable type and sync. Listen to censor boundaries and the final word. Verify dimensions, duration, full-file decode and audio peaks. If listening is unavailable, label the copy provisional and describe that limit. Return the review link before publication; invoking this editing style does not authorize uploading. Keep user footage, transcripts, screenshots and account data out of the public package.
