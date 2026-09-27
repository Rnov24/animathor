# Fourier Harmonic Decomposition

## 1. Mathematical Pre-Flight Audit (Accuracy & Theorem Verification)

Before drafting narration, verify all underlying mathematical facts:
- **Key Theorem / Core Concept**: Fourier Series Theorem and Dirichlet Conditions for periodic waveforms.
- **Exact Formulation**:
  $$S_N(x) = \frac{4}{\pi}\sum_{k=1,3,\dots}^N \frac{\sin(kx)}{k}, \quad x \in [-\pi, \pi]$$
- **Critical Constants & Bounds**:
  $$\text{Gibbs overshoot limit} = \frac{1}{\pi}\int_0^\pi \frac{\sin(t)}{t}dt - \frac{1}{2} \approx 0.08949 \approx 8.95\%$$
- **Convergence Classification**: Pointwise convergence to the midpoint $f(0)=0$; non-uniform convergence near jump discontinuities.
- **Anti-Myth Checklist**: Increasing the number of harmonics does not eliminate overshoot; higher frequencies only compress the ripple width closer to the discontinuity.

---

## 2. Production & Narration Parameters

- **Video Format**: 16:9 Widescreen (1920x1080)
- **Target Duration**: 60 seconds
- **Target Speech Cadence**: 130 - 140 words per minute (~2.1 - 2.3 words per second)
- **Total Word Budget**: Maximum 120 words
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
| **Beat 1: The Hook**<br>00:00 - 00:10<br>*(10 sec)*<br>Budget: $\le 20$ words | - `title = Text("Fourier Harmonic Decomposition", font=MONO)` at top<br>- `axes = Axes(...)` drawn softly (opacity 0.4)<br>- `square_target = VGroup(...)` target step function drawn (opacity 0.6) | On word: **"corner"** | *"Can smooth sine waves combine to form a sharp 90-degree corner?"*<br><br>*(11 words • 1.1 wps • [PASS])* | `title`: Fourier Decomposition<br>`target`: $f(x) \in \{-1, 1\}$ |
| **Beat 2: Fundamental Wave**<br>00:10 - 00:22<br>*(12 sec)*<br>Budget: $\le 24$ words | - Formula $S_1(x) = \frac{4}{\pi}\sin(x)$ writes under axes<br>- Curve $N=1$ drawn smoothly with `Create(curve1)` | On word: **"fundamental"** | *"We start with a single fundamental sine wave matching the target period."*<br><br>*(12 words • 1.0 wps • [PASS])* | `eq`: $S_1(x) = \frac{4}{\pi}\sin(x)$ |
| **Beat 3: Higher Harmonics**<br>00:22 - 00:38<br>*(16 sec)*<br>Budget: $\le 32$ words | - Formula updates to $S_3(x)$ with `TransformMatchingTex`<br>- Curve morphs to include third harmonic<br>- Slope steepens toward square wave | On word: **"harmonics"** | *"Adding odd harmonics flattens the crest and steepens the slope toward vertical."*<br><br>*(12 words • 0.75 wps • [PASS])* | `eq`: $S_3(x) = \frac{4}{\pi}[\sin(x) + \frac{\sin(3x)}{3}]$ |
| **Beat 4: The Aha Moment**<br>00:38 - 00:52<br>*(14 sec)*<br>Budget: $\le 28$ words | - Dot highlights first peak<br>- Arrow indicates overshoot<br>- Label `+8.95% Overshoot` appears<br>- 2.5s pause for retention | On word: **"overshoot"** | *"Yet near the edge, an overshoot of roughly 8.95 percent remains permanent."*<br><br>*(12 words • 0.86 wps • [PASS])* | `alert`: +8.95% Overshoot |
| **Beat 5: Resolution & Clean Exit**<br>00:52 - 00:60<br>*(8 sec)*<br>Budget: $\le 16$ words | - Highlight Dirichlet jump average at $(0,0)$<br>- Elegant fade out across all elements | On word: **"Gibbs"** | *"This boundary behavior is Gibbs Phenomenon."*<br><br>*(6 words • 0.75 wps • [PASS])* | `title`: Gibbs Phenomenon |

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
