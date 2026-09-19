---
name: eddie-motion
description: Edit talking-head videos in EDDIE Motion style with animated typography and diagrams, neckline captions, and supplied click audio. Use for EDDIE Motion edits and previews; use the separate eddie skill for Classic picture-based edits.
---

# EDDIE Motion

EDDIE Motion 1.0.0 uses motion graphics only over the presenter's footage. No photographs, stock images, screenshots, character portraits, or image overlays. Users supply their own video and click audio; an image library is not required. Current user instructions override defaults.

Follow the specification below. Preserve the separate EDDIE Classic style and existing project settings.

## Prepare

Inspect source footage and available local editing tools. Preserve originals and reuse verified word timestamps aligned to the actual edited footage. Preserve an approved cut during style revisions. For a new edit, remove clear recording setup and false starts while preserving meaning, natural breaths and the last syllable.

Keep source references, edit decisions, transcript, caption groups, timed graphic events, click cues, render source and verification notes in an ignored project directory. Create one with `python3 scripts/new_project.py my-video --style motion`. The helper scaffolds a project; it does not render a video.

## Compose

Keep the speaker visible. Place short white captions at the base of the neck, with selective gold and serif-italic keyword emphasis. Place the explanatory graphic immediately below the visible caption bounds. Calibrate to the actual footage; the preset coordinates are examples, not universal face tracking.

Build one idea at a time: title, diagram elements, connecting lines, readable hold. Time meaningful changes to the spoken concept. Reuse a diagram later when the speaker returns to the same idea. Prefer restrained drawing, small slides, fades and separation over constant motion.

Use original vector geometry or procedural shapes, animated type and paths. The reference contains full-screen cards, but this approved style keeps the presenter visible; use full-screen takeovers only if requested. Do not automatically add brand slogans or an opening title. EDDIE is the editing style name, not a character that belongs in every video.

Adapt graphics to the topic. A waveform, splitting timeline, clip tiles, upload branches, calendar/clock and connected workflow are demonstrated patterns, not mandatory visuals for unrelated videos. Illustrative waveforms are not audio measurements; clocks are not time-savings claims. Only use numbers or graphs supported by the supplied script or evidence.

Use the supplied click as the only visual sound effect, normally two frames before each main graphic entrance or exit. Deduplicate adjacent cues and remove orphaned cues. Preserve approved music and keep speech dominant; do not invent speech or clone a voice.

## Render and verify

A preview request stops at the requested duration. Keep preview-only trims separate from the full edit. When the user approves a style and asks for the full video, carry that style through the full retained timeline.

Inspect the encoded output, including hero frames and contiguous transition strips. Check face clearance, caption-to-graphic spacing, readable labels, stable component positions, complete last syllables and correct click timing. Decode the delivered file and check audio levels. Distinguish measured signal or transcription checks from an actual listening review.

Save a versioned export and verify the delivery copy. Public distribution of reusable skill files does not automatically include private footage, reference videos, transcripts, paid assets or audio. Report the final file and any unresolved limitation honestly.

## EDDIE Motion 1.0.0 specification

## Layout and typography

- Vertical 1080 x 1920, normally 30 fps; adapt to the source and requested delivery.
- Presenter remains visible. Preserve the original footage as the base layer.
- Caption reference center: y1150. Graphic reference top: y1200, roughly 20 px beneath the visible caption edge. Recalibrate to the actual neckline and glyph bounds.
- Captions: 1-3 spoken words per chunk, around 67 px at this resolution. Shrink long chunks to fit an 880 px maximum line width. Preserve punctuation and wording.
- Use a bold sans-serif for ordinary speech and a compatible serif italic for selected meaningful terms. The approved example uses Arial Bold and Georgia Italic where installed. Discover local fonts or choose licensed equivalents; do not bundle proprietary fonts.
- White #FFFFFF, warm gold #E8C76B, navy #0D1D2B. Dark caption outline around 3 px; a restrained lower gradient may support contrast while leaving the face clear.
- Standard dark motion card: approximately 900 x 450 px, 24 px corner radius, nearly opaque black/navy. Gold uppercase title, fine divider, concise white labels.
- Explanatory callback card: approximately 940 x 500 px, cream #F7F5EF, dark #161616 type, muted gold #B29A58 connectors and #E9E2D1 node fills.
- Avoid paragraphs and decorative clutter. Fine diagram text must remain readable on a phone.

## Motion grammar

1. Main card enters with 0.90 to 1.00 scale and at most 12 px upward settling over 0.20 seconds, cubic ease-out. Alpha rises over approximately 0.067 seconds.
2. A thin divider draws over roughly 0.30 seconds. Labels or objects arrive in stages anchored to the words they explain.
3. Connectors draw over 0.25-0.45 seconds. Arrowheads arrive at the end of the path. Keep label baselines steady while connectors move.
4. Hold the completed explanation. Animate continuously only when motion conveys meaning, such as recording activity.
5. Main graphic exits in roughly 0.10 seconds. Avoid long crossfades and unnecessary spinning or bouncing.
6. Snap events to output frames. Calculate every state from timeline time so scrubbing and rendering are deterministic.

Short internal staggers around 0.12-0.15 seconds may clarify a build, but do not replace transcript anchoring with a uniform timer.

## Reusable patterns

| Spoken idea | Motion treatment |
| --- | --- |
| Introduce an editing agent | Typographic name and small animated activity bars; no robot picture |
| Record | Outlined recording panel with an illustrative moving waveform |
| Cut | Draw a vertical cut line, then separate two timeline segments |
| Clip | Reveal several portrait-format tiles with simple play symbols |
| Upload | Draw branches from one video node to several destination nodes |
| Work full time | Populate a simple calendar and move a clock hand to its resting position |
| Connected system | Rebuild the earlier steps as a connected diagram and hold the completed map |
| Ownership or control | A document, team or control diagram tied directly to the actual words |

An optional small progress line can connect process steps as they are mentioned. Use a fixed baseline through neighboring beats; different asset heights must not make it jump. Example baseline y1672 with a 135 px strip under a 450 px card. Do not show this process strip when the topic no longer concerns those steps.

These examples illustrate editing services; adapt their concepts to each user's topic. Do not paste an editing workflow onto an unrelated medical or educational script.

## Audio

Use the user's supplied click exclusively for visual effects. Place it two output frames before major graphic changes; do not click every line segment or word. Merge cues less than about 0.15 seconds apart. Use consistent gain calibrated to the supplied sound. Preserve the speaker's voice and approved quiet instrumental. Remove cues whenever their corresponding graphic is removed.

## Full edit and quality

- Keep a source-to-edited word map. Do not apply original timestamps directly to cut footage.
- Keep previews separate; a 20-second sample may have an excerpt offset or short end hold that does not belong in the full edit.
- Preserve approved initial and closing speech. A clean caption-only moment is preferable to an unrelated filler graphic.
- Inspect encoded motion sequences, not just still frames. Check sudden shifts, flashes, doubled entrances, label overflow and graphic/caption collisions.
- Export a new file, verify its complete decode, duration, frame coverage and audio peaks, and document any unperformed listening review.
- Keep project media out of the public repository. Classic remains its own independent style and preset.
