---
name: animathor
description: |
  Trigger when: (1) User wants to create an educational, mathematical, or scientific animation/explainer video, (2) User mentions "Manim", "ManimCE", "ManimGL", "3Blue1Brown", or "3b1b style", (3) User asks to plan, script, or storyboard animations (scenes.md, plan.md, storyboard), (4) User asks to generate math/geometry visualizations, algorithm walkthroughs, or YouTube/Shorts/TikTok/Reels content, (5) Code contains `from manim import *` or `from manimlib import *`.

  Animathor is the unified, next-generation Manim Animation Studio skill. It combines pedagogical storyboarding, cinematic visual design (opacity layering, safe margins, monospace kerning protection), dual-engine mastery (ManimCE & ManimGL Rosetta Stone), and automated rendering/stitching workflows into a single cohesive pipeline.
---

# Animathor — Unified Manim Animation Studio

Animathor elevates programmatic animation into **educational cinema**. Every frame teaches; every motion reveals geometric structure.

---

## 🧭 The 5-Phase Production Lifecycle

When prompted to create an animation, ALWAYS follow this 5-phase lifecycle:

```
[1. IDEATE & STORYBOARD] ➔ [2. SPATIAL & VISUAL DESIGN] ➔ [3. DUAL-ENGINE CODE] ➔ [4. FAST DRAFT PREVIEW] ➔ [5. FINAL RENDER & ASSEMBLY]
```

### Phase 1: Ideate & Storyboard (`storyboard.md`)
*Do not write animation code before establishing the pedagogical narrative.*
1. **Mathematical Pre-Flight Audit**: Explicitly verify all theorems, formal formulas, limits, and convergence properties. Dispel pop-science misconceptions.
2. **The Hook**: Frame an intriguing question or counterintuitive mystery.
3. **The "Aha Moment"**: Identify the pivotal visual insight where intuition clicks.
4. **Anti-Slop Voiceover & Pacing**:
   - Strictly no em dashes (`—`), no exclamation mark stuffing, and no AI buzzwords (*"delve", "unlock", "revolutionary"*).
   - Enforce the speech budget: $\le 2.3$ words/second (130-140 WPM).
5. **Output**: Generate a professional **Two-Column Audio/Visual (AV) Storyboard** binding visual triggers directly to spoken words. (See `references/01_storyboarding.md` and `references/06_anti_slop_scriptwriting.md`).

### Phase 2: Spatial & Visual Standards
1. **Aspect Ratio & Layout**:
   - **Horizontal (16:9)**: $1920 \times 1080$, `frame_width=14.22`, `frame_height=8.0`.
   - **Vertical (9:16 Shorts/Reels/TikTok)**: $1080 \times 1920$, `frame_width=9.0`, `frame_height=16.0`. Keep content inside safe margins (`buff >= 1.2` at top, `buff >= 1.5` at bottom to clear platform UI overlays).
2. **Opacity Layering Hierarchy**:
   - `0.15 - 0.35`: Structural elements (axes, grids, coordinate markers).
   - `0.50 - 0.70`: Contextual elements (reference boundaries, target profiles).
   - `1.00`: Primary focus (main animated curves, shapes, transforms).
   - `1.00 + Glow/Color`: Attention & Anomalies (peaks, braces, markers, alerts).
3. **Typography Standards (Pango Kerning Guard)**:
   - Always define `MONO = "Consolas"` (Windows) / `"Menlo"` (macOS) / `"DejaVu Sans Mono"` (Linux).
   - Never use proportional fonts for `Text()` in Manim without testing, as Pango frequently introduces overlapping letter bugs.
   - Use `MathTex(r"...")` (CE) or `Tex(R"...")` (GL) for all math and formulas.
4. **Pacing & Breathing Room**:
   - Add `self.wait(1.0)` to `self.wait(2.5)` after key reveals. Never immediately wipe the screen.

### Phase 3: Engine Selection & Modular Coding
Select the engine based on user requirements (defaults to **ManimCE**):
- **ManimCE** (`from manim import *`): Recommended for batch rendering, CI/CD, headless output, and modern plugin ecosystem.
- **ManimGL** (`from manimlib import *`): Recommended for real-time interactive development (`-se` flag, `checkpoint_paste()`) or custom GPU shaders.
- Refer to `references/03_dual_engine_rosetta.md` for exact syntax equivalents.

### Phase 4: Quality Linting, Fast Draft & Preview Verification
- **Run the Anti-Slop & Accuracy Linter**:
  ```powershell
  python scripts/animathor_cli.py lint storyboard.md
  python scripts/animathor_cli.py lint script.py
  ```
- **Never iterate at 1080p60**. Iterate at low resolution draft:
  ```powershell
  manim -ql script.py SceneName
  ```
