# Animathor 🎬📐
### The Autonomous AI Animation Director for Manim (3Blue1Brown Standard)

[![GitHub Stars](https://img.shields.io/github/stars/Rnov24/animathor?style=flat-square)](https://github.com/Rnov24/animathor/stargazers)
[![skills.sh Compatible](https://img.shields.io/badge/skills.sh-Verified%20Skill-FACC15?style=flat-square)](https://skills.sh)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=flat-square)](https://www.python.org/)
[![Manim Community](https://img.shields.io/badge/Manim-Community%20Edition-58C4DD?style=flat-square)](https://www.manim.community/)
[![ManimGL 3B1B](https://img.shields.io/badge/ManimGL-3Blue1Brown-83C167?style=flat-square)](https://github.com/3b1b/manim)
[![Anti-Slop Certified](https://img.shields.io/badge/Anti--Slop-Rigorously%20Audited-FF5964?style=flat-square)](#-anti-slop--quality-manifesto)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

> Turn complex mathematical ideas into breathtaking, 3Blue1Brown-style educational animations with your AI assistant. Zero hallucinated equations, zero generic AI slop, and 100% mathematical rigor.

---

## 💡 Why Animathor?

If you have ever asked ChatGPT, Claude, or Copilot to write a Manim animation script, you probably hit these frustrating walls:
- **Broken LaTeX & Syntax Errors**: Outdated API calls that crash halfway through rendering.
- **Visual Chaos**: Overlapping formulas, text overflowing the canvas, and mobjects colliding.
- **Generic AI Narration**: Robotic scripts loaded with empty buzzwords (*"delve into"*, *"unlock the power"*, *"journey into"*) and artificial hype.
- **Zero Timing Sync**: Voiceover and visual animations drift apart after the first five seconds.

**Animathor fixes all of this.**

Animathor is an autonomous Agent Skill that transforms your AI coding agent (Claude Code, Cursor, Windsurf, Codex, Gemini CLI, Antigravity) into a **master mathematical animator and film director**. It enforces pedagogical clarity, mathematical verification, strict visual hierarchy, and production-tested Manim code before a single frame renders.

```
                    THE ANIMATHOR PRODUCTION PIPELINE
 ┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
 │ 1. PRE-FLIGHT AUDIT  │ ───► │ 2. AV STORYBOARD     │ ───► │ 3. DUAL-ENGINE CODE  │
 │ Verify theorems &    │      │ Two-column script    │      │ ManimCE & ManimGL    │
 │ equations beforehand │      │ audio/visual synced  │      │ conflict-free syntax │
 └──────────────────────┘      └──────────────────────┘      └──────────────────────┘
                                                                        │
                                                                        ▼
 ┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
 │ 6. MASTER ASSEMBLY   │ ◄─── │ 5. FAST DRAFT PREVIEW│ ◄─── │ 4. ANTI-SLOP LINT    │
 │ Lossless ffmpeg join │      │ 480p15 in seconds    │      │ Zero buzzwords, zero │
 │ into final.mp4       │      │ check keyframe freeze│      │ em dashes, safe-zone │
 └──────────────────────┘      └──────────────────────┘      └──────────────────────┘
```

---

## ⚡ Quickstart: Create Your First Animation in 3 Steps

### Step 1: Install the Skill

Animathor is fully compatible with the open [skills.sh](https://skills.sh) standard. Install it into your project with a single command:

```bash
# Add to current project (works with Claude Code, Cursor, Windsurf, Antigravity, etc.)
npx skills add Rnov24/animathor

# Or install globally so all your projects have access:
npx skills add Rnov24/animathor -g
```

*Prefer manual setup? Simply clone this repository into your workspace.*

---

### Step 2: Prompt Your AI Assistant

Once installed, simply ask your agent to create an animation. Here are realistic prompt examples you can copy and paste:

#### 🎬 Example A: YouTube Explainer (16:9 Landscape)
> *"Using @animathor, create a 16:9 explainer animation on how Fourier Series transforms a square wave into an infinite sum of harmonics. Focus on visual geometric intuition first before showing the integral formula."*

#### 📱 Example B: TikTok / Reels / Shorts (9:16 Portrait)
> *"Using @animathor, scaffold a 60-second 9:16 vertical short about the Monty Hall problem. Make sure all titles stay inside safe zones so TikTok UI overlays do not block them."*

#### 📐 Example C: Rigorous Academic Proof
> *"Using @animathor, visualize Euler's Identity e^(i*pi) + 1 = 0 using a unit circle in the complex plane, rotating vectors, and series expansion. Perform a mathematical pre-flight audit first."*

---

### Step 3: Preview & Render in Seconds

Your assistant scaffolds a dedicated project folder and writes a complete storyboard and Python script. You can inspect, preview, and render using the built-in CLI:

```bash
# 1. Fast draft render at 480p (renders in seconds for immediate review)
python scripts/animathor_cli.py draft my_project/script.py

# 2. Preview a single freeze frame as a PNG image
python scripts/animathor_cli.py preview my_project/script.py IntroScene

# 3. Final production render at crisp 1080p60
python scripts/animathor_cli.py render my_project/script.py

# 4. Lossless video stitching into output/final.mp4
python scripts/animathor_cli.py stitch my_project/script.py
```

---

## ✨ Core Features

| Feature | What It Does | Why Creators Love It |
|---|---|---|
| **Geometry Before Algebra** | Intuition $\to$ Visual Geometry $\to$ Formula $\to$ Aha Moment | Viewers grasp *why* a theorem works before drowning in algebraic manipulation. |
| **Mathematical Pre-Flight Audit** | Audits equations, boundary conditions, and domain assumptions | Prevents embarrassing formula hallucinations before writing code. |
| **Synchronized AV Scripting** | Two-column table binding spoken words to exact animation triggers | Animation and voiceover remain locked in perfect sync from start to finish. |
| **Dual-Engine Technical Mastery** | Full support for **Manim Community (CE)** and **ManimGL (3B1B)** | Switch between headless rendering pipelines and interactive GPU debugging without syntax headaches. |
| **Anti-Slop Quality Guard** | Automatic linter flagging robotic filler words and banned clichés | Your videos sound like genuine human educators, not generic AI sales pitches. |
| **Clean Project Scaffolding** | Generates self-contained project folders with local `manim.cfg` | No more messy project roots. Custom aspect ratios (16:9 vs 9:16) work automatically. |

---

## 📁 Standard Project Architecture

Every animation project created with Animathor follows a modular, predictable directory structure:

```
my_fourier_short/
├── animathor.json     # Project metadata (resolution, aspect ratio, fps, engine)
├── manim.cfg          # Local Manim config (auto-sets 16:9 or 9:16 canvas & dark theme)
├── storyboard.md      # Verified formulas + synchronized Two-Column AV script
├── script.py          # Modular, clean Python animation script
├── README.md          # Project notes and render instructions
├── assets/            # Project source media
│   ├── audio/         # Voiceover clips (.mp3, .wav), background music
│   ├── images/        # Diagrams, reference bitmaps (.png, .jpg)
│   └── svgs/          # Vector icons and custom curves (.svg)
└── output/            # Exported master video (final.mp4) and thumbnails
```

---

## 🛠️ CLI Toolkit Reference (`animathor_cli.py`)

Animathor includes an automation CLI so you never have to memorize obscure Manim and FFmpeg command flags:

```bash
# Scaffold a new project
python scripts/animathor_cli.py new <project_name> --horizontal --title "Linear Algebra Basics"
python scripts/animathor_cli.py new <project_name> --vertical   --title "Pythagoras in 60s"

# Audit storyboard or script against Anti-Slop & Accuracy guidelines
python scripts/animathor_cli.py lint <project_dir>/storyboard.md
python scripts/animathor_cli.py lint <project_dir>/script.py

# Rendering workflows
python scripts/animathor_cli.py draft   <project_dir>/script.py             # 480p15 fast draft
python scripts/animathor_cli.py preview <project_dir>/script.py SceneName   # Single PNG frame
python scripts/animathor_cli.py render  <project_dir>/script.py             # 1080p60 production

# Lossless video concatenation
python scripts/animathor_cli.py stitch  <project_dir>/script.py             # Joins scenes into output/final.mp4
```

---

## 🎨 Production Templates & Ready-to-Run Demos

Animathor ships with battle-tested template architectures in [templates/](file:///D:/Projects/animathor/templates/) and complete, ready-to-run demo projects in [demos/](file:///D:/Projects/animathor/demos/):

### 🌟 Complete Demos
- **[01_fourier_explainer](demos/01_fourier_explainer/)**: Complete 16:9 widescreen YouTube explainer on Fourier harmonic decomposition and Gibbs overshoot with verified AV script and scene code.
- **[02_gibbs_shorts](demos/02_gibbs_shorts/)**: High-retention 9:16 portrait video engineered for Shorts/Reels with top and bottom UI safe zone clearance and 6-word concise subtitles.
- **[03_product_rule_derivation](demos/03_product_rule_derivation/)**: Step-by-step calculus formula morphing using `TransformMatchingTex`, synchronized side notes, and attention highlighting.

### 📐 Template Architectures
1. **[Horizontal Explainer (16:9)](templates/horizontal_explainer_ce.py)**: Multi-scene YouTube format with HUD overlays, theorem cards, and graph transformations.
2. **[Vertical Short (9:16)](templates/vertical_shorts_ce.py)**: TikTok/Reels/Shorts format with UI safe margins, punchy pacing, and dynamic camera framing.
3. **[Step-by-Step Math Derivation](templates/math_derivation_ce.py)**: Rigorous formula morphing using `TransformMatchingTex`, color-coded variables, and bounding highlights.
4. **[Interactive GPU Scene (ManimGL)](templates/interactive_scene_gl.py)**: 3Blue1Brown OpenGL engine scene with real-time mouse interaction and `checkpoint_paste()` live coding.

---

## ⚡ Dual-Engine Rosetta Stone

Switch effortlessly between **Manim Community Edition** and **Grant Sanderson's ManimGL**:

| Action | Manim Community Edition (ManimCE) | ManimGL (3Blue1Brown) |
|---|---|---|
| **Installation** | `pip install manim` | `pip install manimgl` |
| **Import** | `from manim import *` | `from manimlib import *` |
| **CLI Render** | `manim -ql script.py Scene` | `manimgl script.py Scene -l` |
| **Interactive Mode** | `self.interactive_embed()` | `manimgl script.py Scene -se` / `checkpoint_paste()` |
| **Math Formula** | `MathTex(r"\int_a^b f(x)dx")` | `Tex(R"\int_a^b f(x)dx")` |
| **Coloring Substrings** | `formula.set_color_by_tex("x", BLUE)` | `Tex(..., t2c={"x": BLUE})` |
| **Creation Animation** | `self.play(Create(mob))` | `self.play(ShowCreation(mob))` |
| **Camera Movement** | `self.camera.frame.animate...` | `self.frame.animate...` |
| **Fixed HUD / Watermark** | `self.add_fixed_in_frame_mobjects(hud)` | `hud.fix_in_frame()` |
| **Clean Scene Exit** | `self.play(FadeOut(Group(*self.mobjects)))` | `self.play(FadeOut(Group(*self.mobjects)))` |

---

## 🚫 The Anti-Slop & Quality Manifesto

We believe educational animations should treat the viewer's time with respect. Animathor enforces these editorial standards:

1. **Zero Em Dashes**: Em dashes (Unicode U+2014) are completely banned in narration scripts and text cards. We use clean commas, colons, or simple periods.
2. **No AI Clichés**: Words like *delve, unlock, embark, journey, tapestry, game-changer, magical, mind-blowing, seamlessly, at its core* are strictly rejected.
3. **No Theatrical Filler**: We ban generic rhetorical openings (*"Have you ever wondered..."*, *"In today's video we will explore..."*). We open directly with an intriguing technical puzzle or visual paradox.
4. **Strict Speech Budget**: Narration is capped at $\le 2.3$ words/second (130 to 140 WPM).
5. **Mandatory Breathing Pauses**: Every major visual transition or theorem reveal includes a $1.5$s to $2.5$s pause (`self.wait(2.0)`) so the viewer can absorb the intuition.
6. **Zero Text Collisions & Focal Point Protection**: No blind text stacking. New text must use `ReplacementTransform` or `FadeOut` before occupying the same slot. Central graphs and equations are protected from overlapping labels.
7. **No Freak Subtitles or Meta-Prefixes (Rule R-04)**: Bans robotic labels like `"Title:"`, `"Subtitle:"`, `"Explanation:"`, and awkward colon formats like `"Topic: explain Topic..."`. Subtitles remain natural, clean, and direct.
8. **No On-Screen Paragraphs (Rule R-03: 6-Word Ceiling)**: Eliminates walls of text on the canvas. Spoken narration carries the explanation; on-screen text is strictly limited to $\le 6$ words for punchy badges, tags, and mathematical symbols.

---

## 🔧 Prerequisites & Toolchain Setup

To run Manim locally, ensure you have Python 3.10+, FFmpeg, and a LaTeX distribution:

### 1. Install System Dependencies

#### Windows
```powershell
# Using Winget:
winget install Gyan.FFmpeg
winget install MiKTeX.MiKTeX  # or TeXLive
```

#### macOS
```bash
# Using Homebrew:
brew install ffmpeg
brew install --cask mactex-no-gui
```

#### Ubuntu / Debian
```bash
sudo apt update
sudo apt install -y ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-science
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Your System
Run the built-in system diagnostics tool:
```bash
python scripts/check_health.py
```
This utility checks Python version, Manim installation, FFmpeg presence, and LaTeX compiler availability.

---

## 📖 Deep-Dive Reference Library

Need specific mathematical animation techniques? Explore the comprehensive reference guides in [skills/animathor/references/](file:///D:/Projects/animathor/skills/animathor/references/):

- **[01. Storyboarding & Pacing](skills/animathor/references/01_storyboarding.md)**: Narrative arcs, 3B1B visual hooks, and timing budgets.
- **[02. Spatial & Visual Design](skills/animathor/references/02_visual_design.md)**: Opacity hierarchy, kerning protection, and platform safe zones.
- **[03. Dual-Engine Rosetta Stone](skills/animathor/references/03_dual_engine_rosetta.md)**: Complete API cross-reference between ManimCE and ManimGL.
- **[04. Core Mathematical Patterns](skills/animathor/references/04_core_patterns.md)**: ValueTrackers, dynamic graphs, vector fields, and 3D scenes.
- **[05. Pipeline & Production Rendering](skills/animathor/references/05_pipeline_and_rendering.md)**: Quality settings, audio synchronization, and troubleshooting.
- **[06. Anti-Slop Scriptwriting](skills/animathor/references/06_anti_slop_scriptwriting.md)**: The mathematical pre-flight protocol and Two-Column AV script standard.

---

## 🤝 Contributing & Community

Contributions are warmly welcomed! Whether you want to add new animation patterns, improve the dual-engine rosetta stone, or enhance the CLI automation:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-pattern`).
3. Commit your changes (`git commit -m "feat: add 3D vector field flow pattern"`).
4. Push to the branch (`git push origin feature/amazing-pattern`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

Crafted with mathematical care for educators, researchers, and creators worldwide.
