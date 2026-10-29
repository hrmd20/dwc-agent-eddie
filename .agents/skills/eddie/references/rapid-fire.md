# EDDIE Rapid Fire (Text hook, captions, images)

This is also the Rapid Fire mode inside EDDIE MASTER EDITOR.

Before overlay placement, apply [shared subject framing](framing.md).

## Approved treatment
- Portrait 1080 × 1920, usually 30 fps. Preserve the presenter framing.
- Start on the first complete spoken word. Remove setup and excessive gaps; keep complete questions, responses and meaningful qualifiers. Use original recorded speech with 200% gain (2× amplitude, approximately +6.02 dB), applied once to the clean source, with peak limiting as needed to prevent clipping. No added voiceover, music or click unless requested. Do not double already boosted exports; honor an explicit gain override.
- Stationary Arial Bold white speech captions with black outline and subtle shadow. Use short 1–3 word phrases; keep short questions together. Calibrate once just below the beard; do not track head movement.
- Display numerical rankings as `0/10`, `8/10`, `9.5/10`, etc., matching the actual answer. Use larger type for ratings. Preserve additional commentary rather than replacing a qualified answer with a number alone.
- Hook: follow [the shared top-centered 0–3 second hook](text-hook.md), maximum two lines, white rounded box, black text/red emphasis and equal vertical padding.
- Images: one per topic, directly below captions. Pop in at the question, hold through the answer, disappear or replace at the next topic. Preserve aspect ratio. Default to still pop-ups; mix slide transitions only if requested.
- The hook stays at the top; images stay below captions. Preserve both without overlap.

## Interviewer and audio choice
At the start, determine which input mode the user wants. Infer it from supplied files and explicit instructions; ask if it is unclear. Do not assume the questions need an AI voice.

### AI interviewer
- When requested, draft or use the approved question script, then generate the interviewer voice using the chosen provider and voice. Offer voice options when none is selected; do not silently reuse another project’s voice.
- Confirm the doctor’s preferred name and pronunciation for the introduction. Preserve approved questions and ordering.
- Make speed and response gaps configurable. The reference workflow used Liza in Higgsfield, 20% faster delivery and 5 seconds between questions; these are optional settings, not universal defaults. Create exact silent gaps in post-production when needed rather than relying on punctuation or voice-model instructions.
- If the doctor has not recorded answers yet, provide the question audio with response gaps as a recording guide. Once answers are supplied, synchronize each question with its matching answer and tighten excess silence for the final edit.
- If the recording already contains the AI interviewer audio, use that embedded track rather than adding a duplicate. Keep the doctor’s real answers unless explicitly asked otherwise.

### Nurse or other recorded interviewer
- Use the nurse’s actual recorded questions. No synthetic voice is needed unless the user requests replacement.
- With one shared recording, preserve the approved camera framing and both speakers. With separate nurse and doctor clips, synchronize and pair each complete question and answer before cutting.
- For an on-camera nurse, retain the nurse during questions and the doctor during answers using the supplied shared shot or clean cuts between separate shots. If a different arrangement is requested, follow it. Do not turn an on-camera interview into an off-camera AI format by default.
- Calibrate captions and image placement for each camera shot so neither speaker’s face is covered. Keep captions stationary within each shot. Avoid duplicate audio from overlapping recordings and balance speaker levels without clipping.

Both modes use the same brief hook, Eddie captions, topic images and verified scores. Preserve the questions’ full meaning and the doctor’s qualifications. Generated question audio, scripts and nurse footage remain private project assets.

## Image sourcing
Use supplied images first unless the user requests search. Otherwise use Google Images by default for this selected mode. For each topic, search each actual spoken term and select the first displayed matching image; sponsored product images are allowed. Honor explicit choices such as Echo Flask for hydrogen water. Record the search term, source page and chosen image in the private project. Do not silently substitute generated art or a different search engine. Prefer a usable resolution of that same selected image. Preserve watermarks; if unavailable, explain the substitution needed. A product image illustrates the topic, not a new endorsement or medical claim.

## Baseline coordinates
Read `presets/eddie-rapid-fire.json` at the repository root. These values reproduce the approved framing; recalibrate for different footage. At 1080 × 1920: captions center (540,1060), 67 px, outline 4 px; scores 96 px. Use text-hook.md for hook geometry. Images start y=1130, fit within 640 × 470, below the captions. Scale together for other resolutions.

## Workflow and delivery
1. Inspect framing and transcribe the actual recording with word timestamps. Verify terms, numbers and cut boundaries; correct recognition errors such as Berberine and VO2.
2. Save a topic/cut plan and retime captions and image cues to the edited timeline. Preserve an approved cut for layout-only revisions.
3. Render a new version. For hook revisions, start from the clean caption-and-image master so old hooks are not burned into the new version.
4. Inspect encoded opening, each image/score, joins, hook exit at 3 s, and ending. Check audio for clipped words and synchronization. Full decoding supplements visual/audio review.
5. Save to the user's selected destination. Upload only when requested. When replacing an old export, verify the new copy before removing the specifically identified old one. Keep raw footage intact.

Private recordings, downloaded images, transcripts and renders stay in ignored `projects/`; publish only reusable instructions and presets.
