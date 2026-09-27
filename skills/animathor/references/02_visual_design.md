# 02. Visual Design & Cinema Standards

A high-end educational animation looks intentional, clear, and cohesive. Every element on screen must compete for attention only when needed.

---

## 1. The 4-Tier Opacity Layering Hierarchy

Visual confusion occurs when all elements are drawn at 100% opacity. The human eye cannot determine what to look at first. Animathor enforces a 4-tier visual hierarchy:

| Tier | Opacity Range | Visual Elements | Examples |
|---|---|---|---|
| **Tier 1: Structural** | `0.15 - 0.35` | Coordinate axes, background grid planes, projection dashed lines, tick marks. | `NumberPlane(background_line_style={"stroke_opacity": 0.2})`, `DashedLine(stroke_opacity=0.3)` |
| **Tier 2: Contextual** | `0.45 - 0.70` | Reference boundaries, target profiles, historical ghost trails, inactive options. | Target square wave in Fourier analysis, faded previous curve versions. |
| **Tier 3: Primary** | `1.00` | The current active object being derived, animated, or transformed. | Main function plot, rotating vector, active equation term. |
| **Tier 4: Attention / Focus** | `1.00` + Vibrant Glow / Color | Anomaly indicators, overshoot peaks, Dirichlet points, measurement braces, callouts. | `Dot(color=ALERT, radius=0.12)`, `Brace(..., color=ACCENT)`, `Arrow(..., color=ALERT)` |

---

## 2. Typography & The Pango Kerning Guard

> **CRITICAL PITFALL**: Manim's Pango text renderer frequently causes letters to overlap or crash into each other when using proportional fonts (e.g. Arial, Times New Roman, Roboto).

### The Monospace Mandate
Always declare and use a system-compatible monospace font for all `Text()` mobjects:

```python
# Cross-platform monospace font constant
import platform

if platform.system() == "Windows":
    MONO = "Consolas"
elif platform.system() == "Darwin":
    MONO = "Menlo"
else:
    MONO = "DejaVu Sans Mono"

# Usage:
title = Text("Fourier Analysis", font=MONO, font_size=40, weight=BOLD)
```

### Font Size Hierarchy
| Role | Font Size (`font_size`) | Usage |
|---|---|---|
| **Title / Hook** | `42 - 48` | Opening question, scene title banner |
| **Section Header** | `32 - 36` | Subtitles, section indicators |
| **Body / Explanations** | `26 - 30` | Explanatory sentences, badges |
| **Annotations / Ticks** | `20 - 24` | Axis tick values, arrow labels, braces |
| **Subtitles / Safe Bar** | `18 - 22` | Bottom narration cards, captions |

---

## 3. Aspect Ratio & UI Safe Margins

### 3.1 Horizontal Format (16:9 — YouTube / Desktop)
- Resolution: $1920 \times 1080$ (Full HD)
- Frame dimensions: `frame_width = 14.22`, `frame_height = 8.0`
- Safe margin: Keep content at least `buff = 0.5` away from screen edges.

### 3.2 Vertical Format (9:16 — Shorts / Reels / TikTok)
Mobile video platforms place heavy UI elements (profile icon, like/comment buttons on the right, sound title and captions at the bottom, search/live at the top).

- Config settings:
  ```python
  config.pixel_width = 1080
  config.pixel_height = 1920
  config.frame_width = 9.0
  config.frame_height = 16.0
  ```
- **Top Safe Zone**: Header/Pill must be positioned at `UP * 6.8` to `UP * 7.2` (below the platform status bar).
- **Bottom Safe Zone**: Subtitle bar must be positioned between `DOWN * 5.8` and `DOWN * 6.5` (above the TikTok/Reels caption & sound title area).
- **Horizontal Width**: Central visuals should stay within `width <= 7.8` to prevent being covered by the right-hand interaction buttons.

---

## 4. Curated Color Palettes

### 4.1 Classic 3Blue1Brown Cinema (Default)
```python
BG = "#0B0F19"          # Deep Slate Midnight
PRIMARY = "#58C4DD"     # 3B1B Cyan-Blue
SECONDARY = "#83C167"   # 3B1B Sage Green
ACCENT = "#FACC15"      # Vibrant Yellow
ALERT = "#FF5964"       # Coral Red Anomaly
MUTED = "#64748B"       # Slate Grey
SURFACE = "#121726"     # Card Surface
BORDER = "#1E293B"      # Card Border
```

