# Demo 02: Gibbs Phenomenon in 60s (Vertical 9:16 Shorts)

A fast-paced, high-retention 9:16 portrait video engineered specifically for YouTube Shorts, Instagram Reels, and TikTok.

## Architecture

```
02_gibbs_shorts/
├── animathor.json     # 1080x1920, 9:16, 60fps vertical configuration
├── manim.cfg          # Local canvas preset (9:16 portrait frame bounds)
├── storyboard.md      # Verified mathematical theorems & Two-Column AV table
├── script.py          # GibbsShortsScene with strict UI safe zones & 6-word ceiling
├── assets/            # Audio clips, reference SVGs, and diagram images
└── output/            # Rendered video clips and stitched final video
```

## UI Safe Zone Standard

This scene strictly adheres to the mobile vertical 9:16 canvas boundaries:
- **Top Zone ($Y \in [6.5, 7.5]$)**: Monospace category pill (`MATHEMATICS & SIGNALS`) + bold title. Clears system notifications and app header bars.
- **Center Focus ($Y \in [-3.0, 4.5]$)**: High-contrast coordinate axes, square wave target, and harmonic waveform animations.
- **Bottom Zone ($Y \in [-7.0, -5.5]$)**: Subtitle card placed comfortably above UI engagement buttons (like, share, comment).
- **Rule R-03 Compliant**: Subtitle card contains concise text ($\le 6$ words): `"The overshoot near the edge\nnever vanishes"`.

## Quickstart & Verification

1. **Audit Storyboard and Code**:
   ```powershell
   python ../../scripts/animathor_cli.py lint storyboard.md
   python ../../scripts/animathor_cli.py lint script.py
   ```

2. **Render Fast Draft (480p15)**:
   ```powershell
   python ../../scripts/animathor_cli.py draft script.py
   ```

3. **Preview a Single Frame**:
   ```powershell
   python ../../scripts/animathor_cli.py preview script.py GibbsShortsScene
   ```

4. **Production Master Render (1080x1920 60fps)**:
   ```powershell
   python ../../scripts/animathor_cli.py render script.py
   ```
