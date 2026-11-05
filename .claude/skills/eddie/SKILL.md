---
name: eddie
description: Edit videos with EDDIE MASTER EDITOR using captions and a hook, optional Google topic images, automatically selected Rapid Fire Q&A/rankings, or Sync and Async reaction videos. All modes default to 150% audio; on-screen iPhone messages are opt-in.
---

# EDDIE MASTER EDITOR — DWC Agent Eddie

MASTER EDITOR follows the simplified Preview 3 treatment: clean talking-head cuts, stationary captions, and optional supplied still pictures with a click cue. Standard captions and topic pictures remain stationary. The explicitly requested iPhone-message option below is an exception. Read [the style specification](references/style.md) before editing. Current user directions override defaults. Other EDDIE styles remain separate.

For first-use setup or the START HERE prompt, read [the welcome flow](../../../ONBOARDING.md). Keep normal editing requests direct; do not force onboarding.

## Five modes: select from the brief and script

Honor an explicit mode or existing approved edit. Otherwise inspect the script/transcript:
1. **Captions + text hook**: default for ordinary talking-head speech without an image request. Stationary Eddie captions and a rounded white hook; no topic images.
2. **Captions + Google images + text hook**: use when the user wants supporting topic pictures with explanatory speech. Search actual spoken terms on Google Images, select a suitable landscape image, preferably 16:9, using [image selection and rounded cards](references/image-selection.md), retain source URLs in the private project and use supplied/explicitly selected images in preference to search. Preserve aspect ratio and watermarks. Place pictures below captions with a small gap; hold for the discussed concept. Do not silently substitute generated pictures.
3. **Rapid Fire — text hook + captions + Google images**: auto-select for repeated short questions with yes/no answers or rankings. Read [Rapid Fire](references/rapid-fire.md) for question/answer timing, larger /10 scores, Google images and AI/recorded interviewer options.

4. **EDDIE Sync Reaction**: source clip with synchronized bottom-left doctor inset, then full-screen commentary. Read [reaction selection](references/reaction.md) and [Sync Reaction](references/reaction-sync.md).
5. **EDDIE Async Reaction**: full-screen source excerpt, then separately recorded full-screen doctor commentary, with optional supporting images/study excerpts below EDDIE captions. Read [reaction selection](references/reaction.md) and [Async Reaction](references/reaction-async.md). Both reaction modes override ordinary talking-head placement during source playback. Script-only input receives a plan until footage is provided.

All five modes use **150% audio gain** (1.5× amplitude, about +3.52 dB), plus peak protection to prevent clipping. Apply this once to the clean source; do not repeatedly double already processed exports. Inspect source gain/history and output peaks, preserve sync, and use a limiter as needed without uncontrolled loudness normalization. Explain if peak limiting reduces the gain on loud peaks. Honor any explicit audio override.

All five modes use the [shared text hook](references/text-hook.md): top-centered wide rounded white box, maximum two lines, bold black text with selected red emphasis, visible from 0–3 seconds. Center the visible text with equal top/bottom padding. An explicit no-hook request overrides this default. Read the shared reference before placing any hook.

Explicit on-screen SMS/iPhone messages enable the additional [iPhone message treatment](references/iphone-messages.md). Ordinary captions, hooks, or merely saying “text” do not activate notifications.

With a script alone, prepare the hook, question/answer map and visual plan; do not claim a rendered video or invent doctor answers. Use available footage and generate question audio only when requested. For mixed or unclear formats, follow clear segments or ask one focused question only when necessary.

## Default quality pass for every practice

For every new edit in all five modes, apply [quality defaults](references/quality-defaults.md): complete speech cleanup and second-pass review, conservative voice isolation/denoise, a single 150% audio gain, centered proportional framing without accidental edge bars, and 4K delivery. Honor user overrides and preserve approved audio/cuts during visual-only revisions. These are editing instructions, not model fine-tuning or a promise of error-free results.

## Establish the edit

For recorded speech in every video mode, read and apply [speech cleanup and delivery review](references/speech-cleanup.md). Run the four-pass workflow: source and overlapping excerpt audit, clean speech and join review, rebuilt captions/visual timing, then actual export playback and technical checks. Use the bundled candidate scanner; resolve every issue in a private ledger. A full-length transcript or successful render is not a release check. Unresolved issues block final delivery; unavailable listening requires an explicitly provisional review.

Use the user's footage, output folder, any supplied pictures and optional click audio. Captions-only is a complete supported edit; do not require pictures or sound to start it. Inspect available local editing tools and transcription. Preserve originals. Do not assume a paid service or a particular workstation.

