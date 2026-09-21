#!/usr/bin/env python3
"""Create a private local EDDIE project without copying user media."""
import argparse
import json
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('name', help='Project name using letters, digits and hyphens')
    parser.add_argument('--style', choices=('classic', 'motion', 'carousel'), default='classic',
                        help='Editing style; existing commands keep Classic')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.name):
        parser.error('Use lowercase letters, digits and hyphens, for example my-video.')
    root = Path(__file__).resolve().parents[1]
    project = root / 'projects' / args.name
    if project.exists():
        parser.error(f'Project already exists: {project}')
    preset_name = {'classic': 'eddie.json', 'motion': 'eddie-motion.json',
                   'carousel': 'eddie-carousel.json'}[args.style]
    preset = json.loads((root / 'presets' / preset_name).read_text())
    project.mkdir(parents=True)
    folders = ('sources', 'copy', 'exports', 'qa') if args.style == 'carousel' else ('assets', 'transcripts', 'renders', 'qa')
    for folder in folders:
        (project / folder).mkdir()
    (project / 'eddie.json').write_text(json.dumps(preset, indent=2) + '\n')
    if args.style == 'carousel':
        (project / 'BRIEF.md').write_text(
            '# ' + args.name + '\n\nStyle: EDDIE Carousel\n\n'
            'On first use, ask for your own editable Canva template link, a topic, '
            'audience and inspiration posts or accounts. Use only your connected Canva account.\n\n'
            'Record the template and working copy IDs, branding, tone, CTA, sources and '
            'delivery destination here. Preserve the template. No DWC templates are included.\n\n'
            'Daily monitoring is off until separately requested and configured with '
            'accounts, time, time zone and a supported scheduler. Save outputs as drafts for review.\n'
        )
        (project / 'sources' / 'ledger.json').write_text('[]\n')
        print(project)
        return
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