- Or inspect a single freeze frame instantly:
  ```powershell
  manim -s -ql script.py SceneName
  ```

### Phase 5: Production Render & Stitching
- Render production quality:
  ```powershell
  manim -qh script.py Scene1 Scene2 Scene3
  ```
- Concatenate scene files using ffmpeg into `output/final.mp4` and add optional voiceover audio:
  ```powershell
  python scripts/animathor_cli.py stitch script.py
  ```

---

## 📁 Standard Project Directory Template

When creating a new animation project, ALWAYS follow or scaffold the standardized Animathor project directory structure:

```powershell
python scripts/animathor_cli.py new <project_name> [--vertical | --horizontal] [--title "Project Title"]
```

### Standard Layout:
```
<project_name>/
├── animathor.json     # Machine-readable metadata (resolution, aspect ratio, fps, engine)
├── manim.cfg          # Local Manim engine configuration (inherits resolution & background)
├── storyboard.md      # Mathematical Pre-Flight Audit & Two-Column AV Script
├── script.py          # Clean, modular Python animation script (or scenes/ if modular)
├── README.md          # Local project documentation and workflow instructions
├── assets/            # Project source assets
│   ├── audio/         # Voiceover recordings (.mp3), sound effects, audio tracks
│   ├── images/        # Bitmaps, reference diagrams, overlays (.png, .jpg)
│   └── svgs/          # Vector icons, custom curves (.svg)
└── output/            # Exported master video files (final.mp4) and promotional stills
```

### Directory Rules:
1. **No loose assets**: Store audio files in `assets/audio/`, images in `assets/images/`, and SVGs in `assets/svgs/`.
2. **`manim.cfg` as Local Engine Anchor**: The local `manim.cfg` sets the canvas dimensions, frame rate, and background theme, eliminating manual CLI flag repetition.
3. **Audit First**: Always run `python scripts/animathor_cli.py lint <project>/storyboard.md` before coding.
4. **Master Output**: Stitched master outputs and release videos must be placed in `output/final.mp4`.

---

## ⚡ Quick Reference: Dual-Engine Rosetta Stone

| Feature | Manim Community Edition (ManimCE) | ManimGL (3b1b) |
|---|---|---|
| **Import** | `from manim import *` | `from manimlib import *` |
| **CLI Render** | `manim -ql script.py Scene` | `manimgl script.py Scene -l` |
| **Interactive Mode** | `self.interactive_embed()` | `manimgl script.py Scene -se 20` |
| **Math Text** | `MathTex(r"\int_a^b f(x)dx")` | `Tex(R"\int_a^b f(x)dx")` |
| **Coloring Math** | `formula.set_color_by_tex("x", BLUE)` | `Tex(..., t2c={"x": BLUE})` |
| **Creation Animation** | `self.play(Create(mob))` | `self.play(ShowCreation(mob))` |
| **Camera Movement** | `self.play(self.camera.frame.animate.shift(...))` | `self.play(self.frame.animate.reorient(...))` |
| **Screen-Fixed HUD** | `self.add_fixed_in_frame_mobjects(hud)` | `hud.fix_in_frame()` |
| **Clean Scene Exit** | `self.play(FadeOut(Group(*self.mobjects)))` | `self.play(FadeOut(Group(*self.mobjects)))` |

---

## 📚 Reference Library Index

- [references/01_storyboarding.md](references/01_storyboarding.md): 3B1B narrative structures, hook formulas, and scene planning.
- [references/02_visual_design.md](references/02_visual_design.md): Opacity hierarchy, color palettes, kerning protection, and safe margins.
- [references/03_dual_engine_rosetta.md](references/03_dual_engine_rosetta.md): Exhaustive API comparison between ManimCE and ManimGL.
- [references/04_core_patterns.md](references/04_core_patterns.md): MathTex morphing, graphs, ValueTrackers, updaters, and 3D scenes.
- [references/05_pipeline_and_rendering.md](references/05_pipeline_and_rendering.md): CLI commands, ffmpeg concatenation, audio muxing, troubleshooting.
- [references/06_anti_slop_scriptwriting.md](references/06_anti_slop_scriptwriting.md): Mathematical accuracy audit, banned AI slop clichés, zero em dashes, and AV script format.

## 🛠️ Reusable Templates

Templates located in `templates/`:
- `templates/horizontal_explainer_ce.py`: 16:9 YouTube cinematic template.
- `templates/vertical_shorts_ce.py`: 9:16 Shorts/TikTok mobile template.
- `templates/math_derivation_ce.py`: Formula derivation with `TransformMatchingTex`.
- `templates/interactive_scene_gl.py`: ManimGL interactive scene.
- `templates/storyboard_template.md`: Scene storyboard spec markdown.
