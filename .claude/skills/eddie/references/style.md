# EDDIE Classic style specification

## Picture and framing

- Portrait 9:16, normally 1080×1920 at source-compatible frame rate (30 fps for the approved example).
- Talking-head footage remains visible; no full-screen replacement of the presenter.
- Preserve the approved cut, pacing, audio and image content during layout-only changes.
- Supplied images take priority. Preserve their aspect ratios and legibility.
- No opening “Your brand / Your AI editor” card, promotional closing cards, decorative diagrams or new animation by default.
- The approved DWC demonstration retains only “One Connected Workflow: Record → Cut → Clip → Upload.” This is project-specific, not a mandatory insert in every EDDIE edit.

## Caption and image geometry

Caption baseline placement follows the base of the neck/V-neck. Use the actual source, not a fixed pixel coordinate for every speaker. For the approved 1080×1920 demonstration, center the caption line around y=1150 and place the top of the image around y=1200. This leaves roughly 20 px below the visible caption glyphs. The user described the desired apparent gap as about 3 mm; physical millimeters vary by display and cannot be guaranteed in a video file.

Treat these coordinates as calibration starting points. Determine the visible caption bounding box including stroke; set image top to caption bottom plus a small gap (roughly 12–24 px at 1080-wide output). Scale coordinates proportionally with output size. Check that both the image bottom and caption fit; reduce an oversized image proportionally rather than clipping it. Do not cover the face. Avoid large empty space between caption and picture.

Bold white sans-serif captions, short groups of 1–3 words. Gold #E8C76B highlights for salient words only while spoken. Dark stroke for contrast. The approved example uses Arial Bold; select a locally available/licensed font rather than shipping a system font. Keep timing derived from the final edit’s words, not the uncut recording.

## Image behavior and audio

- Supplied click starts about two frames before a picture appears.
- Quick scale-in, approximately 87% to 100% over 160 ms; short alpha rise around 67 ms.
- Hold for the spoken concept; approximately 100 ms scale/fade exit.
- Keep existing picture timing when revising layout. Do not introduce unrelated images to meet an effects quota.
- Use the same supplied click for exits if that treatment was approved. A rapid replacement may use one shared cue to avoid doubled clicks.
- No other sound effects by default. Keep voice dominant over quiet music; preserve approved audio when possible.

## Review expectations

Inspect at full resolution and phone size: first seconds, every picture, the retained workflow graphic, the last phrase, and transitions. Captions and images must remain separated even on the longest caption. Check actual output rather than only a project preview or configuration. Keep source files, image permissions and private material out of public packages.
