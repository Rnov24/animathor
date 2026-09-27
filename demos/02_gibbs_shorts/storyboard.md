# Gibbs Phenomenon in 60s

## 1. Mathematical Pre-Flight Audit (Accuracy & Theorem Verification)

Before drafting narration, verify all underlying mathematical facts:
- **Key Theorem / Core Concept**: Fourier Series and the Gibbs Phenomenon at jump discontinuities.
- **Exact Formulation**:
  $$S_N(x) = \frac{4}{\pi}\sum_{k=1,3,\dots}^N \frac{\sin(kx)}{k}$$
- **Critical Constants & Bounds**:
  $$\lim_{N \to \infty} S_N\left(\frac{\pi}{N}\right) = \frac{2}{\pi} \int_0^\pi \frac{\sin(t)}{t} dt \approx 1.17898 \implies +8.95\% \text{ overshoot}$$
- **Convergence Classification**: Pointwise convergence to midpoint $0$; non-uniform convergence on open intervals containing $0$.
- **Anti-Myth Checklist**: Overshoot energy concentrates into an infinitesimal needle as $N \to \infty$, but its peak amplitude never drops to zero.

---

## 2. Production & Narration Parameters

- **Video Format**: 9:16 Portrait Shorts (1080x1920)
- **Target Duration**: 60 seconds
- **Target Speech Cadence**: 130 - 140 words per minute (~2.1 - 2.3 words per second)
- **Total Word Budget**: Maximum 120 words
- **Safe Zone Buffers**:
  - Top: $Y \in [6.5, 7.5]$ for category pill and title
  - Center: $Y \in [-3.0, 4.5]$ for graphic axes and curves
  - Bottom: $Y \in [-7.0, -5.5]$ for clean subtitle card
- **Color Palette**:
  - `BG`: `#0B0F19` (Slate Dark Cinema)
  - `PRIMARY`: `#58C4DD` (Cyan-Blue 3B1B)
  - `SECONDARY`: `#83C167` (Sage Green 3B1B)
  - `ACCENT`: `#FACC15` (Vibrant Yellow)
  - `ALERT`: `#FF5964` (Coral Red)
  - `MUTED`: `#64748B` (Structural Slate Grey)

---

## 3. Two-Column Audio/Visual (AV) Script

| Beat & Duration | Visual Action & Mobjects (Manim) | Sync Trigger [Word] | Spoken Narration (Voiceover & WPM) | On-Screen Text / MathTex (<= 6 Words) |
|---|---|---|---|---|
| **Beat 1: The Hook**<br>00:00 - 00:10<br>*(10 sec)*<br>Budget: $\le 20$ words | - Pill `MATHEMATICS & SIGNALS` fades in at top<br>- Title `Gibbs Phenomenon` writes<br>- Dashed target square wave appears | On word: **"corner"** | *"Can smooth sine waves combine to form a sharp 90-degree corner?"*<br><br>*(11 words • 1.1 wps • [PASS])* | `pill`: MATHEMATICS & SIGNALS<br>`title`: Gibbs Phenomenon |
| **Beat 2: Summing Harmonics**<br>00:10 - 00:25<br>*(15 sec)*<br>Budget: $\le 30$ words | - Fundamental wave $N=1$ created<br>- Morphs into 19 harmonics curve<br>- Edge slope steepens rapidly | On word: **"harmonics"** | *"A Fourier series sums odd harmonics, steepening the slope toward a square wave."*<br><br>*(13 words • 0.87 wps • [PASS])* | `badge`: Harmonic N = 19<br>`math`: $N = 1 \to 19$ |
| **Beat 3: The Mystery Overshoot**<br>00:25 - 00:45<br>*(20 sec)*<br>Budget: $\le 40$ words | - Peak dot indicates first crest<br>- Badge reads `Overshoot ~8.95%`<br>- Subtitle card displays key insight<br>- 2.5s pause for visual retention | On word: **"vanishes"** | *"Yet near the edge, a spike of nearly 9 percent appears and never vanishes."*<br><br>*(14 words • 0.70 wps • [PASS])* | `alert`: Overshoot ~8.95%<br>`sub`: Overshoot never vanishes |
| **Beat 4: Resolution & Outro**<br>00:45 - 00:60<br>*(15 sec)*<br>Budget: $\le 30$ words | - Highlight jump midpoint convergence<br>- Elegant fade out across all scene elements | On word: **"Gibbs"** | *"This fundamental wave limit is known as Gibbs Phenomenon."*<br><br>*(9 words • 0.60 wps • [PASS])* | `title`: Gibbs Phenomenon |

---

## 4. Anti-Slop Quality & Accuracy Checklist

- [x] **Zero Em Dashes**: No em dash characters in narration, subtitles, or on-screen labels (Rule R-02).
- [x] **Zero Text Stacking (Zero Overlap)**: Every new text replaces old text using `ReplacementTransform` or `FadeOut`. No text elements overlap at identical coordinates or obscure graphic focal points.
- [x] **Zero On-Screen Paragraphs (<= 6 Words)**: On-screen text is strictly limited to concise labels or formulas. Full sentences belong exclusively in spoken voiceover (Rule R-03).
- [x] **Zero Meta-Prefixes**: No prefixes such as 'Title:', 'Subtitle:', 'Explanation:', or patterns like 'X: explain Y' on canvas text (Rule R-04).
- [x] **Zero AI Clichés**: Script is strictly free of marketing hype and rhetorical filler per guide 06.
- [x] **Speech Pacing Budget**: No narrative beat exceeds 2.3 words per second.
- [x] **Mathematical Accuracy**: Formal limit definitions, LaTeX notation, and convergence types are strictly verified.
- [x] **Breathing Room**: At least 1.5 to 2.5 seconds of silence (`self.wait(2.5)`) follows every key conceptual reveal.
- [x] **Explicit Sync Triggers**: Every visual transition is explicitly tied to a spoken trigger word.
