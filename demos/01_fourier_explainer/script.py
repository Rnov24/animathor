"""
Animathor Demo: Fourier Harmonic Decomposition
Engine: Manim Community Edition (ManimCE)
Aspect Ratio: 1920x1080 (16:9 Widescreen)
"""

from manim import *
import platform

# 1. Typography Standard: Monospace prevents Pango kerning overlap bugs
if platform.system() == "Windows":
    MONO = "Consolas"
elif platform.system() == "Darwin":
    MONO = "Menlo"
else:
    MONO = "DejaVu Sans Mono"

# 2. Cohesive Color Palette - Classic 3B1B Dark Slate Cinema
BG = "#0B0F19"          # Deep Slate Midnight
PRIMARY = "#58C4DD"     # 3B1B Cyan-Blue (Primary focus)
SECONDARY = "#83C167"   # 3B1B Sage Green (Contextual)
ACCENT = "#FACC15"      # Vibrant Yellow (Highlights & headers)
ALERT = "#FF5964"       # Coral Red (Anomalies & attention)
MUTED = "#64748B"       # Slate Grey (Structural axes & grids)
SURFACE = "#121726"     # Card surface


class FourierExplainerScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        # --- TIER 1: HEADER & TITLE (UP * 3.2) ---
        title = Text("Fourier Harmonic Decomposition", font=MONO, font_size=36, color=ACCENT, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=1.2)
        self.wait(0.5)

        # --- TIER 2: STRUCTURAL LAYER (Axes with 0.25 - 0.35 opacity) ---
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": MUTED, "stroke_width": 2, "stroke_opacity": 0.4},
            tips=False,
        ).shift(DOWN * 0.4)

        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=5,
            background_line_style={"stroke_color": MUTED, "stroke_width": 1, "stroke_opacity": 0.15},
        ).shift(DOWN * 0.4)

        self.play(Create(grid), Create(axes), run_time=1.0)

        # --- TIER 3: CONTEXTUAL REFERENCE LAYER (Opacity 0.5 - 0.7) ---
        # Target step / square shape
        square_target = VGroup(
            Line(axes.c2p(-4, -1), axes.c2p(0, -1), color=SECONDARY, stroke_width=3, stroke_opacity=0.6),
            Line(axes.c2p(0, 1), axes.c2p(4, 1), color=SECONDARY, stroke_width=3, stroke_opacity=0.6),
        )
        target_label = Text("Target Function f(x)", font=MONO, font_size=20, color=SECONDARY)
        target_label.next_to(square_target, UP, buff=0.2).set_opacity(0.8)

        self.play(Create(square_target), FadeIn(target_label), run_time=1.0)
        self.wait(0.5)

        # --- TIER 4: PRIMARY ANIMATION LAYER (Opacity 1.0) ---
        # First harmonic curve
        curve1 = axes.plot(lambda x: (4 / np.pi) * np.sin(x), color=PRIMARY, stroke_width=3.5)
        curve1_label = MathTex(r"S_1(x) = \frac{4}{\pi}\sin(x)", color=PRIMARY, font_size=28)
        curve1_label.next_to(axes, DOWN, buff=0.4)

        self.play(Create(curve1), Write(curve1_label), run_time=1.5)
        self.wait(1.0)

        # Morphing to higher harmonic
        curve3 = axes.plot(
            lambda x: (4 / np.pi) * (np.sin(x) + np.sin(3 * x) / 3),
            color=PRIMARY,
            stroke_width=3.5
        )
        curve3_label = MathTex(
            r"S_3(x) = \frac{4}{\pi}\left[\sin(x) + \frac{\sin(3x)}{3}\right]",
            color=PRIMARY,
            font_size=28
        )
        curve3_label.next_to(axes, DOWN, buff=0.4)

        self.play(
            ReplacementTransform(curve1, curve3),
            ReplacementTransform(curve1_label, curve3_label),
            run_time=1.5
        )
        self.wait(1.5)

        # --- TIER 5: ATTENTION / RESOLUTION (Glow / Alert) ---
        focus_dot = Dot(point=axes.c2p(0.3, 1.18), color=ALERT, radius=0.1)
        alert_arrow = Arrow(
            start=axes.c2p(1.2, 1.8),
            end=axes.c2p(0.35, 1.25),
            color=ALERT,
            buff=0.1,
            stroke_width=3,
        )
        alert_text = Text("+8.95% Overshoot", font=MONO, font_size=20, color=ALERT, weight=BOLD)
        alert_text.next_to(alert_arrow.get_start(), UP, buff=0.15)

        self.play(GrowFromCenter(focus_dot), Create(alert_arrow), Write(alert_text), run_time=1.2)
        self.wait(2.5)  # Breathing room for insight

        # Clean Exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.5)
