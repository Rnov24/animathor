# 06. Anti-Slop Scriptwriting & Mathematical Accuracy

> *"Elegance is not a luxury; it is the natural consequence of mathematical truth spoken plainly."*

This guide sets the non-negotiable editorial and scientific standards for writing animation scripts, storyboards, voiceover narration, and on-screen text in Animathor. Its goal is simple: **eliminate generic AI slop, guarantee mathematical accuracy, and deliver genuine pedagogical insight.**

---

## 1. The Mathematical Accuracy Gate (Proof-First Mandate)

Before writing a single sentence of narration or planning an animation beat, you must perform a **Mathematical Pre-Flight Audit**:

1. **Formal Definitions**:
   - Never replace a precise mathematical definition with hand-waving pop-science unless you immediately clarify the boundary.
   - Example: Do not say *"Fourier series turns any wave into smooth circles"*. Say: *"A Fourier series decomposes any periodic function satisfying the Dirichlet conditions into a sum of sinusoidal harmonics."*
2. **Explicit Convergence Types**:
   - Be scrupulously accurate regarding convergence. Distinguish between *pointwise convergence*, *uniform convergence*, and *mean-square convergence ($L^2$)*.
   - Example in Gibbs Phenomenon: State clearly that the Fourier series of a square wave converges *pointwise* to $(f(x^+) + f(x^-))/2$ at jump discontinuities, but does **not** converge *uniformly*, which is why the ~8.95% overshoot persists.
3. **Exact Constants and Limits**:
   - Double-check all analytical constants.
   - Gibbs overshoot constant: $\frac{1}{\pi} \int_0^\pi \frac{\sin(t)}{t} dt - \frac{1}{2} \approx 0.08948987... \approx 8.95\%$.
   - Never round numbers casually without indicating approximation ($\approx$).
4. **Domain Boundaries & Edge Cases**:
   - Always state the valid domain for equations (e.g., $x \in [-\pi, \pi]$, $n \ge 1$, $k \text{ odd}$).
   - Test extreme values ($x=0$, $x \to \infty$, $N \to \infty$) to ensure the visual animation matches mathematical reality.

---

## 2. The Banned AI Slop Lexicon & Clichés

AI writing models default to predictable rhetorical filler, false enthusiasm, and theatrical padding. In Animathor scripts, these patterns are strictly **FORBIDDEN**.

### 2.1 Banned Vocabulary & Phrases
Replace these hollow markers with concrete mathematical statements:

| Banned AI Slop | Why It Fails | What to Say Instead |
|---|---|---|
| *"Delve into / Dive deep"* | Cliche AI transition. | State the topic directly: *"We examine..."* or *"Let us trace..."* |
| *"Unlock the power of / Unlock the secret"* | Corporate marketing hype. | State the utility: *"This formula allows us to compute..."* |
| *"Imagine a world where..."* | Fictional theatricality. | Frame a concrete problem: *"Suppose we want to construct..."* |
| *"Have you ever wondered..."* | Stale rhetorical opener. | Pose the technical question: *"Can smooth functions produce a 90-degree corner?"* |
| *"Mind-blowing / Fascinating / Magical"* | Telling the viewer how to feel instead of showing beauty. | Show the geometric surprise: let the viewer experience the insight. |
| *"At its core / Fundamentally / The heart of the matter"* | Significance inflation. | State the core theorem or mechanism directly. |
| *"Revolutionary / Game-changer / Next-level"* | Empty tech buzzwords. | Cite the historical or engineering consequence (e.g. JPEG compression, MRI imaging). |
| *"Without further ado / In this video we will..."* | Meta-commentary padding. | Cut the meta-commentary; begin directly with the hook. |
| *"Tapestry / Symphony / Dance of equations"* | Pretentious poetic fluff. | Describe the physical or geometric operation (e.g. vector sum, phase rotation). |

