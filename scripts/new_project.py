#!/usr/bin/env python3
"""Create a private local EDDIE project without copying user media."""
import argparse
import json
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('name', help='Project name using letters, digits and hyphens')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.name):
        parser.error('Use lowercase letters, digits and hyphens, for example my-video.')
    root = Path(__file__).resolve().parents[1]
    project = root / 'projects' / args.name
    if project.exists():
        parser.error(f'Project already exists: {project}')
    preset = json.loads((root / 'presets' / 'eddie.json').read_text())
    project.mkdir(parents=True)
    for folder in ('assets', 'transcripts', 'renders', 'qa'):
        (project / folder).mkdir()
    (project / 'eddie.json').write_text(json.dumps(preset, indent=2) + '\n')
    (project / 'BRIEF.md').write_text(
        '# ' + args.name + '\n\n'
        'Record the source video path, supplied image paths, click audio path, '
        'desired duration, approved graphics, and delivery destination here.\n\n'
        'Calibrate captions to the neckline and images to the caption bounds. '
        'Keep the exact cut and asset timing when revising only placement.\n'
    )
    print(project)


if __name__ == '__main__':
    main()