Clean recording setup, false starts, coughs and excessive gaps while preserving meaning, natural delivery, complete first/last words and closing phrases. Check every join in context so quiet syllables are not cut off. Keep an approved cut intact when revising only captions or visuals. Retain source ranges and retime captions after editing.

## Shared subject framing — all five modes

Before overlays, read [subject framing](references/framing.md). Automatically correct unintentionally off-center direct-to-camera talking-head shots using a stable, proportional crop. Preserve intended side angles, nurse/interview compositions and reaction layouts. Frame first, then calibrate stationary captions and visuals. Use the shared top-hook layout in all five modes.

### Clean voice and centered talking-head cuts

For new direct-to-camera talking-head edits, keep the head centered horizontally in both the base shot and tighter shots. Reframe the clean footage before overlays; preserve the complete hairline, natural headroom and useful gestures. Use a stable crop rather than chasing small head movements. Preserve intentional side angles, interviews and reaction compositions.

Use restrained cut-ins and cut-outs at meaningful sentence/section transitions or to conceal a necessary speech edit. Start with a modest tighter crop (roughly 1.08–1.15 times the base crop, only if resolution permits), hold through the thought, then return to the base crop. These are purposeful shot changes, not continuous zooms or changes on a fixed timer. Keep the head centered at both scales; inspect the join for distracting head jumps. Apply crops before captions/hooks/images so overlays remain stationary, readable and unscaled. Preserve approved framing for unrelated revisions.

Assess room hiss, hum and background noise before the single 150% gain stage. Use conservative noise reduction only when noise is audible; compare processed and original speech at matched loudness. Preserve consonants, breaths and a natural voice; reduce or bypass processing if it creates metallic, watery or gated sound. Never repeatedly denoise or amplify an already processed export. Check quiet phrases, pauses, sibilants and edit joins by listening to the actual export. Record the filter/settings and whether listening was completed; signal measurements cannot certify natural sound. If a supplied reference is byte-identical to the previous export, disclose that and do not claim to have learned new processing from it.

## Compose

Do not add bottom explanatory notes, claim explanations, or educational footnote panels in any EDDIE mode. Keep spoken captions, the requested hook and topic images; explanation notes require a new explicit request for that specific video.

Keep the presenter visible as the base layer. Use bold white captions with a black outline in short speech-synced phrases. Calibrate one fixed position just below the beard/base of the neck, then keep it stationary: no tracking, bouncing, sliding, scaling or animated word emphasis.

For images, follow the selected mode above and match each picture to the spoken concept. Preserve their content and proportions; do not generate replacements or add unrelated logos, diagrams or workflow animations. Pictures appear immediately below the captions with a small gap, hold still, and disappear or replace instantly when the topic changes. Here, a pop-up means a hard on/off appearance, not a scale or fade animation. EDDIE is the skill name, not an instruction to add a robot image.

For mode 1, omit all picture and click events. For a requested short preview, deliver that duration; do not silently move topic cues just to fit pictures into it. Otherwise complete the authorized full edit.

For user-requested screenshot matching, persistent hooks, full-screen stills, transparent product cutouts, or slide/whoosh cues, read [requested visual revisions](references/requested-overrides.md). These opt-in treatments override defaults only for the requested edit.

For sourced and supplied topic images, apply [image selection and rounded cards](references/image-selection.md): prefer relevant 16:9 landscape photos, with rounded corners and a subtle shadow on rectangular cards. Preserve transparent cutouts and explicit user overrides.

## Optional iPhone messages

Enable only when the user requests text messages or iPhone notifications on camera/on screen. Ordinary speech captions and text hooks do not trigger this mode. Read [iPhone message treatment](references/iphone-messages.md) when enabled; keep normal captions stationary.

## Sound and delivery

When the user supplies and wants a click, play it approximately two frames before each picture appears. Do not require or synthesize a substitute sound. No exit click, repeated caption clicks, other sound effects, added music or new speech by default. Apply the shared 150% gain once, preserving an approved treatment and any explicitly requested music. Remove cues belonging to removed pictures.

Inspect the encoded opening, picture events, stationary captions, every revised join and final spoken word. Verify caption timing/bounds, image separation, full-file decode, duration, dimensions, A/V sync and audio levels. Distinguish signal/transcription checks from actual listening; report review limits honestly.

Save a newly named MP4 in the requested folder without overwriting originals or earlier exports. Keep media, transcripts, edit decisions and verification notes in ignored projects/. Public packages contain reusable instructions and presets only. Upload or public sharing follows the user's authorization for the destination.
