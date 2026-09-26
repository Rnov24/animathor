# Animathor: Unified Manim Animation Studio Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Adapt, consolidate, and elevate the 4 separate Manim skills (`manim-composer`, `manim-video`, `manimce-best-practices`, and `manimgl-best-practices`) into a unified, next-generation skill and production environment named **`animathor`** in the `d:\Projects\animathor` workspace.

**Architecture:** A comprehensive, single-source-of-truth skill (`animathor`) combining pre-production storyboarding, cinematic visual design standards, dual-engine technical references (ManimCE & ManimGL Rosetta Stone), production templates, and an automated CLI workflow runner.

**Tech Stack:** Manim Community Edition (ManimCE), ManimGL, Python 3.10+, LaTeX, ffmpeg, Agent Skills specification.

**Spec:** [animathor_implementation_plan.md](file:///C:/Users/Rnov24/.gemini/antigravity/brain/10b26e48-ff23-4731-a9d9-97ba0548ffa5/animathor_implementation_plan.md)

---

## Global Constraints
- Unified skill must be self-contained in `.agents/skills/animathor/` and accessible via `.claude/skills/animathor/`.
- Must seamlessly support both Manim Community Edition (primary) and ManimGL (secondary).
- Code templates must prevent Pango kerning overlap bugs using monospace font declarations (`Consolas`/`Menlo`).
- Opacity layering rules (0.15-0.35 structural, 0.5-0.7 contextual, 1.0 primary) must be standard across all templates.
- Support both 16:9 (Horizontal Widescreen) and 9:16 (Vertical Shorts/TikTok) formats with safe margin constraints.

---

## Task Decomposition

### Task 1: Environment & Project Scaffolding
**Files:**
- Create: `README.md`
- Create: `requirements.txt`
- Create: `environment.yml`
- Create: `.gitignore`

- [ ] **Step 1: Create requirements.txt and environment.yml**
Define dependencies: `manim>=0.18.0`, `numpy`, `scipy`, `edge-tts` (optional).
- [ ] **Step 2: Create .gitignore**
Ignore `media/`, `__pycache__/`, `*.aux`, `*.dvi`, `*.log`, `.venv/`.
- [ ] **Step 3: Create README.md**
Document the Animathor workspace, skill usage, and architecture.

---

### Task 2: Core Unified Skill Definition (`SKILL.md`)
**Files:**
- Create: `.agents/skills/animathor/SKILL.md`

- [ ] **Step 1: Write SKILL.md**
Craft rich YAML frontmatter triggers and the master 5-phase operational workflow:
1. Concept & Storyboard
2. Spatial Layout & Cinema Standards
3. Engine Selection & Coding
4. Fast Draft & Visual Verification
5. Final Render & Assembly

---

### Task 3: Unified Knowledge Base & Reference Guides
**Files:**
- Create: `.agents/skills/animathor/references/01_storyboarding.md`
- Create: `.agents/skills/animathor/references/02_visual_design.md`
- Create: `.agents/skills/animathor/references/03_dual_engine_rosetta.md`
- Create: `.agents/skills/animathor/references/04_core_patterns.md`
- Create: `.agents/skills/animathor/references/05_pipeline_and_rendering.md`

- [ ] **Step 1: Write 01_storyboarding.md**
Incorporate 3b1b pedagogy, hook, aha moment, pacing, and scenes breakdown.
- [ ] **Step 2: Write 02_visual_design.md**
Incorporate opacity layering, monospace typography standards, and vertical vs horizontal layout presets.
- [ ] **Step 3: Write 03_dual_engine_rosetta.md**
Comprehensive side-by-side comparison between ManimCE and ManimGL.
- [ ] **Step 4: Write 04_core_patterns.md**
Mobjects, MathTex morphing, Updaters/Trackers, and 3D scenes.
- [ ] **Step 5: Write 05_pipeline_and_rendering.md**
CLI flags, preview stills, ffmpeg concatenation, and audio muxing.

---

### Task 4: Production Templates
**Files:**
- Create: `.agents/skills/animathor/templates/horizontal_explainer_ce.py`
- Create: `.agents/skills/animathor/templates/vertical_shorts_ce.py`
- Create: `.agents/skills/animathor/templates/math_derivation_ce.py`
- Create: `.agents/skills/animathor/templates/interactive_scene_gl.py`
- Create: `.agents/skills/animathor/templates/storyboard_template.md`

- [ ] **Step 1: Write storyboard_template.md**
- [ ] **Step 2: Implement horizontal_explainer_ce.py**
- [ ] **Step 3: Implement vertical_shorts_ce.py**
- [ ] **Step 4: Implement math_derivation_ce.py**
- [ ] **Step 5: Implement interactive_scene_gl.py**

---

### Task 5: Automation Scripts & Tooling
**Files:**
- Create: `scripts/check_health.py`
- Create: `scripts/animathor_cli.py`

- [ ] **Step 1: Implement check_health.py**
Tests Python version, Manim installation, ffmpeg, and LaTeX binaries.
- [ ] **Step 2: Implement animathor_cli.py**
CLI commands: `new`, `draft`, `render`, `stitch`.

---

### Task 6: Cross-Platform Agent Mirroring & Verification
- [ ] **Step 1: Mirror or link `.agents/skills/animathor` to `.claude/skills/animathor`**
- [ ] **Step 2: Run Python compilation check on all python templates and scripts**
- [ ] **Step 3: Run health check script to verify local toolchain**
