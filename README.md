# Animathor: Unified Manim Animation Studio 🎬📐

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Manim Community](https://img.shields.io/badge/Manim-Community%20Edition-58C4DD.svg)](https://www.manim.community/)
[![ManimGL 3B1B](https://img.shields.io/badge/ManimGL-3Blue1Brown-83C167.svg)](https://github.com/3b1b/manim)
[![Anti-Slop Certified](https://img.shields.io/badge/Anti--Slop-Certified-FF5964.svg)](#-anti-slop--mathematical-accuracy-standards)
[![skills.sh Compatible](https://img.shields.io/badge/skills.sh-Compatible-FACC15.svg)](#-installation)

Animathor is an autonomous AI agent skill and production studio for mathematical, algorithmic, and scientific animation videos. Built on top of **Manim Community Edition** and **ManimGL**, it transforms vague video concepts into **educational cinema** with mathematical rigor, cinematic visual design, and zero AI slop.

---

## 🌟 Key Pillars

1. **Pedagogical Storyboarding (3Blue1Brown Standard)**:
   - "Geometry before algebra" narrative arcs (Intuition $\to$ Geometry $\to$ Formula $\to$ Aha Moment).
   - High-precision **Two-Column Audio/Visual (AV) Script** binding spoken words directly to visual animation triggers.
2. **Anti-Slop & Mathematical Accuracy**:
   - Mandatory **Mathematical Pre-Flight Audit** verifying theorems, boundary limits, and convergence definitions.
   - Absolute ban on em dashes (`—`), exclamation mark stuffing, manufactured drama, and empty AI marketing buzzwords.
   - Speech budget constraints ($\le 2.3$ words/second, 130–140 WPM) with guaranteed breathing room pauses.
3. **Dual-Engine Technical Mastery**:
   - Complete **Rosetta Stone** cross-referencing API differences between **ManimCE** (`from manim import *`) and **ManimGL** (`from manimlib import *`).
4. **Standard Project Directory Template & Local `manim.cfg`**:
   - Fully segregated project structure (`assets/audio/`, `assets/images/`, `output/`).
   - Local `manim.cfg` auto-configures canvas dimensions (16:9 Landscape vs 9:16 Portrait) without repetitive CLI flags.
5. **Automated Tooling**:
   - Built-in CLI for project scaffolding, anti-slop linting, fast draft rendering (480p15), and lossless ffmpeg video concatenation.

---

## 📦 Installing from the `skills.sh` Marketplace

[skills.sh](https://skills.sh) is the open-source registry and package manager for AI Agent Skills, supporting Claude Code, Cursor, Windsurf, Codex, Gemini CLI, and Antigravity.

### 1. Install via Command Line (`npx skills`)
To install Animathor from the `skills.sh` ecosystem into your active project:

```bash
# Add to current project (auto-detects agent: Claude, Cursor, Antigravity, etc.)
npx skills add <username>/animathor

# Or install globally so all your projects have access:
npx skills add <username>/animathor -g

# Or target specific AI agents:
npx skills add <username>/animathor -a claude-code cursor

# Local testing without pushing to GitHub:
npx skills add ./skills/animathor
```

When run, `skills.sh`:
1. Identifies the agent environment (e.g. `.claude/skills/`, `.cursor/skills/`, `.agents/skills/`).
2. Installs the skill into the appropriate directory.
3. Automatically creates/updates `skills-lock.json` to lock the skill version and hash.

---

### 2. Install via VS Code Marketplace Extension
If you prefer a graphical interface in VS Code or Cursor:
1. Open VS Code / Cursor extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`).
2. Search for **"Agent Skills - Browse, Install & Manage"** (by skills.sh).
3. Search for **`animathor`** in the marketplace panel.
4. Click **Install** and select your desired agent and scope (project or global).

---

### 3. How to Publish / Index Animathor on `skills.sh`
`skills.sh` is decentralized: there is no manual approval form. Any public GitHub repository structured according to the Agent Skills specification is automatically indexed:
1. **Repository Structure**: This repository already places the skill inside `skills/animathor/SKILL.md` (the standard multi-skill layout expected by `skills.sh`).
2. **Push to Public GitHub**: Push this repository to a public GitHub repo (e.g. `https://github.com/<username>/animathor`).
3. **Add GitHub Topics**: In your GitHub repository settings, add the topics:
   - `agent-skills`
   - `skills`
   - `manim`
   - `mathematics`
   - `animation`
   - `3blue1brown`
4. **Instant Indexing**: Once pushed, users anywhere can run `npx skills add <username>/animathor`, and your skill will appear on [skills.sh](https://skills.sh).

---

### 4. Alternative Local & Offline Installers

Animathor includes a standalone installer script for Unix and Git Bash environments:

```bash
# 1. Install into the current project:
bash skill.sh install

# 2. Or install into a specific target project:
bash skill.sh install --project /path/to/my-video-project

# 3. Or install GLOBALLY for all agent sessions (~/.agents and ~/.claude):
bash skill.sh install --global

# 4. Check system toolchain health (Python, Manim, FFmpeg, LaTeX):
bash skill.sh check
```

**One-liner Remote Install**:
```bash
curl -fsSL https://raw.githubusercontent.com/<username>/animathor/main/skill.sh | bash
```

---

### Method 3: Install via `skill.ps1` (Windows PowerShell)

For native Windows users without Git Bash:

```powershell
# Install into the current project:
.\skill.ps1 install

# Install into a specific directory:
.\skill.ps1 install -Project D:\Projects\MyVideoProject

# Install GLOBALLY for all agent sessions:
.\skill.ps1 install -Global

# Run toolchain health check:
.\skill.ps1 check
```

---

## 🧭 The 5-Phase Production Lifecycle

When invoking `@animathor`, the agent strictly follows this 5-phase production lifecycle:

```
[1. IDEATE & STORYBOARD] ➔ [2. SPATIAL & VISUAL DESIGN] ➔ [3. DUAL-ENGINE CODE] ➔ [4. QUALITY LINT & DRAFT] ➔ [5. FINAL RENDER & ASSEMBLY]
```

### Phase 1: Ideate & Storyboard (`storyboard.md`)
1. **Mathematical Pre-Flight Audit**: Explicitly verify theorems, formulas, limits, and convergence definitions.
2. **The Hook & Aha Moment**: Frame an intriguing paradox; identify the pivotal visual breakthrough.
3. **Anti-Slop Speech Budget**: Enforce 130–140 WPM ($\le 2.3$ words/second). Strictly zero em dashes (`—`).
4. **Two-Column AV Table**: Produce a structured script binding every spoken word to an animation sync cue.

### Phase 2: Spatial & Visual Standards
- **Opacity Hierarchy**: Structural (`0.15 - 0.35`), Contextual (`0.50 - 0.70`), Primary (`1.00`), Attention (`1.00` + Glow).
- **Pango Kerning Guard**: Enforce monospace fonts (`Consolas`, `Menlo`, `DejaVu Sans Mono`) to prevent text overlap bugs.
- **Safe Zones**: Comply with platform UI overlays for 9:16 Shorts/Reels/TikTok (`buff >= 1.2` top, `buff >= 1.5` bottom).

### Phase 3: Dual-Engine Coding
Select the engine based on technical requirements (defaults to **ManimCE**):
- **ManimCE**: For headless rendering, CI/CD, and standalone productions.
- **ManimGL**: For interactive GPU exploration (`-se` breakpoint, `checkpoint_paste()`).

### Phase 4: Quality Lint & Fast Draft
- Audit against anti-slop rules: `python scripts/animathor_cli.py lint <project>/storyboard.md`.
- Preview freeze frame: `manim -s -ql script.py SceneName`.
- Draft low-res render: `manim -ql script.py SceneName`.

### Phase 5: Final Render & Assembly
- Production high-res render: `manim -qh script.py Scene1 Scene2 Scene3`.
- Lossless concatenation with ffmpeg into `output/final.mp4`.

---

## 📁 Standard Project Directory Template

Every animation project is structured using clean, self-contained directories:

```
my_fourier_short/
├── animathor.json     # Project metadata (resolution, aspect ratio, fps, engine)
├── manim.cfg          # Local Manim engine configuration (inherits resolution & background)
├── storyboard.md      # Mathematical Pre-Flight Audit & Two-Column AV Script
├── script.py          # Clean, modular Python animation script (or scenes/ if modular)
├── README.md          # Local project documentation and instructions
├── assets/            # Project source assets
│   ├── audio/         # Voiceovers (.mp3), sound effects, audio tracks
│   ├── images/        # Bitmaps, reference diagrams, overlays (.png, .jpg)
│   └── svgs/          # Vector icons, custom curves (.svg)
└── output/            # Exported master video files (final.mp4) and promotional stills
```

---

## 🛠️ CLI Quick Reference (`animathor_cli.py`)

The workspace includes a built-in automation CLI:

```powershell
# 1. Scaffold a 9:16 Vertical Short project:
python scripts/animathor_cli.py new fourier_shorts --vertical --title "Fenomena Gibbs"

# 2. Scaffold a 16:9 YouTube Widescreen project:
python scripts/animathor_cli.py new calculus_video --horizontal --title "Kalkulus Intuitif"

# 3. Audit a storyboard or Python script for anti-slop compliance:
python scripts/animathor_cli.py lint fourier_shorts/storyboard.md
python scripts/animathor_cli.py lint fourier_shorts/script.py

# 4. Fast draft render (480p15):
python scripts/animathor_cli.py draft fourier_shorts/script.py

# 5. Production high-res render (1080p60):
python scripts/animathor_cli.py render fourier_shorts/script.py

# 6. Lossless stitching with ffmpeg into output/final.mp4:
python scripts/animathor_cli.py stitch fourier_shorts/script.py
```

---

## ⚡ Dual-Engine Rosetta Stone

| Capability | Manim Community Edition (ManimCE) | ManimGL (3b1b) |
|---|---|---|
| **Package** | `pip install manim` | `pip install manimgl` |
| **Import** | `from manim import *` | `from manimlib import *` |
| **CLI Render** | `manim -ql script.py Scene` | `manimgl script.py Scene -l` |
| **Interactive Mode** | `self.interactive_embed()` | `manimgl script.py Scene -se [line]` / `checkpoint_paste()` |
| **Math Text** | `MathTex(r"\int_a^b f(x)dx")` | `Tex(R"\int_a^b f(x)dx")` |
| **Coloring Math** | `formula.set_color_by_tex("x", BLUE)` | `Tex(..., t2c={"x": BLUE})` |
| **Creation Animation** | `self.play(Create(mob))` | `self.play(ShowCreation(mob))` |
| **Camera Frame** | `self.camera.frame.animate...` | `self.frame.animate...` |
| **Fixed HUD Overlay** | `self.add_fixed_in_frame_mobjects(hud)` | `hud.fix_in_frame()` |
| **Clean Scene Exit** | `self.play(FadeOut(Group(*self.mobjects)))` | `self.play(FadeOut(Group(*self.mobjects)))` |

---

## 🚫 Anti-Slop & Mathematical Accuracy Standards

Animathor enforces strict editorial rules:

1. **Rule R-02 (Zero Em Dashes)**: Em dashes (`—`) are strictly banned in narration scripts and on-screen text. Use commas, colons, or periods.
2. **Banned AI Vocabulary**: Strictly forbids words like *delve, unlock, embark, journey, tapestry, game-changer, revolutionary, magical, mind-blowing, seamlessly, at its core, fundamentally*.
3. **No Theatrical Filler**: Replaces vague openers (*"Have you ever wondered..."*, *"In this video we will explore..."*) with direct, intriguing technical questions.
4. **Speech Word Budget**: Limits speech to $\le 2.3$ words/second (130–140 WPM).
5. **Breathing Room Pauses**: Requires $1.5$s to $2.5$s silence buffer after major visual reveals (`self.wait(2.0)`).

---

## 📚 Reference Library Catalog

Detailed documentation located in `skills/animathor/references/`:
- [01_storyboarding.md](skills/animathor/references/01_storyboarding.md): 3B1B narrative arcs, hook formulas, and pacing benchmarks.
- [02_visual_design.md](skills/animathor/references/02_visual_design.md): Opacity hierarchy, typography kerning protection, and safe margins.
- [03_dual_engine_rosetta.md](skills/animathor/references/03_dual_engine_rosetta.md): Comprehensive API comparison between ManimCE and ManimGL.
- [04_core_patterns.md](skills/animathor/references/04_core_patterns.md): MathTex morphing, graphs, ValueTrackers, updaters, and 3D scenes.
- [05_pipeline_and_rendering.md](skills/animathor/references/05_pipeline_and_rendering.md): Quality flags, ffmpeg concatenation, audio muxing, and troubleshooting.
- [06_anti_slop_scriptwriting.md](skills/animathor/references/06_anti_slop_scriptwriting.md): Mathematical accuracy audit, banned AI clichés, and two-column AV script format.

---

## 📄 License

MIT License. Designed with excellence for AI-assisted mathematical and technical animation.
