# DWC AGENT EDDIE

**Five Digital White Coat content workflows: EDDIE MASTER EDITOR, Carousel, Landscape, Sync Reaction and Rapid Fire. Async Reaction is included inside Master Editor.**

## Choose your style

| Style | Style version | Visual treatment | You provide |
| --- | --- | --- | --- |
| **EDDIE MASTER EDITOR** | 1.1.0 | **1. Captions + hook:** Eddie captions and a 4-second text hook.<br><br>**2. Captions + Google images + hook:** Adds relevant images below the captions.<br><br>**3. Rapid Fire:** Question-and-answer timing, Google images, large ratings or answer labels, and a 4-second hook.<br><br>**4. Sync Reaction:** Original clip with synchronized doctor inset, then full-screen commentary.<br><br>**5. Async Reaction:** Full-screen source clip, then separate full-screen doctor commentary with supporting images/study excerpts below EDDIE captions. | Your recording; for Reaction, the original clip and your reaction recording |
| **EDDIE Carousel** | 1.0.0 | Original educational carousels filled into your own Canva template | Editable Canva template, topic and optional inspiration |
| **EDDIE Landscape** | 1.0.0 | 4K 16:9, stationary white outlined captions and clean speech cuts | Video, optional script |
| **EDDIE Sync Reaction** | 1.0.0 | Synced bottom-left reaction inset, captions, then full-screen commentary | Original clip, reaction recording and click sound |

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


## EDDIE Landscape 1.0.0

The approved V1 Revision 3 landscape treatment is available as **EDDIE Landscape**, alongside the existing styles. It uses 4K 16:9 presenter footage, stationary bold white lower-center captions with a black outline, and natural cuts that remove coughs, repeated takes and delays while preserving complete words. No graphics, images, music or click effects are added by default.

Users supply their own footage, optional script and output folder. Lower-resolution sources are upscaled for 4K delivery; exporting in 4K does not restore missing detail.

> Use EDDIE Landscape to edit my video in 4K 16:9. Use stationary bold white captions with a black outline at lower center. Remove coughs, repeated takes and long pauses, preserve every complete word and closing phrase, and deliver an MP4 plus SRT in my output folder.

```sh
python3 scripts/new_project.py my-landscape-video --style landscape
```

Invoke `eddie-landscape` in your agent, or load [.agents/skills/eddie-landscape/SKILL.md](.agents/skills/eddie-landscape/SKILL.md). Matching Claude instructions live in `.claude/skills/eddie-landscape/`; reusable defaults are in `presets/eddie-landscape.json`. The project starter creates a private brief and preset; the editing agent performs the edit using separately installed local video tools.


## EDDIE Sync Reaction 1.0.0

> Use EDDIE Sync Reaction with my original clip and separate reaction recording. Synchronize them, keep the original playing continuously, put me in the bottom-left corner with a click when I appear, and add the reaction captions. Then show my commentary full-screen, keeping natural laughter and removing recording setup, abandoned takes and long pauses. Save a new MP4 in my output folder.

```sh
python3 scripts/new_project.py my-reaction-video --style reaction
```

Use [.agents/skills/eddie-reaction/SKILL.md](.agents/skills/eddie-reaction/SKILL.md) for Codex or the matching `.claude/skills/eddie-reaction/SKILL.md` for Claude Code. Defaults are in `presets/eddie-reaction.json`. Each user provides their own recordings and click sound. The agent measures synchronization for each recording; the preset does not hardcode an example offset. Existing projects retain their copied settings.

## EDDIE Rapid Fire (Text hook, captions, images)

Rapid-fire questions and rankings with original audio, stationary Eddie captions, clear /10 scores, topic images beneath captions, and a rounded white hook with red emphasis for the first 4 seconds.

> Use EDDIE Rapid Fire to edit my recording. Add the hook directly below the captions for 0–4 seconds, highlight my selected phrase in red, and show one image per question below the captions. Keep my original audio.

Create a private project with `python3 scripts/new_project.py my-rapid-fire --style rapid-fire`. Read [.agents/skills/eddie-rapid-fire/SKILL.md](.agents/skills/eddie-rapid-fire/SKILL.md) for Codex or the matching `.claude/skills/eddie-rapid-fire/SKILL.md` for Claude. Defaults: [presets/eddie-rapid-fire.json](presets/eddie-rapid-fire.json).

## EDDIE MASTER EDITOR naming and optional messages

EDDIE MASTER EDITOR is the new name for EDDIE Classic. The `eddie` skill path and `presets/eddie.json` remain stable. Use `--style master`; legacy `--style classic` commands still work. Existing projects keep their copied settings.

Request iPhone messages or notifications on screen to enable the optional glass-message treatment: sender and timestamp, smooth upward entrance, notification sound, and optional blurred introduction followed by a readable reveal. Captions or a text hook alone do not enable it.

### Automatic Rapid Fire mode

EDDIE MASTER EDITOR detects repeated short questions, yes/no answers and rankings from your script or recording. It uses Eddie captions, a rounded white hook with selected red emphasis for the first **4 seconds**, larger /10 scores and Google topic images directly below captions. Supplied images and explicit style choices take priority. With a script alone it prepares the plan; footage or requested voice generation is needed to produce the video. AI interviewer and recorded nurse options are supported.

## Master Editor: five modes

1. **Captions + text hook** — no topic pictures.
2. **Captions + Google images + text hook** — supporting pictures below captions.
3. **Rapid Fire** — automatically selected for short Q&A/ranking scripts; hook, captions, Google images and large /10 scores.

4. **Sync Reaction** — original clip with synchronized presenter inset, followed by full-screen commentary.
5. **Async Reaction** — full-screen source excerpt, then separately recorded full-screen doctor commentary with optional supporting visuals below EDDIE captions.

The first three modes default to a **4-second hook**. All five use **200% audio gain**, applied once with peak protection. Sync and Async Reaction each use their own layout and an optional approved hook. Explicit user choices override defaults. iPhone message overlays remain optional.

### Shared subject framing

All five Master Editor modes inspect the footage before overlays. Direct-to-camera talking heads are centered when needed with a stable proportional crop, intact headroom and room for captions and images. Intentional side angles, interviews and reaction layouts remain intact. The reference top-hook composition is optional; the below-caption hook remains the default. Reframing preserves recorded gaze and does not synthesize eye contact.

### Sync and Async Reaction inside Master Editor

Master Editor includes both reaction styles:

- **EDDIE Sync Reaction:** source clip with synchronized bottom-left doctor inset, then full-screen commentary. The existing standalone `eddie-reaction` skill and `--style reaction` command remain compatible; the displayed name is now EDDIE Sync Reaction.
- **EDDIE Async Reaction:** full-screen source excerpt first, then separately recorded full-screen doctor commentary. Optional images or study excerpts sit below the original EDDIE captions. No synchronized inset is required. [Approved reference](https://www.instagram.com/reel/Dd46Pe2COyK/).

Say which format you want, or provide footage and a brief so Master Editor can choose. Existing approved edits retain their style. Both apply 200% audio gain once with peak protection. Script-only input produces a plan until footage is supplied.

```bash
python3 scripts/new_project.py my-sync-reaction --style sync-reaction
python3 scripts/new_project.py my-async-reaction --style async-reaction
```

Instructions: [Sync](.agents/skills/eddie/references/reaction-sync.md) · [Async](.agents/skills/eddie/references/reaction-async.md).
