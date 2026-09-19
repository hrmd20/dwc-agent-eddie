---
name: eddie
description: Edit talking-head videos in the Digital White Coat EDDIE style using supplied pictures, neckline captions, tight picture spacing, and click-before-pop timing. Use for EDDIE edits, style revisions, and short layout previews.
---

# EDDIE — DWC Agent Eddie

Read [the style specification](references/style.md) before editing. Current user directions override the defaults.

## Establish the edit

Inspect the actual source video, all supplied images and sound, and available local editing tools. Preserve originals. Use local transcription when configured; do not assume a cloud provider or paid service. Read the entire transcript, remove clear false starts and recording setup only when editing is requested, and retain the speaker’s meaning and complete last syllable. Preserve an approved cut when the request is only a layout revision.

Create a private project with source references, word timestamps, frame-aligned edit decisions, the retimed transcript, image events, sound cues, render source and verification notes. Keep private assets and transcripts under ignored projects/, not inside this public skill.

## Compose

Use the speaker as the continuous base. Match supplied pictures to the exact spoken concepts. Inspect image content rather than relying only on filenames. Do not generate replacement pictures, redraw logos, add stock or insert new title cards unless requested. Caption wording must match the retained speech.

Calibrate captions to the visible base of the neck/V-neck in the actual footage. Position each image immediately below the visible caption glyphs, preserving proportions and keeping the face clear. Follow the style reference for the latest approved geometry and motion. Save the same placement rules in the project configuration so future revisions remain consistent.

Only include a workflow animation if the user approves it or it belongs to an explicitly reused approved project. Approval of one graphic is not approval to add unrelated cards. EDDIE is a skill name; do not assume every video should contain a robot portrait.

For a requested 10-second preview, render only that duration. If no picture appears in the chosen interval, explain any preview-only retiming used to demonstrate the layout; preserve the full edit’s original event timing. Do not silently apply preview timing to the full export.

## Sound and export

Use the provided click exclusively for visual sound effects, normally two frames before the picture entrance. Remove cues for deleted visuals. Preserve approved music and voice treatment; use a quiet instrumental only when consistent with the brief. Do not add a new voice or spoken words.

Render a draft, inspect encoded hero frames and transition strips, then export. Verify duration, dimensions, frame coverage, caption/image separation, word alignment, final syllable and audio levels. Measure clipping and decode the whole delivered file. Distinguish audio signal/ASR checks from listening; never claim an unavailable review passed. Fix observable defects before delivery.

Use separate versioned output names. Save to the destination the user specified, and verify the copied file. Upload/public sharing needs the user’s authorization for that destination. If a folder has moved, locate it instead of recreating an obsolete directory. Deliver a link to the actual final file.
