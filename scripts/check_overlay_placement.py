#!/usr/bin/env python3
"""Check actual overlay bounds against marked regions from sampled frames."""
import argparse
import json
import math
from pathlib import Path


def rectangle(value, label):
    if not isinstance(value, list) or len(value) != 4 or not all(
        isinstance(n, (int, float)) and math.isfinite(n) for n in value
    ):
        raise ValueError(f'{label} must be [left, top, right, bottom]')
    left, top, right, bottom = value
    if not 0 <= left < right <= 1 or not 0 <= top < bottom <= 1:
        raise ValueError(f'{label} must have positive area within the normalized canvas')
    return left, top, right, bottom


def intersects(first, second, gap):
    left, top, right, bottom = first
    a, b, c, d = second
    return left < c + gap and right > a - gap and top < d + gap and bottom > b - gap


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('layout', type=Path)
    args = parser.parse_args()
    try:
        layout = json.loads(args.layout.read_text())
        safe = rectangle(layout['safe'], 'safe')
        gap = layout.get('gap', .01)
        if not isinstance(gap, (int, float)) or not 0 <= gap <= 1:
            raise ValueError('gap must be between 0 and 1')
        if not layout['frames']:
            raise ValueError('At least one sampled frame is required')
        issues = []
        for frame in layout['frames']:
            stamp = frame['time']
            if not frame['overlays']:
                raise ValueError(f'{stamp}: sample must include at least one overlay')
            overlays = {name: rectangle(box, name) for name, box in frame['overlays'].items()}
            avoid = {name: rectangle(box, name) for name, box in frame['avoid'].items()}
            for name, box in overlays.items():
                if box[0] < safe[0] or box[1] < safe[1] or box[2] > safe[2] or box[3] > safe[3]:
                    issues.append(f'{stamp}: {name} extends outside the safe area')
                for obstacle, bounds in avoid.items():
                    if intersects(box, bounds, gap):
                        issues.append(f'{stamp}: {name} needs clearance from {obstacle}')
                for other, bounds in overlays.items():
                    if name < other and intersects(box, bounds, gap):
                        issues.append(f'{stamp}: {name} needs clearance from {other}')
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        parser.error(str(error))
    for issue in issues:
        print(issue)
    if not issues:
        print(f'Placement passed on {len(layout["frames"])} sampled frames.')
    return int(bool(issues))


if __name__ == '__main__':
    raise SystemExit(main())
