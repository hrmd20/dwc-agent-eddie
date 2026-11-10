# Place Async Reaction hooks and captions

Lock the footage crop and cuts first. Sample the actual framed shot across the hook window (including the first and last active frames), each shot or zoom change, and the widest caption beat in each reaction shot. Sample extra frames when the subject moves near text. Use the target platform preview or safe-area guide to account for controls and cropped previews.

1. Mark the subject's hairline and face, embedded captions, and objects or gestures essential to the story. Use their positions across the sampled frames. Measure the entire rendered box, including padding or shadow.
2. For the hook, try immediately below embedded source captions when that space stays clear, as in the Hormozi cut. Otherwise try just above the hairline, as in the Jen cut. Use the largest readable two-line treatment that fits with a small visible gap. If neither position clears the shot, try a shorter hook, a smaller box or a shot with more room.
3. For reaction captions, start at the neckline, just below the beard. Use the widest beat to confirm clearance from the face and from essential props. Keep one fixed anchor through the reaction whenever possible. If a crop changes, check that anchor on both sides and adjust the crop or choose another shared anchor before rendering.
4. Check the actual export at phone size. Look for covered faces, text touching hair, competing captions, cropped shadows, and layout drift. Recheck the opening, longest caption, and transitions after corrections.

For a repeatable geometry check, save the measured overlay and obstacle rectangles in the private project's QA folder. Use normalized output coordinates `[left, top, right, bottom]` from 0 to 1. Set the safe rectangle from the intended viewing surface. The optional gap defaults to .01 of each axis. Include only active overlays and visible obstacles at each sampled timestamp.

```json
{
  "safe": [0.05, 0.05, 0.9, 0.82],
  "gap": 0.01,
  "frames": [
    {
      "time": "00:00.50",
      "overlays": {"hook": [0.12, 0.28, 0.84, 0.39]},
      "avoid": {"face": [0.35, 0.07, 0.62, 0.25], "source captions": [0.15, 0.42, 0.85, 0.47]}
    }
  ]
}
```

Run `python3 scripts/check_overlay_placement.py <layout.json>` from the repository root. It reports collisions and safe-area violations in the supplied measurements. Verify readability, movement between samples and platform UI clearance in the rendered preview.
