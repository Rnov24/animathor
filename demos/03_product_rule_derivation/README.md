# Demo 03: Calculus Product Rule Derivation

A formula-morphing mathematical derivation illustrating the algebraic proof of the product rule for differentiation using Manim's `TransformMatchingTex`.

## Architecture

```
03_product_rule_derivation/
├── animathor.json     # 1920x1080, 16:9, 60fps ManimCE settings
├── manim.cfg          # Local canvas preset (Slate Midnight background #0B0F19)
├── storyboard.md      # Mathematical pre-flight audit & Two-Column AV table
├── script.py          # MathDerivationScene with formula morphing & note syncing
├── assets/            # Audio clips, reference SVGs, and diagram images
└── output/            # Rendered video clips and stitched final video
```

## Mathematical Features Demonstrated

1. **Limit Definition**: Formal introduction of the difference quotient for $[f(x)g(x)]'$.
2. **Algebraic Add-and-Subtract**: Visual splitting of the numerator using $+f(x+h)g(x) - f(x+h)g(x)$.
3. **TeX Matching & Morphing**: Seamless transformation between intermediate algebraic steps without jarring cuts (`TransformMatchingTex`).
4. **Surrounding Highlighting**: Visual framing of the final result using `SurroundingRectangle`.

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
   python ../../scripts/animathor_cli.py preview script.py MathDerivationScene
   ```

4. **Production Master Render (1080p60)**:
   ```powershell
   python ../../scripts/animathor_cli.py render script.py
   ```
