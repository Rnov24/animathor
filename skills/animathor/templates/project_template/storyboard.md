# [Video Title]

## 1. Mathematical Pre-Flight Audit (Accuracy & Theorem Verification)

Before drafting narration, verify all underlying mathematical facts:
- **Key Theorem / Core Concept**: [e.g. Fourier Series Theorem and Dirichlet Conditions for periodic waveforms]
- **Exact Formulation**:
  $$\text{[Write formal equation with domain and index bounds, e.g. } S_N(x) = \frac{4}{\pi}\sum_{k=1,3,\dots}^N \frac{\sin(kx)}{k} \text{]}$$
- **Critical Constants & Bounds**: [e.g. Gibbs overshoot limit = $\frac{1}{\pi}\int_0^\pi \frac{\sin(t)}{t}dt - \frac{1}{2} \approx 0.08949 \approx 8.95\%$]
- **Convergence Classification**: [e.g. Pointwise convergence to jump average $f(0)=0$; non-uniform convergence near discontinuities]
- **Anti-Myth Checklist**: [e.g. Adding harmonics does not eliminate overshoot; increasing frequency only compresses ripples toward the jump]

---

## 2. Production & Narration Parameters

- **Video Format**: [16:9 Widescreen (1920x1080) OR 9:16 Portrait Shorts (1080x1920)]
- **Target Duration**: [e.g. 60 seconds]
- **Target Speech Cadence**: 130 - 140 words per minute (~2.1 - 2.3 words per second)
- **Total Word Budget**: Maximum [Target Duration x 2.0] words = [e.g. 120 words]
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
| **Beat 1: The Hook**<br>00:00 - 00:10<br>*(10 sec)*<br>Budget: $\le 20$ words | - `title = Text("Fourier Square Corner", font=MONO)` at top<br>- `axes = Axes(...)` drawn softly (opacity 0.3)<br>- `target = DashedLine(...)` target square wave appears (opacity 0.6) | On word: **"corner"** | *"Can smooth sine waves combine to form a sharp 90-degree corner?"*<br><br>*(11 words • 1.1 wps • [PASS])* | `title`: Fourier Square Corner<br>`target`: $f(x) \in \{-1, 1\}$ |
| **Beat 2: Harmonic Recipe**<br>00:10 - 00:25<br>*(15 sec)*<br>Budget: $\le 30$ words | - Formula for Fourier series $S_N(x)$ fades in<br>- Curve $N=1$ drawn via `Create(curve)`<br>- Progressively morphs to $N=3$, $N=7$, and $N=19$<br>- Slope of edge steepens toward vertical | On word: **"harmonics"** | *"A Fourier series sums odd harmonics: as frequencies rise, the slope steepens toward a square wave."*<br><br>*(16 words • 1.07 wps • [PASS])* | `eq`: $S_N(x) = \frac{4}{\pi}\sum_{k=1,3,\dots}^N \frac{\sin(kx)}{k}$<br>`badge`: $N = 1 \to 19$ |
| **Beat 3: The Aha Moment**<br>00:25 - 00:42<br>*(17 sec)*<br>Budget: $\le 34$ words | - Harmonic count elevated to $N=51$<br>- `peak_dot = Dot(color=ALERT)` marks first crest<br>- `brace = Brace(...)` measures overshoot of $+8.95\%$<br>- Visual pause of 2.5s for comprehension | On word: **"overshoot"** | *"Yet right at the jump, an overshoot of roughly 8.95 percent remains. No matter how many harmonics you add, this spike never vanishes."*<br><br>*(24 words • 1.41 wps • [PASS])* | `badge`: Persistent Overshoot<br>`math`: $+8.95\%$ |
| **Beat 4: Resolution & Outro**<br>00:42 - 00:55<br>*(13 sec)*<br>Budget: $\le 26$ words | - Highlight Dirichlet midpoint convergence at $(0,0)$<br>- Elegant fade out across all scene elements (*clean exit*) | On word: **"Gibbs"** | *"This is Gibbs Phenomenon: the mathematical boundary when continuous waves attempt to build a discontinuity."*<br><br>*(15 words • 1.15 wps • [PASS])* | `title`: Gibbs Phenomenon<br>`math`: $f(0) = 0$ |

---

## 4. Anti-Slop Quality & Accuracy Checklist

- [ ] **Zero Em Dashes**: No em dash characters in narration, subtitles, or on-screen labels (Rule R-02).
- [ ] **Zero Text Stacking (Zero Overlap)**: Every new text replaces old text using `ReplacementTransform` or `FadeOut`. No text elements overlap at identical coordinates or obscure graphic focal points.
- [ ] **Zero On-Screen Paragraphs (<= 6 Words)**: On-screen text is strictly limited to concise labels or formulas. Full sentences belong exclusively in spoken voiceover (Rule R-03).
- [ ] **Zero Meta-Prefixes**: No prefixes such as 'Title:', 'Subtitle:', 'Explanation:', or patterns like 'X: explain Y' on canvas text (Rule R-04).
- [ ] **Zero AI Clichés**: Script is strictly free of marketing hype and rhetorical filler per guide 06.
- [ ] **Speech Pacing Budget**: No narrative beat exceeds 2.3 words per second.
- [ ] **Mathematical Accuracy**: Formal limit definitions, LaTeX notation, and convergence types are strictly verified.
- [ ] **Breathing Room**: At least 1.5 to 2.5 seconds of silence (`self.wait(2.0)`) follows every key conceptual reveal.
- [ ] **Explicit Sync Triggers**: Every visual transition is explicitly tied to a spoken trigger word.