### 2.2 Punctuation & Rhetorical Rules
- **Rule R-02 (Zero Em Dashes)**:
  - The em dash character (`—`) is strictly forbidden in narration scripts, on-screen subtitles, and visual text cards.
  - Use a period, a comma, a colon, or separate sentences instead.
- **No Exclamation Stuffing (`!`)**:
  - Technical cinema conveys authority through calm clarity. Limit exclamation marks to zero or at most one in an entire 60-second video.
- **No Manufactured Staccato Drama**:
  - Avoid runs of 2-3 word sentences: *"No rules. No limits. Just math."* Write complete, well-formed sentences with rhythmic cadence.
- **No Forced Rule of Three**:
  - Do not force lists into trios (*"simple, elegant, and powerful"*). List only the properties that are mathematically relevant.

---

## 3. Narration Pacing & The Speech Budget

The number one cause of rushed, unwatchable explainer videos is **too many words packed into too few seconds**.

### 3.1 The Speed Benchmark
- **Conversational Explainer Speed**: **130 to 140 words per minute (WPM)**.
- In words per second: **$\approx 2.1$ to $2.3$ words per second**.
- **Math Deduction Factor**: When a mathematical formula or intricate visual transition is displayed, speech must pause or slow down to $\approx 1.5$ words per second.

### 3.2 The Word Budget Formula
For every scene or beat:
$$\text{Max Words} = \text{Beat Duration (seconds)} \times 2.0$$

*Example*: A 10-second opening hook must not exceed 20 words. If your draft has 34 words, you are forcing the voiceover to rush, destroying viewer comprehension.

### 3.3 The Breathing Room Rule
Every major visual reveal must have at least **1.5 to 2.5 seconds of silence** (`self.wait(2.0)`):
- Equation written: pause 2.0s.
- Peak anomaly identified: pause 2.5s.
- Never trigger the next sentence while the viewer is still trying to decode the graph that just transformed.

---

## 4. The Two-Column AV Script Format (Industry Standard)

All Animathor storyboards must be organized into the professional **Audio/Visual (AV) Table**. This binds every spoken syllable directly to its corresponding animation trigger and on-screen text.

### Format Structure:

| Beat & Timecode | Visual Action & Mobjects (Manim) | Sync Cue [Word] | Spoken Narration (Voiceover) | Subtitle / MathTex |
|---|---|---|---|---|
| **Beat 1**<br>00:00 - 00:08<br>*(8 seconds)* | `title = Text(...)`<br>`axes = Axes(...)`<br>`target = Line(...)`<br>Draw axes and square wave target. | On word: **"sudut"** | *"Bisakah gelombang sinus yang mulus membentuk sudut kotak 90 derajat?"*<br><br>*(11 kata • 1.38 wps • PASS)* | **Title**: Sudut Patah Fourier<br><br>**Subtitle**: Bisakah gelombang sinus mulus membentuk sudut 90 derajat? |
| **Beat 2**<br>00:08 - 00:20<br>*(12 seconds)* | `eq = MathTex(...)`<br>`curve = axes.plot(...)`<br>Draw fundamental harmonic $N=1$. | On word: **"ganjil"** | *"Deret Fourier menjumlahkan harmonik ganjil satu per satu, dimulai dari frekuensi dasar."*<br><br>*(12 kata • 1.0 wps • PASS)* | **Math**: $S_1(x) = \frac{4}{\pi}\sin(x)$<br><br>**Badge**: N = 1 |

---

## 5. Voice & Tone Guidelines (The 3B1B Standard)

Adopt the persona of a brilliant, calm mathematical mentor:
1. **Curious and Respectful**: Treat the audience as intelligent peers who appreciate seeing how things work under the hood.
2. **Plain-Spoken Rigor**: Prefer simple, precise words over jargon, but never dumb down the mathematics.
3. **Observation-Led**: Guide the viewer's eye: *"Notice how the peak moves closer to the boundary, yet its height stays fixed."*
4. **Honest About Limitations**: Acknowledge when a proof is partial or when intuition precedes formal proof.
