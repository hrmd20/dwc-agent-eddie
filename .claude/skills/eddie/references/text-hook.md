# Shared EDDIE Master Editor text hook

Approved 2026-10-29. Applies to all five Master Editor modes: captions + hook, captions + images + hook, Rapid Fire, Sync Reaction and Async Reaction. This replaces the older below-caption, 4-second hook. Honor explicit user overrides and preserve an existing approved edit unless a change is requested.

- Show from 0 seconds up to but not including 3 seconds; disappear cleanly at 3.000 seconds.
- Top-centered wide white rounded rectangle; bold black text with the user's selected phrase in bright red (#FF0000).
- Maximum TWO lines. Use more characters per line and natural phrase breaks before reducing font size. Preserve approved wording.
- Center the actual visible text horizontally and vertically inside the box, with EQUAL top and bottom padding. Do not use nominal font line-height as the visible text height: it causes excess white space beneath the last line.
- Render all colored runs on the SAME baseline. Measure the complete rendered text's nontransparent bounds, crop to those bounds, then center that text block in the background. Set box height to visible ink height plus twice the padding.
- Reference for a 1080×1920 canvas: top y=80, width about 960, center x=540, Arial Bold 58 px (reduce only to fit), line advance about 1.22× font size, 22 px equal vertical padding, corner radius 26. Scale proportionally for other resolutions. Box height is dynamic, never a fixed oversized rectangle.
- Maintain face/hair clearance and side margins. Inspect actual first-three-second footage, including motion and existing source text; adjust the top inset/type size if necessary, without moving below captions silently. If a materially different composition is required, show it in a preview.
- Leave existing speech captions and supporting images in their own zones. Hook-only revisions preserve audio, cut, captions and images; do not apply another 200% gain to an already edited video.
- Use the supplied hook. Otherwise propose an accurate hook from the actual recording, without inventing claims, ratings or credentials. Explicit requests for no hook override this default.

For placement approval, show the actual 2-second video frame with the proposed overlay. For batch work, label each frame with its video ID. After approval render the full video and inspect the first three seconds and the exit at 3 seconds. Keep originals intact.
