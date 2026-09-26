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
