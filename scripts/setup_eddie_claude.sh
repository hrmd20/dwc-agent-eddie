#!/usr/bin/env bash
# One-time setup for EDDIE Claude: creates an ignored .venv in this repository
# with the Python tools the eddie_claude.py toolkit needs, and a bundled FFmpeg
# if none is installed. Run from the repository root:
#   bash scripts/setup_eddie_claude.sh            # core tools
#   bash scripts/setup_eddie_claude.sh --denoise  # also DeepFilterNet (large download, best noise removal)
set -euo pipefail
cd "$(dirname "$0")/.."

PY=${PYTHON:-python3}
if ! command -v "$PY" >/dev/null; then
  echo "Python 3 is required. On macOS install the Xcode Command Line Tools (xcode-select --install) or python.org Python." >&2
  exit 1
fi
"$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' || { echo "Python 3.9 or newer is required." >&2; exit 1; }

[ -d .venv ] || "$PY" -m venv .venv
.venv/bin/pip install --quiet --upgrade pip
.venv/bin/pip install --quiet -r .claude/skills/eddie-claude/requirements.txt
if [ "${1:-}" = "--denoise" ]; then
  .venv/bin/pip install --quiet deepfilternet torch torchaudio
fi

if command -v ffmpeg >/dev/null; then
  FF=$(command -v ffmpeg)
else
  FF=$(.venv/bin/python -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())')
fi

echo "EDDIE Claude is ready."
echo "  python: $(pwd)/.venv/bin/python"
echo "  ffmpeg: $FF"
echo "Run the toolkit with:"
echo "  FFMPEG=\"$FF\" .venv/bin/python .claude/skills/eddie-claude/scripts/eddie_claude.py -h"
.venv/bin/python -c 'import df' 2>/dev/null && echo "  DeepFilterNet noise removal: installed" \
  || echo "  DeepFilterNet noise removal: not installed (rerun with --denoise for the strongest cleanup; FFmpeg denoise is used otherwise)"