### 4.2 Cyberpunk / Tech
```python
BG = "#08080C"
PRIMARY = "#00F5FF"     # Neon Cyan
SECONDARY = "#39FF14"   # Electric Lime
ACCENT = "#FF007F"      # Hot Pink
ALERT = "#FF3131"       # Neon Red
MUTED = "#4A4E69"
```

### 4.3 Warm Academic
```python
BG = "#1A1A2E"
PRIMARY = "#E94560"     # Crimson
SECONDARY = "#F9A826"   # Warm Gold
ACCENT = "#16C79A"      # Mint Green
ALERT = "#FF4C60"
MUTED = "#7F8C8D"
```

---

## 5. The Spatial Anti-Collision & Focal Point Protection System

Visual collisions occur when text overlaps other text, or when annotations cover the visual focal point (the graph, curve, or derivation step). Animathor enforces strict spatial slots and collision prevention rules:

### 5.1 The 4 Non-Overlapping Canvas Slots

Divide the screen into clear vertical zones that never share mobjects:

```
┌────────────────────────────────────────────────────────┐
│ ZONE 1: HEADER & TITLE SLOT  (UP * 3.0 to UP * 3.5)    │
├────────────────────────────────────────────────────────┤
│                                                        │
│ ZONE 2: PRIMARY FOCAL POINT ZONE  ([-2.0, +2.0])       │
│ Graph / Geometry / Math Derivation. ZERO text here     │
│ except direct pointer arrows/callouts pointing IN.     │
│                                                        │
├────────────────────────────────────────────────────────┤
│ ZONE 3: ANNOTATION / FORMULA SLOTS (FLANK RIGHT/BELOW) │
│ .next_to(focal_point, RIGHT, buff=0.4) or DOWN         │
├────────────────────────────────────────────────────────┤
│ ZONE 4: SUBTITLE / CAPTION BAR  (DOWN * 3.0 to 3.4)    │
└────────────────────────────────────────────────────────┘
```

### 5.2 The "No Blind Stacking" Rule
NEVER animate a new text mobject into a slot where an existing text mobject resides without clearing the old one first:
- **Option A (Morphing)**: `self.play(ReplacementTransform(old_title, new_title))`
- **Option B (Fade Transition)**: `self.play(FadeOut(old_title)); self.play(FadeIn(new_title))`
- **Option C (Relative Stacking)**: `new_text.next_to(old_text, DOWN, buff=0.3)`

Calling `Write(title2.to_edge(UP))` while `title1.to_edge(UP)` is still on screen without `next_to` or `FadeOut` is a critical collision error.

### 5.3 Focal Point Clear-Radius
When pointing to a critical anomaly (e.g. Gibbs peak, tangent line, discontinuity):
- Arrows and callout text must point *at* the target with `buff=0.15` to `0.25`.
- Never place text directly over the dot, vertex, or intersection.

---

## 6. Clean Subtitles & Concise On-Screen Labeling

### 6.1 Zero Meta-Prefix Subtitles (Rule R-04)
AI script generators frequently leak markdown metadata and robotic prefixes into visual text cards. The following patterns are strictly **FORBIDDEN** in on-screen `Text()` or subtitles:
- **Banned**: `Text("Title: Fourier Analysis")` -> **Correct**: `Text("Fourier Analysis")`
- **Banned**: `Text("Subtitle: Explain how waves add up")` -> **Correct**: `Text("Harmonic Wave Addition")`
- **Banned**: `Text("Beat 1: In this scene we see...")` -> **Correct**: Use voiceover narration.
- **Banned Colon Chaining**: `Text("Fourier Series: explain sine waves...")` -> **Correct**: Concise standalone label.

### 6.2 Zero On-Screen Paragraphs (The 6-Word Ceiling)
The voiceover explains; the screen visualizes:
- **Maximum 6 words** for any on-screen text label, card, or annotation.
- **Never display a paragraph on screen**. If you write more than 8 words in a `Text()` call, you have committed an educational failure: viewers cannot read a paragraph and watch an animation at the same time.
- Move all explanatory sentences into the **Spoken Narration (voiceover)** track. The canvas should only hold:
  1. Mathematical notation (`MathTex`)
  2. Concise tags (`Overshoot: +8.95%`, `Fundamental Harmonic`, `Jump Discontinuity`)

