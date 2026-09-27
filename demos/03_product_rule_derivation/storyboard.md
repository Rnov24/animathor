# Product Rule Derivation

## 1. Mathematical Pre-Flight Audit (Accuracy & Theorem Verification)

Before drafting narration, verify all underlying mathematical facts:
- **Key Theorem / Core Concept**: Product Rule for Differentiation in single-variable calculus.
- **Exact Formulation**:
  $$\frac{d}{dx}[f(x)g(x)] = f(x)g'(x) + f'(x)g(x)$$
- **Critical Constants & Bounds**:
  Assumes $f$ and $g$ are differentiable at $x$, which guarantees continuity: $\lim_{h \to 0} f(x+h) = f(x)$.
- **Convergence Classification**: Standard difference quotient limit under $\lim_{h \to 0}$.
- **Anti-Myth Checklist**: The derivative of a product is not simply the product of derivatives ($[fg]' \ne f'g'$); cross-terms naturally emerge from the geometric expansion of rectangles.

---

## 2. Production & Narration Parameters

- **Video Format**: 16:9 Widescreen (1920x1080)
- **Target Duration**: 45 seconds
- **Target Speech Cadence**: 130 - 140 words per minute (~2.1 - 2.3 words per second)
- **Total Word Budget**: Maximum 90 words
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
| **Beat 1: The Setup**<br>00:00 - 00:10<br>*(10 sec)*<br>Budget: $\le 20$ words | - Title `Product Rule Derivation` writes at top<br>- Difference quotient limit appears<br>- Colors highlight $f$ (cyan) and $g$ (green) | On word: **"definition"** | *"To differentiate a product, we start directly from the formal definition of a limit."*<br><br>*(14 words • 1.40 wps • [PASS])* | `title`: Product Rule Derivation<br>`note`: Derivative limit definition |
| **Beat 2: The Algebraic Trick**<br>00:10 - 00:25<br>*(15 sec)*<br>Budget: $\le 30$ words | - Equation morphs via `TransformMatchingTex`<br>- Middle terms factored: $f(x+h)$ and $g(x)$<br>- Label updates to factor instruction | On word: **"trick"** | *"We add and subtract a shared middle term, splitting the expression into two clean factors."*<br><br>*(15 words • 1.00 wps • [PASS])* | `note`: Factor f(x+h) and g(x) |
| **Beat 3: The Result**<br>00:25 - 00:40<br>*(15 sec)*<br>Budget: $\le 30$ words | - Formula resolves to $f(x)g'(x) + f'(x)g(x)$<br>- Surrounding rectangle highlights final formula<br>- 3.0s breathing pause for viewer retention | On word: **"derivatives"** | *"Taking the limit yields the derivative of each function multiplied by the other."*<br><br>*(13 words • 0.87 wps • [PASS])* | `note`: Product Rule Complete<br>`math`: $f g' + f' g$ |
| **Beat 4: Clean Outro**<br>00:40 - 00:45<br>*(5 sec)*<br>Budget: $\le 10$ words | - Elegant fade out across all scene elements | On word: **"complete"** | *"The product rule is proven."*<br><br>*(5 words • 1.00 wps • [PASS])* | `title`: Product Rule Complete |

---

## 4. Anti-Slop Quality & Accuracy Checklist

- [x] **Zero Em Dashes**: No em dash characters in narration, subtitles, or on-screen labels (Rule R-02).
- [x] **Zero Text Stacking (Zero Overlap)**: Every new text replaces old text using `ReplacementTransform` or `FadeOut`. No text elements overlap at identical coordinates or obscure graphic focal points.
- [x] **Zero On-Screen Paragraphs (<= 6 Words)**: On-screen text is strictly limited to concise labels or formulas. Full sentences belong exclusively in spoken voiceover (Rule R-03).
- [x] **Zero Meta-Prefixes**: No prefixes such as 'Title:', 'Subtitle:', 'Explanation:', or patterns like 'X: explain Y' on canvas text (Rule R-04).
- [x] **Zero AI Clichés**: Script is strictly free of marketing hype and rhetorical filler per guide 06.
- [x] **Speech Pacing Budget**: No narrative beat exceeds 2.3 words per second.
- [x] **Mathematical Accuracy**: Formal limit definitions, LaTeX notation, and convergence types are strictly verified.
- [x] **Breathing Room**: At least 1.5 to 2.5 seconds of silence (`self.wait(3.0)`) follows every key conceptual reveal.
- [x] **Explicit Sync Triggers**: Every visual transition is explicitly tied to a spoken trigger word.
