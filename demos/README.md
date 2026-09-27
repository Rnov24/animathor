# Animathor Demos

This directory contains three complete, production-ready demo projects based on Animathor's core archetypes and templates:

1. **[01_fourier_explainer](./01_fourier_explainer/)**:
   - **Archetype**: Horizontal 16:9 Explainer (YouTube Widescreen)
   - **Topic**: Fourier Harmonic Decomposition & Gibbs Phenomenon
   - **Highlights**: 5-tier visual hierarchy, subtle structural grids, harmonic plotting, and alert badges.

2. **[02_gibbs_shorts](./02_gibbs_shorts/)**:
   - **Archetype**: Vertical 9:16 Portrait (Shorts / Reels / TikTok)
   - **Topic**: Gibbs Phenomenon in 60 seconds
   - **Highlights**: Mobile safe zone layout (category pill, central focus, bottom subtitle card with Rule R-03 compliance).

3. **[03_product_rule_derivation](./03_product_rule_derivation/)**:
   - **Archetype**: Mathematical Derivation & Formula Morphing
   - **Topic**: Single-Variable Calculus Product Rule
   - **Highlights**: Dynamic equation transitions using `TransformMatchingTex`, synchronized explanatory notes, and attention highlighting.

---

## Running the Anti-Slop & Accuracy Linter

Each demo has been audited and certified at **100% PASS** under Animathor's Anti-Slop, Accuracy, and Pacing standards.

Run the linter across all demo storyboards and scripts:

```powershell
# Audit Storyboards
python scripts/validate_script.py demos/01_fourier_explainer/storyboard.md
python scripts/validate_script.py demos/02_gibbs_shorts/storyboard.md
python scripts/validate_script.py demos/03_product_rule_derivation/storyboard.md

# Audit Manim Code
python scripts/validate_script.py demos/01_fourier_explainer/script.py
python scripts/validate_script.py demos/02_gibbs_shorts/script.py
python scripts/validate_script.py demos/03_product_rule_derivation/script.py
```

---

## Rendering Demos

Render low-resolution drafts or production releases directly with the `animathor_cli.py` utility:

```powershell
# Fast 480p15 drafts (renders in seconds)
python scripts/animathor_cli.py draft demos/01_fourier_explainer/script.py
python scripts/animathor_cli.py draft demos/02_gibbs_shorts/script.py
python scripts/animathor_cli.py draft demos/03_product_rule_derivation/script.py

# High-fidelity 1080p60 production renders
python scripts/animathor_cli.py render demos/01_fourier_explainer/script.py
python scripts/animathor_cli.py render demos/02_gibbs_shorts/script.py
python scripts/animathor_cli.py render demos/03_product_rule_derivation/script.py
```
