#!/usr/bin/env python3
"""Create a private local EDDIE project without copying user media."""
import argparse
import json
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('name', help='Project name using letters, digits and hyphens')
    parser.add_argument('--style', choices=('classic', 'motion'), default='classic',
                        help='Editing style; existing commands keep Classic')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.name):
        parser.error('Use lowercase letters, digits and hyphens, for example my-video.')
    root = Path(__file__).resolve().parents[1]
    project = root / 'projects' / args.name
    if project.exists():
        parser.error(f'Project already exists: {project}')
    preset_name = 'eddie-motion.json' if args.style == 'motion' else 'eddie.json'
    preset = json.loads((root / 'presets' / preset_name).read_text())
    project.mkdir(parents=True)
    for folder in ('assets', 'transcripts', 'renders', 'qa'):
        (project / folder).mkdir()
    (project / 'eddie.json').write_text(json.dumps(preset, indent=2) + '\n')
    (project / 'BRIEF.md').write_text(
        '# ' + args.name + '\n\n'
        'Style: ' + preset['name'] + '\n\n'
        'Record the source video path, click audio path, '
        'desired duration, approved graphics, and delivery destination here.\n\n'
        + ('Use motion graphics only; no picture overlays. ' if args.style == 'motion'
         else 'Record supplied image paths and preserve their proportions. ')
        + 'Calibrate captions to the neckline and visuals to the caption bounds. '
        'Keep the exact cut and asset timing when revising only placement.\n'
    )
    print(project)


if __name__ == '__main__':
    main()
