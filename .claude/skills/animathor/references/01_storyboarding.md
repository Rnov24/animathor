# 01. Storyboarding & Pedagogical Design

> *"The purpose of visualization is insight, not pictures." — Richard Hamming*

Effective educational animation is not about making equations fly around the screen; it is about building geometric intuition so that the mathematical formula feels inevitable.

---

## 1. The 3Blue1Brown Pedagogical Arc

Every great explainer follows a classic 4-stage narrative arc:

```
[1. THE HOOK] ➔ [2. THE GEOMETRIC INTUITION] ➔ [3. THE SYMBOLIC DERIVATION] ➔ [4. THE AHA MOMENT & RESOLUTION]
```

### 1.1 Stage 1: The Hook (0% - 15% duration)
- **Question the Given**: Pose a puzzle, paradox, or counterintuitive question.
  - *Example*: *"Can smooth, continuous sine waves make a sharp 90-degree square corner?"*
- **Acknowledge the Difficulty**: Validate why this is confusing or why the standard textbook explanation feels dry.
- **Set the Stakes**: Explain what becomes possible once this concept is mastered (e.g., JPEG compression, audio synthesis, quantum mechanics).

### 1.2 Stage 2: Geometric Intuition (15% - 45% duration)
- **Geometry Before Algebra**: Always show visual shapes, vectors, areas, or morphing curves before presenting the formal equation.
- **Physical Metaphor**: Ground abstractions in physical concepts (e.g., Fourier series as rotating epicycles, derivatives as velocity meters, eigenvectors as unmoved directions).
- **Progressive Disclosure**: Introduce one visual element at a time. Never show a fully populated coordinate plane with 10 labeled items all at once.

### 1.3 Stage 3: Symbolic Formulation (45% - 75% duration)
- **Equation as Description**: Introduce equations only after the visual pattern is clear. The equation should feel like a shorthand summary of what the viewer has already witnessed visually.
- **Color-Coded Math**: Every variable in an equation must match the color of its geometric counterpart on screen (e.g., if radius $r$ is yellow in the formula, the circle's radius vector must be yellow).
- **Morphing Transformations**: Use `ReplacementTransform` or `TransformMatchingTex` to show how terms simplify or balance out.

### 1.4 Stage 4: The "Aha Moment" & Resolution (75% - 100% duration)
- **The Payoff**: Demonstrate the breakthrough where the initial paradox is resolved (e.g., Gibbs overshoot $\approx 8.95\%$ persisting at infinity, proving why ringing artifacts exist).
- **Breathing Room**: Add a 2.5s to 3.0s pause (`self.wait(2.5)`) right after the key insight is revealed. Let the viewer absorb the elegance before wiping the screen.
- **Real-World Connection**: Close with a tangible application.

---

## 2. Storyboard Decomposition Spec (`storyboard.md`)

When planning an animation, always begin with a **Mathematical Pre-Flight Audit** and format the script using the professional **Two-Column Audio/Visual (AV) Table**. See `references/06_anti_slop_scriptwriting.md` for exhaustive anti-slop guidelines.

### 2.1 Mathematical Pre-Flight Audit
1. **Theorems & Formulas**: State the exact theorem, valid index ranges, and formal LaTeX equation.
2. **Convergence & Boundary Cases**: Verify whether convergence is pointwise or uniform, and check behavior at $x=0$, $x \to \infty$.
3. **Exact Constants**: Confirm all analytical values (e.g. Gibbs constant $\approx 8.95\%$) before scripting.

### 2.2 The Two-Column AV Script Table

Organize the scene-by-scene script into an AV table that binds visual cues to spoken words:

| Beat & Timecode | Visual Action & Mobjects (Manim) | Sync Cue [Word] | Spoken Narration (Voiceover) | Subtitle / MathTex |
|---|---|---|---|---|
| **Beat 1**<br>00:00 - 00:10<br>*(10 sec)* | Draw coordinate axes and square target. | On word: **"corner"** | *"Can smooth, continuous sine waves make a sharp 90-degree corner?"*<br><br>*(11 words • 1.1 wps)* | **Title**: Fourier Analysis<br><br>**Subtitle**: Can smooth waves make a sharp corner? |
| **Beat 2**<br>00:10 - 00:25<br>*(15 sec)* | Progressive addition of odd harmonics $N=1, 3, 7, 19$. | On word: **"steeper"** | *"Fourier series add odd harmonics one by one. As frequencies rise, the slope gets steeper."*<br><br>*(15 words • 1.0 wps)* | **Math**: $S_N(x) = \frac{4}{\pi}\sum \frac{\sin(kx)}{k}$<br><br>**Badge**: $N = 1 \to 19$ |

---

## 3. Pacing Benchmarks

Use these timing guidelines to ensure natural educational rhythm:

| Event Type | Animation `run_time` | `self.wait()` After | Total Beat |
|---|---|---|---|
| Scene Title / Question Reveal | 1.2s - 1.5s | 1.0s | ~2.5s |
| Basic Shape / Axis Creation | 1.0s - 1.5s | 0.5s | ~2.0s |
| Key Formula Reveal | 1.5s - 2.0s | 2.0s | ~4.0s |
| Complex Morph / Transform | 1.5s - 2.0s | 1.0s | ~3.0s |
| Subtitle / Label Update | 0.6s - 0.8s | 0.5s | ~1.3s |
| **"Aha Moment" Peak Reveal** | **2.0s - 2.5s** | **2.5s - 3.5s** | **~5.5s** |
| Scene FadeOut / Clean Exit | 0.5s - 0.8s | 0.3s | ~1.0s |
