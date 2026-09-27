# Demo 01: Fourier Harmonic Decomposition

A complete 16:9 widescreen educational explainer demonstrating how orthogonal sine harmonics reconstruct a square wave, and revealing the persistent ~8.95% Gibbs overshoot.

## Architecture

```
01_fourier_explainer/
├── animathor.json     # 1920x1080, 16:9, 60fps ManimCE settings
├── manim.cfg          # Local canvas preset (Slate Midnight background #0B0F19)
├── storyboard.md      # Verified mathematical theorems & Two-Column AV table
├── script.py          # FourierExplainerScene implementing 5-tier visual hierarchy
├── assets/            # Audio clips, reference SVGs, and diagram images
└── output/            # Rendered video clips and stitched final video
```

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
   python ../../scripts/animathor_cli.py preview script.py FourierExplainerScene
   ```

4. **Production Master Render (1080p60)**:
   ```powershell
   python ../../scripts/animathor_cli.py render script.py
   ```
