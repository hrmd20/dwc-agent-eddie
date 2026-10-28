---
name: eddie
description: Edit videos with EDDIE MASTER EDITOR using captions and a hook, optional Google topic images, automatically selected Rapid Fire Q&A/rankings, or synchronized reaction videos. All modes default to 200% audio; on-screen iPhone messages are opt-in.
---

# EDDIE MASTER EDITOR — DWC Agent Eddie

MASTER EDITOR 1.1.0 follows the simplified Preview 3 treatment: clean talking-head cuts, stationary captions, and optional supplied still pictures with a click cue. Standard captions and topic pictures remain stationary. The explicitly requested iPhone-message option below is an exception. Read [the style specification](references/style.md) before editing. Current user directions override defaults. Other EDDIE styles remain separate.

## Four modes: select from the brief and script

Honor an explicit mode or existing approved edit. Otherwise inspect the script/transcript:
1. **Captions + text hook**: default for ordinary talking-head speech without an image request. Stationary Eddie captions and a rounded white hook; no topic images.
2. **Captions + Google images + text hook**: use when the user wants supporting topic pictures with explanatory speech. Search actual spoken terms on Google Images, select the first displayed relevant image (including sponsored results when relevant), retain source URLs in the private project and use supplied/explicitly selected images in preference to search. Preserve aspect ratio and watermarks. Place pictures below captions with a small gap; hold for the discussed concept. Do not silently substitute generated pictures.
3. **Rapid Fire — text hook + captions + Google images**: auto-select for repeated short questions with yes/no answers or rankings. Read [Rapid Fire](references/rapid-fire.md) for question/answer timing, larger /10 scores, Google images and AI/recorded interviewer options.

4. **Reaction**: select when reacting to an original clip with presenter footage or an approved composite. Read [Reaction](references/reaction.md) for synchronization, source playback, presenter inset, separate caption tracks and full-screen commentary. These mode-specific rules take priority over standard talking-head placement. Script-only reactions receive a plan until the required footage is available.

All four modes use **200% audio gain** (2.0× amplitude, about +6.02 dB), plus peak protection to prevent clipping. Apply this once to the clean source; do not repeatedly double already processed exports. Inspect source gain/history and output peaks, preserve sync, and use a limiter as needed without uncontrolled loudness normalization. Explain if peak limiting reduces the gain on loud peaks. Honor any explicit audio override.

The first three modes include a text hook for the first **4 seconds** by default: black lettering on a rounded white background, with requested emphasis in bright red. Position below the captions, clear of the face. Use supplied wording; otherwise propose an accurate hook from the script. A captions-only request explicitly excluding a hook overrides this default. Keep hook and image areas from overlapping; show images after the hook or use a separately approved clear area.

Explicit on-screen SMS/iPhone messages enable the additional [iPhone message treatment](references/iphone-messages.md). Ordinary captions, hooks, or merely saying “text” do not activate notifications.

With a script alone, prepare the hook, question/answer map and visual plan; do not claim a rendered video or invent doctor answers. Use available footage and generate question audio only when requested. For mixed or unclear formats, follow clear segments or ask one focused question only when necessary.

## Establish the edit

Use the user's footage, output folder, any supplied pictures and optional click audio. Captions-only is a complete supported edit; do not require pictures or sound to start it. Inspect available local editing tools and transcription. Preserve originals. Do not assume a paid service or a particular workstation.

Clean recording setup, false starts, coughs and excessive gaps while preserving meaning, natural delivery, complete first/last words and closing phrases. Check every join in context so quiet syllables are not cut off. Keep an approved cut intact when revising only captions or visuals. Retain source ranges and retime captions after editing.

## Shared subject framing — all four modes

Before overlays, read [subject framing](references/framing.md). Automatically correct unintentionally off-center direct-to-camera talking-head shots using a stable, proportional crop. Preserve intended side angles, nurse/interview compositions and reaction layouts. Frame first, then calibrate stationary captions and visuals. The supplied top-hook example is an optional layout, not a replacement for the existing below-caption hook.

## Compose

Keep the presenter visible as the base layer. Use bold white captions with a black outline in short speech-synced phrases. Calibrate one fixed position just below the beard/base of the neck, then keep it stationary: no tracking, bouncing, sliding, scaling or animated word emphasis.

For images, follow the selected mode above and match each picture to the spoken concept. Preserve their content and proportions; do not generate replacements or add unrelated logos, diagrams or workflow animations. Pictures appear immediately below the captions with a small gap, hold still, and disappear or replace instantly when the topic changes. Here, a pop-up means a hard on/off appearance, not a scale or fade animation. EDDIE is the skill name, not an instruction to add a robot image.

For mode 1, omit all picture and click events. For a requested short preview, deliver that duration; do not silently move topic cues just to fit pictures into it. Otherwise complete the authorized full edit.

## Optional iPhone messages

Enable only when the user requests text messages or iPhone notifications on camera/on screen. Ordinary speech captions and text hooks do not trigger this mode. Read [iPhone message treatment](references/iphone-messages.md) when enabled; keep normal captions stationary.

## Sound and delivery

When the user supplies and wants a click, play it approximately two frames before each picture appears. Do not require or synthesize a substitute sound. No exit click, repeated caption clicks, other sound effects, added music or new speech by default. Apply the shared 200% gain once, preserving an approved treatment and any explicitly requested music. Remove cues belonging to removed pictures.

Inspect the encoded opening, picture events, stationary captions, every revised join and final spoken word. Verify caption timing/bounds, image separation, full-file decode, duration, dimensions, A/V sync and audio levels. Distinguish signal/transcription checks from actual listening; report review limits honestly.

Save a newly named MP4 in the requested folder without overwriting originals or earlier exports. Keep media, transcripts, edit decisions and verification notes in ignored projects/. Public packages contain reusable instructions and presets only. Upload or public sharing follows the user's authorization for the destination.
