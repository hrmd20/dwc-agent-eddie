# DWC AGENT EDDIE

**Digital White Coat content workflows: EDDIE MANAGER, EDDIE MASTER EDITOR, Carousel, Landscape, Sync Reaction, Rapid Fire and EDDIE Claude. Async Reaction is included inside Master Editor. EDDIE INSIDER TEXT is its named message-commentary variant.**

## New here? Start here

**No editing commands needed.** Download and unzip this folder, open it in an AI assistant that can edit local files, and paste:

> Read AGENTS.md and ONBOARDING.md in this folder. Help me make my first EDDIE video. Check what is ready on this computer, explain anything missing in plain language, and recommend a style from my footage. Start with a short preview before making the full video.

**[Read the practice's Start Here guide](START%20HERE.md)** · After downloading, double-click **START HERE.html** for a visual guide.

EDDIE guides your first edit, recommends a style and checks the tools. The download contains instructions and presets; it is not a standalone editor and cannot launch itself. Your assistant may need one-time tool setup. See [requirements](#requirements).

## Choose your style

| Style | Style version | Visual treatment | You provide |
| --- | --- | --- | --- |
| **EDDIE MASTER EDITOR** | 1.1.0 | **1. Captions + hook:** Eddie captions and a 3-second text hook.<br><br>**2. Captions + Google images + hook:** Adds relevant images below the captions.<br><br>**3. Rapid Fire:** Question-and-answer timing, Google images, large ratings or answer labels, and a 3-second hook.<br><br>**4. Sync Reaction:** Original clip with synchronized doctor inset, then full-screen commentary.<br><br>**5. Async Reaction:** Full-screen source clip, then separate full-screen doctor commentary with supporting images/study excerpts below EDDIE captions. | Your recording; for Reaction, the original clip and your reaction recording |
| **EDDIE INSIDER TEXT** | 1.0.0 | Full-video charcoal/yellow hook close above the head, captions below the lips, supplied message screenshots; optional requested blur/beep censorship | Recording, message screenshots and hook wording |
| **EDDIE MANAGER — BASIC** | 1.1.0 | Vista Social uploads, channels, captions, scheduling, public replies, Opening DM and resource DM | Approved videos, matching scripts and connected Vista Social profiles |
| **EDDIE Carousel** | 1.0.0 | Original educational carousels filled into your own Canva template | Editable Canva template, topic and optional inspiration |
| **EDDIE Landscape** | 1.0.0 | 4K 16:9, stationary white outlined captions and clean speech cuts | Video, optional script |
| **EDDIE Claude** | 1.0.0 | Best-take cuts with audited word edges, face-centered alternating zooms, AI noise removal, EDDIE captions, white text hook and your pictures, frame-accurate sync | Raw video, hook wording, optional pictures and hook image |

MASTER EDITOR keeps the presenter visible and places short captions at the base of the neck. Optional iPhone notifications activate only when requested.

The latest repository adds **EDDIE Landscape 1.0.0** and **EDDIE Sync Reaction 1.0.0** alongside MASTER EDITOR and Carousel. **EDDIE MASTER EDITOR 1.1.0** now uses the simplified Preview 3 treatment: stationary white outlined captions, optional still pictures that appear instantly, and optional click-before-image cues. Notification animation is opt-in. Existing projects keep their copied settings until you request this update. [Classic-only v1.0.0](https://github.com/hrmd20/dwc-agent-eddie/releases/tag/v1.0.0) remains available.

## Download and start

1. Click **Code → Download ZIP** and extract it, or clone:

   ```sh
   git clone https://github.com/hrmd20/dwc-agent-eddie.git
   cd dwc-agent-eddie
   ```
2. Open the folder in your editing agent.
3. Choose your workflow. For videos, provide footage and an output folder; Sync Reaction can use your supplied click sound; Async Reaction does not require one. MASTER EDITOR supports captions-only, or your own pictures with an optional click, and Reaction needs both the original clip and your reaction recording. For Carousel, share your own editable Canva template, topic and inspiration.
4. Use one of these prompts:

**EDDIE MASTER EDITOR**

> Use EDDIE MASTER EDITOR to edit this talking-head video. Keep me visible with stationary bold white captions outlined in black, just below my beard at the base of my neck. Use only my supplied pictures directly below the captions, appearing and disappearing instantly with no animation. If I provide and request a click, play it just before each picture. With no pictures, use captions only. Start with a 10-second placement preview.

**EDDIE INSIDER TEXT**

> Use EDDIE INSIDER TEXT. Keep a large charcoal/yellow hook close above my head throughout the video, captions below my lips and my supplied messages below them. Preserve complete words at the ending and show me a 4K review copy before uploading.

**EDDIE Carousel**

> Use EDDIE Carousel. First ask me for my own Canva template that you are allowed to edit, my topic and audience, and posts or accounts for inspiration. Work in a copy of my template, preserve my branding, and create original slide copy and a social caption. Verify medical claims and return the editable Canva draft for my review.

### Your template, your account

No DWC Canva templates are included. On first use, EDDIE Carousel asks for your own template and checks that your connected Canva account can edit it. It preserves the master by using a working copy and follows the template's page count, fonts, colors and layout. Inspiration is optional; your topic is enough to begin writing. Never share your password or make your template publicly editable just to use the skill.

The prompt appears when you invoke EDDIE Carousel in a compatible agent. Downloading the ZIP alone does not run an app or open a setup wizard.

### Optional daily inspiration

Ask the agent to set up daily research for your chosen accounts, specifying the time, time zone and whether you want ideas or Canva drafts. Each doctor configures their own account access and scheduler. The agent records sources, skips previously processed posts, writes original content and checks health claims. It cannot guarantee access to every social account. Downloading EDDIE does not activate a schedule, and this workflow does not automatically post to social media.

A video preview request stops at the preview. After approval, ask for the full video. If you already specify an approved style and request a complete edit, the agent can continue through editing and verification.

## Create a private project

```sh
python3 scripts/new_project.py my-master-video --style master
python3 scripts/new_project.py my-carousel --style carousel
python3 scripts/new_project.py my-insider-video --style insider-text
```

Omitting `--style` keeps the original MASTER EDITOR default. The helper copies the chosen preset into an ignored `projects/<name>/` folder. Video projects contain assets, transcripts, renders and QA; Carousel projects contain sources, copy, exports, QA and a private setup brief. It refuses to overwrite an existing project. Updating this repository does not silently change a project's copied preset.

## Included files

| Location | Purpose |
| --- | --- |
| `.agents/skills/eddie/` | EDDIE MASTER EDITOR skill and reference for Codex |
| `.agents/skills/eddie-carousel/` | Self-contained Canva carousel workflow for Codex |
| `.claude/skills/` | Matching skills for Claude Code |
| `presets/eddie.json` | EDDIE MASTER EDITOR 1.1.0 defaults |
| `presets/eddie-carousel.json` | Carousel defaults; monitoring starts disabled |
| `.agents/skills/eddie-claude/` | EDDIE Claude skill and `scripts/eddie_claude.py` toolkit |
| `presets/eddie-claude.json` | EDDIE Claude 1.0.0 defaults |
| `scripts/new_project.py` | Private project starter with style selection |
| `AGENTS.md` / `CLAUDE.md` | Style routing and workspace instructions |

Invoke `eddie` for MASTER EDITOR, `eddie-carousel` for Carousel in agents that discover repository skills. You can also point the agent directly to the relevant SKILL.md.

## Requirements

This is an **agent-guided skill package**, not a standalone editor or automatic publishing service. The starter creates folders and settings; it does not render videos or edit Canva by itself.

**Carousel:** use an agent with a connected Canva integration or supported signed-in browser, access to your editable design, and web research tools. A scheduler is needed only for recurring runs. Canva capabilities and any plan requirements depend on your own account and integration. No particular agent model is required.

**Video editing:** install separately:

- An editing agent that can read skills and run local tools.
- Python 3.9+ for the project helper; it uses only the standard library.
- FFmpeg and FFprobe for inspection and export.
- A word-timestamp transcription engine, such as local Whisper.
- A compositor supported by the agent, such as HyperFrames or Python/Pillow.
- Locally available, properly licensed fonts. No proprietary fonts are bundled.

The agent should check tools before editing. No video style requires a paid service. Users supply source footage, sound and any licensed music; MASTER EDITOR can use supplied pictures or Google images in image modes; click audio is optional for MASTER EDITOR.

For the broader toolkit, see [Nate Herk's HyperFrames Student Kit](https://github.com/nateherkai/hyperframes-student-kit). Its installation guide covers the original toolkit and dependencies; EDDIE's chosen style controls the resulting edit.

## Versions and sharing

Keep new styles separate and publish numbered releases. Preserve old presets and downloads so users can repeat an approved look. MASTER EDITOR and Carousel remain separate workflows.

Public files are reusable instructions, presets and helpers. Footage, exports, transcripts, private Canva links, account preferences, source notes, reference videos, paid stock, click audio and credentials stay local under ignored project directories. No robot portrait, stock subscription, audio file or private demonstration video is bundled.

## Credits

Built from the DWC editing workflow developed with Digital White Coat and informed by [Nate Herk's HyperFrames Student Kit](https://github.com/nateherkai/hyperframes-student-kit). EDDIE's neckline layout, MASTER EDITOR picture treatment are DWC customizations. This repository is not affiliated with or endorsed by Nate Herk, HeyGen, or HyperFrames.

The upstream MIT notice is preserved in `LICENSE`. Third-party tools and assets retain their own licenses. No AIS branding or upstream showcase videos are included.


## EDDIE Claude 1.0.0

**EDDIE Claude** is a separate vertical style built and tested with Claude Code. It keeps the cleanest take of every line, checks every cut edge so no word is clipped or doubled, centers the presenter's face in every shot with alternating 1.12×/1.30× zooms, removes background noise and chair creaks with DeepFilterNet plus a voice-energy gate, and cuts on exact frames so audio never drifts. It uses stationary white EDDIE captions, the white rounded text hook with red emphasis, an optional hook image and your own pictures below the captions. No explainer notes are added.

> Use EDDIE Claude to edit this raw talking-head video. Keep the best take of every line, center my face in every shot, remove background noise and chair creaks, and use white captions, the text hook "Normal Total Testosterone? / Check Your Free T" and my pictures. Verify sync and that no words are cut off.

```sh
python3 scripts/new_project.py my-claude-video --style claude
```

**Quick start in Claude Code:** download the ZIP, open the folder in Claude Code and paste the prompt above with your video path. Claude installs the tools into the folder on first use with `bash scripts/setup_eddie_claude.sh` (add `--denoise` for DeepFilterNet), so no manual setup is needed. See the [Start Here guide](START%20HERE.md#using-eddie-claude-in-claude-code).

The toolkit `scripts/eddie_claude.py` inside the skill runs each step (`transcribe`, `clean-audio`, `cut`, `audit`, `faces`, `render`, `captions`, `compose`, `verify`). It needs FFmpeg with libass, `numpy`, `pillow`, `faster-whisper`, `opencv-python-headless<5` and, for strong noise removal, `deepfilternet`. See [.agents/skills/eddie-claude/SKILL.md](.agents/skills/eddie-claude/SKILL.md). Defaults: [presets/eddie-claude.json](presets/eddie-claude.json).

## EDDIE Landscape 1.0.0

The approved V1 Revision 3 landscape treatment is available as **EDDIE Landscape**, alongside the existing styles. It uses 4K 16:9 presenter footage, stationary bold white lower-center captions with a black outline, and natural cuts that remove coughs, repeated takes and delays while preserving complete words. No graphics, images, music or click effects are added by default.

Users supply their own footage, optional script and output folder. Lower-resolution sources are upscaled for 4K delivery; exporting in 4K does not restore missing detail.

> Use EDDIE Landscape to edit my video in 4K 16:9. Use stationary bold white captions with a black outline at lower center. Remove coughs, repeated takes and long pauses, preserve every complete word and closing phrase, and deliver an MP4 plus SRT in my output folder.

```sh
python3 scripts/new_project.py my-landscape-video --style landscape
```

Invoke `eddie-landscape` in your agent, or load [.agents/skills/eddie-landscape/SKILL.md](.agents/skills/eddie-landscape/SKILL.md). Matching Claude instructions live in `.claude/skills/eddie-landscape/`; reusable defaults are in `presets/eddie-landscape.json`. The project starter creates a private brief and preset; the editing agent performs the edit using separately installed local video tools.


## EDDIE Rapid Fire (Text hook, captions, images)

Rapid-fire questions and rankings with original audio, stationary Eddie captions, clear /10 scores, topic images beneath captions, and a rounded translucent charcoal hook with white text and yellow emphasis, positioned just above the head for the first 3 seconds.

> Use EDDIE Rapid Fire to edit my recording. Add the hook at the top for 0–3 seconds, highlight my selected phrase in red, and show one image per question below the captions. Keep my original audio.

Create a private project with `python3 scripts/new_project.py my-rapid-fire --style rapid-fire`. Read [.agents/skills/eddie-rapid-fire/SKILL.md](.agents/skills/eddie-rapid-fire/SKILL.md) for Codex or the matching `.claude/skills/eddie-rapid-fire/SKILL.md` for Claude. Defaults: [presets/eddie-rapid-fire.json](presets/eddie-rapid-fire.json).

## EDDIE MASTER EDITOR naming and optional messages

EDDIE MASTER EDITOR is the new name for EDDIE Classic. The `eddie` skill path and `presets/eddie.json` remain stable. Use `--style master`; legacy `--style classic` commands still work. Existing projects keep their copied settings.

Request iPhone messages or notifications on screen to enable the optional glass-message treatment: sender and timestamp, smooth upward entrance, notification sound, and optional blurred introduction followed by a readable reveal. Captions or a text hook alone do not enable it.

### Automatic Rapid Fire mode

EDDIE MASTER EDITOR detects repeated short questions, yes/no answers and rankings from your script or recording. It uses Eddie captions, a rounded translucent charcoal hook with white text and selected yellow emphasis just above the doctor’s head for the first **3 seconds**, larger /10 scores and Google topic images directly below captions. Supplied images and explicit style choices take priority. With a script alone it prepares the plan; footage or requested voice generation is needed to produce the video. AI interviewer and recorded nurse options are supported.

## Master Editor: five modes

1. **Captions + text hook** — no topic pictures.
2. **Captions + Google images + text hook** — supporting pictures below captions.
3. **Rapid Fire** — automatically selected for short Q&A/ranking scripts; hook, captions, Google images and large /10 scores.

4. **Sync Reaction** — original clip with synchronized presenter inset, followed by full-screen commentary.
5. **Async Reaction** — full-screen source excerpt, then separately recorded full-screen doctor commentary with optional supporting visuals below EDDIE captions.

The shared default is a **3-second hook positioned at the doctor’s hairline with a small upward clearance**, maximum two lines, ONE translucent gray rounded rectangle enclosing both lines, fitted to the complete text block, large bold white text/yellow keyword emphasis and minimal equal padding. All five target **−14 LUFS integrated** with peak protection. Async Reaction uses a four-second hook placed around the source captions and heavy white reaction captions in short beats. Explicit user choices override defaults. iPhone message overlays remain optional.

### Shared subject framing

All five Master Editor modes inspect the footage before overlays. Direct-to-camera talking heads are centered when needed with a stable proportional crop, intact headroom and room for captions and images. Intentional side angles, interviews and reaction layouts remain intact. The shared head-relative hook is the default in all five modes. Reframing preserves recorded gaze and does not synthesize eye contact.

### Sync and Async Reaction inside Master Editor

Master Editor includes both reaction styles:

- **EDDIE Sync Reaction:** source clip with synchronized bottom-left doctor inset, then full-screen commentary. The existing standalone `eddie-reaction` skill and `--style reaction` command remain compatible; the displayed name is now EDDIE Sync Reaction.
- **EDDIE Async Reaction:** full-screen source excerpt first, then separately recorded full-screen doctor commentary. Start the doctor’s response on the first substantive line or the requested phrase. Use the Hormozi med-spa treatment for framing, a four-second source hook and short white caption beats. Optional supporting visuals sit below the reaction captions.

Say which format you want, or provide footage and a brief so Master Editor can choose. Existing approved edits retain their style. Both apply 150% audio gain once with peak protection. Script-only input produces a plan until footage is supplied.

```bash
python3 scripts/new_project.py my-sync-reaction --style sync-reaction
python3 scripts/new_project.py my-async-reaction --style async-reaction
```

Instructions: [Sync](.agents/skills/eddie/references/reaction-sync.md) · [Async](.agents/skills/eddie/references/reaction-async.md).

### Master Editor quality defaults for every practice

All five Master Editor modes now default to **4K delivery**, **150% audio applied once**, conservative **voice isolation and denoise**, a second speech-cleanup pass, and checks for accidental black edge bars. Keep the presenter centered, preserve complete words and natural pauses, and retime captions/images after edits. User overrides and approved edits take precedence. Preview links come before posting-folder moves or uploads.

Read the [quality defaults](.agents/skills/eddie/references/quality-defaults.md). These instructions require actual export review; automated transcripts and successful renders cannot guarantee that every mistake was removed. An export without a full listening check must be labeled provisional.

## EDDIE MANAGER — BASIC

[EDDIE MANAGER — BASIC](.agents/skills/eddie-manager/SKILL.md) takes approved videos and their matching scripts through an educational publishing workflow:

- Upload approved videos to Vista Social without changing the approved edit.
- Select all intended connected brand channels, while keeping unrelated accounts unselected.
- Add script-based captions and approved first comments, preserving platform-specific edits.
- Schedule at the requested date, time and timezone; the default is one video per day at 9 AM.
- Attach a keyword trigger to the exact post on supported profiles.
- Reply publicly to the keyword comment, send an Opening DM with a button, then deliver the approved information after the recipient taps the button.

BASIC captions focus on exchanging useful information: **no booking links or consultation offers**. The keyword, caption and promised resource must agree. Public replies and DMs are configured only where supported; publishing to a channel does not imply that channel supports DM automation.

Example: “Use EDDIE MANAGER BASIC to upload these approved videos to my selected practice channels, schedule one per day at 9 AM, and add educational captions and first comments. Link each keyword to a public reply, an Opening DM button, and the approved resource DM.”

It checks the calendar and exact profile/post IDs to avoid duplicates and wrong-brand uploads. The included [Telemed ED example](.agents/skills/eddie-manager/references/ed-basic-example.md) records the approved three-action flow. Other practices use their own approved accounts, wording and resources. Saved/active status is verified separately from actual delivery.

Requires connected Vista Social tools or an authenticated browser for unsupported actions. Installing or updating the skill does not itself schedule posts or activate automations.

## EDDIE Quality Check

Local speech alignment and export QC now produce timestamped findings, optional review clips, and a hash-bound release report. Checks cover cut boundaries, repeats, gaps, ASS captions, decode, black/frozen frames and audio peaks. Full playback, layout and natural audio review remain required; skipped checks cannot silently pass. See [.claude/skills/eddie-quality-check/SKILL.md](.claude/skills/eddie-quality-check/SKILL.md). Install its isolated Python requirements for WhisperX; the scanner itself uses Python plus FFmpeg/FFprobe.
