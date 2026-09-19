# DWC AGENT EDDIE

**Reusable Digital White Coat video-editing styles.**

## Available styles

| Style | Version | Status |
| --- | --- | --- |
| **EDDIE Classic** | 1.0.0 | Available: neckline captions, your own images, and click-before-pop timing |
| **EDDIE Motion Graphics** | — | Planned; not included in this release |

Users provide **their own images**, video, and click audio. No image subscription, portrait library, or brand assets are bundled.

EDDIE Classic teaches an AI editing agent the DWC style: precise neckline captions, supplied pictures directly underneath, and a consistent click before each visual appears.

## The style

- Presenter stays on screen.
- Tight, natural edits that preserve meaning.
- Bold white captions with gold keyword emphasis at the base of the neck.
- Pictures sit closely below the captions, with a small visual gap.
- Supplied pictures and the supplied click sound are reused.
- Added graphics appear only when approved; no automatic intro or outro cards.

## What this repository contains

| File | Purpose |
| --- | --- |
| `.agents/skills/eddie/SKILL.md` | EDDIE skill for Codex |
| `.claude/skills/eddie/SKILL.md` | Matching Claude Code skill |
| `presets/eddie.json` | Editable layout and timing defaults |
| `scripts/new_project.py` | Create a private project folder with EDDIE settings |
| `AGENTS.md` / `CLAUDE.md` | Project instructions |

This is an **agent-guided skill starter**, not a standalone video editor or an automatic social publishing service. It needs an editing agent and locally installed video/transcription tools. Your private footage, brand pictures and click audio are supplied separately. No paid service is required by the skill itself.

## Start

1. Click **Code → Download ZIP** and extract it, or clone this repository:

   ```sh
   git clone https://github.com/hrmd20/dwc-agent-eddie.git
   cd dwc-agent-eddie
   ```
2. Open the folder in your editing agent.
3. Provide a video, the pictures to use, your click audio, and an output folder.
4. Say:

> Use EDDIE Classic to edit this talking-head video. Keep me visible, use my supplied pictures, place captions at the base of my neck, and tuck each picture closely below them. Use my click before each picture appears. Keep the voice clear. Start with a 10-second placement preview, then apply the approved layout to the full video.

A preview-only request stops at the preview. A request for a finished edit authorizes the agent to continue through ordinary editing and verification.

Create a local project with Python 3:

```sh
python3 scripts/new_project.py my-video
```

Store footage and exports inside the generated `projects/my-video/` directory. Those files stay out of Git by default. In agents that discover repository skills, invoke `eddie` or refer directly to its SKILL.md file.

## Requirements

- An editing agent that can read skill instructions and run local tools.
- Python 3.9+ for the project helper. It uses only the standard library.
- FFmpeg and FFprobe for inspecting and exporting video.
- A transcription engine that provides word timestamps, such as locally installed Whisper.
- A compositor supported by the agent, such as HyperFrames or Python/Pillow.
- Your source video, licensed pictures, and click sound.

Ask your agent to check these tools before starting. Missing dependencies must be installed separately; creating a project does not render a video.

## Editing tools

Use an available local video pipeline with FFmpeg/FFprobe, a word-timestamp transcription engine, and a compositor. An agent may use HyperFrames or deterministic graphics with FFmpeg. The skill specifies the output style; it does not bundle those tools.

For the broader editing toolkit, see [Nate Herk’s HyperFrames Student Kit](https://github.com/nateherkai/hyperframes-student-kit). Its installation guide covers the original toolkit and dependencies. You can use its editing tools alongside EDDIE, with the EDDIE style taking precedence for EDDIE projects.

## Updates and older styles

Keep this repository as the central source. Add future styles separately instead of replacing Classic. Publish numbered releases so users can download a stable version. Existing projects contain a copy of their preset: updating the repository must not silently change a project’s chosen style.

The current `presets/eddie.json` is the **EDDIE Classic v1** preset. EDDIE Motion Graphics will receive its own preset and instructions when created.

## Public sharing

Publish the skill, presets, helper scripts and documentation. Keep footage, exports, transcripts, credentials, client records and paid stock assets local. The supplied robot portrait and click sound are not bundled. Adding public demonstration media requires a separate intentional decision about those files.

## Credits

Built from the DWC editing workflow developed with Digital White Coat and informed by [Nate Herk’s HyperFrames Student Kit](https://github.com/nateherkai/hyperframes-student-kit). EDDIE’s compact neckline layout and restrained graphics are the DWC customization. This repository is not affiliated with or endorsed by Nate Herk, HeyGen, or HyperFrames.

The upstream MIT notice is preserved in `LICENSE`. Third-party tools and assets retain their own licenses. No AIS branding or upstream showcase videos are included.
