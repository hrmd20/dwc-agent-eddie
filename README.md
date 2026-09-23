# DWC AGENT EDDIE

**Five Digital White Coat content workflows: EDDIE Classic, Motion, Carousel, Landscape and Reaction.**

## Choose your style

| Style | Style version | Visual treatment | You provide |
| --- | --- | --- | --- |
| **EDDIE Classic** | 1.1.0 | Stationary white outlined captions; optional still-image pop-ups and click cues; no animations | Video, optional own images and click audio |
| **EDDIE Motion** | 1.0.0 | Animated typography, drawn connectors and explanatory diagrams; no image overlays | Video and click audio |
| **EDDIE Carousel** | 1.0.0 | Original educational carousels filled into your own Canva template | Editable Canva template, topic and optional inspiration |
| **EDDIE Landscape** | 1.0.0 | 4K 16:9, stationary white outlined captions and clean speech cuts | Video, optional script |
| **EDDIE Reaction** | 1.0.0 | Synced bottom-left reaction inset, captions, then full-screen commentary | Original clip, reaction recording and click sound |

Classic and Motion keep the presenter visible and place short captions at the base of the neck. Motion adds selective serif-italic keywords, gold highlights, staged diagram builds and dark/cream graphic cards. Graphics explain the actual script.

The latest repository adds **EDDIE Landscape 1.0.0** and **EDDIE Reaction 1.0.0** alongside Classic, Motion and Carousel. **EDDIE Classic 1.1.0** now uses the simplified Preview 3 treatment: stationary white outlined captions, optional still pictures that appear instantly, and optional click-before-image cues. No motion graphics or animations. Existing projects keep their copied settings until you request this update. [Classic-only v1.0.0](https://github.com/hrmd20/dwc-agent-eddie/releases/tag/v1.0.0) remains available.

## Download and start

1. Click **Code → Download ZIP** and extract it, or clone:

   ```sh
   git clone https://github.com/hrmd20/dwc-agent-eddie.git
   cd dwc-agent-eddie
   ```
2. Open the folder in your editing agent.
3. Choose your workflow. For videos, provide footage and an output folder; Motion and Reaction use your supplied click sound. Classic supports captions-only, or your own pictures with an optional click, and Reaction needs both the original clip and your reaction recording. For Carousel, share your own editable Canva template, topic and inspiration.
4. Use one of these prompts:

**EDDIE Classic**

> Use EDDIE Classic to edit this talking-head video. Keep me visible with stationary bold white captions outlined in black, just below my beard at the base of my neck. Use only my supplied pictures directly below the captions, appearing and disappearing instantly with no animation. If I provide and request a click, play it just before each picture. With no pictures, use captions only. Start with a 10-second placement preview.

**EDDIE Motion**

> Use EDDIE Motion to edit this talking-head video with motion graphics only. Keep me visible, place short captions at the base of my neck, and put animated text and diagrams immediately below them. Use white and gold type, selective italic emphasis, staged line drawing, and my click sound. Use no photos, screenshots or image overlays. Create a 20-second preview first.

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
python3 scripts/new_project.py my-classic-video --style classic
python3 scripts/new_project.py my-motion-video --style motion
python3 scripts/new_project.py my-carousel --style carousel
```

Omitting `--style` keeps the original Classic default. The helper copies the chosen preset into an ignored `projects/<name>/` folder. Video projects contain assets, transcripts, renders and QA; Carousel projects contain sources, copy, exports, QA and a private setup brief. It refuses to overwrite an existing project. Updating this repository does not silently change a project's copied preset.

## Included files

| Location | Purpose |
| --- | --- |
| `.agents/skills/eddie/` | EDDIE Classic skill and reference for Codex |
| `.agents/skills/eddie-motion/` | Self-contained EDDIE Motion skill for Codex |
| `.agents/skills/eddie-carousel/` | Self-contained Canva carousel workflow for Codex |
| `.claude/skills/` | Matching skills for Claude Code |
| `presets/eddie.json` | EDDIE Classic 1.1.0 defaults |
| `presets/eddie-motion.json` | EDDIE Motion defaults |
| `presets/eddie-carousel.json` | Carousel defaults; monitoring starts disabled |
| `scripts/new_project.py` | Private project starter with style selection |
| `AGENTS.md` / `CLAUDE.md` | Style routing and workspace instructions |

Invoke `eddie` for Classic, `eddie-motion` for Motion or `eddie-carousel` for Carousel in agents that discover repository skills. You can also point the agent directly to the relevant SKILL.md.

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

The agent should check tools before editing. No video style requires a paid service. Users supply source footage, sound and any licensed music; Classic users supply their own pictures if they want image pop-ups; click audio is optional for Classic.

For the broader toolkit, see [Nate Herk's HyperFrames Student Kit](https://github.com/nateherkai/hyperframes-student-kit). Its installation guide covers the original toolkit and dependencies; EDDIE's chosen style controls the resulting edit.

## Versions and sharing

Keep new styles separate and publish numbered releases. Preserve old presets and downloads so users can repeat an approved look. Classic, Motion and Carousel remain separate workflows.

Public files are reusable instructions, presets and helpers. Footage, exports, transcripts, private Canva links, account preferences, source notes, reference videos, paid stock, click audio and credentials stay local under ignored project directories. No robot portrait, stock subscription, audio file or private demonstration video is bundled.

## Credits

Built from the DWC editing workflow developed with Digital White Coat and informed by [Nate Herk's HyperFrames Student Kit](https://github.com/nateherkai/hyperframes-student-kit). EDDIE's neckline layout, Classic picture treatment and Motion graphic treatment are DWC customizations. This repository is not affiliated with or endorsed by Nate Herk, HeyGen, or HyperFrames.

The upstream MIT notice is preserved in `LICENSE`. Third-party tools and assets retain their own licenses. No AIS branding or upstream showcase videos are included.


## EDDIE Landscape 1.0.0

The approved V1 Revision 3 landscape treatment is available as **EDDIE Landscape**, alongside the existing styles. It uses 4K 16:9 presenter footage, stationary bold white lower-center captions with a black outline, and natural cuts that remove coughs, repeated takes and delays while preserving complete words. No graphics, images, music or click effects are added by default.

Users supply their own footage, optional script and output folder. Lower-resolution sources are upscaled for 4K delivery; exporting in 4K does not restore missing detail.

> Use EDDIE Landscape to edit my video in 4K 16:9. Use stationary bold white captions with a black outline at lower center. Remove coughs, repeated takes and long pauses, preserve every complete word and closing phrase, and deliver an MP4 plus SRT in my output folder.

```sh
python3 scripts/new_project.py my-landscape-video --style landscape
```

Invoke `eddie-landscape` in your agent, or load [.agents/skills/eddie-landscape/SKILL.md](.agents/skills/eddie-landscape/SKILL.md). Matching Claude instructions live in `.claude/skills/eddie-landscape/`; reusable defaults are in `presets/eddie-landscape.json`. The project starter creates a private brief and preset; the editing agent performs the edit using separately installed local video tools.


## EDDIE Reaction 1.0.0

> Use EDDIE Reaction with my original clip and separate reaction recording. Synchronize them, keep the original playing continuously, put me in the bottom-left corner with a click when I appear, and add the reaction captions. Then show my commentary full-screen, keeping natural laughter and removing recording setup, abandoned takes and long pauses. Save a new MP4 in my output folder.

```sh
python3 scripts/new_project.py my-reaction-video --style reaction
```

Use [.agents/skills/eddie-reaction/SKILL.md](.agents/skills/eddie-reaction/SKILL.md) for Codex or the matching `.claude/skills/eddie-reaction/SKILL.md` for Claude Code. Defaults are in `presets/eddie-reaction.json`. Each user provides their own recordings and click sound. The agent measures synchronization for each recording; the preset does not hardcode an example offset. Existing projects retain their copied settings.
