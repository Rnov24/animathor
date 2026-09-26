"""
Animathor Scene Script
Engine: Manim Community Edition (ManimCE)
Settings inherited from local manim.cfg
"""

from manim import *
import platform

# 1. Monospace font guard
if platform.system() == "Windows":
    MONO = "Consolas"
elif platform.system() == "Darwin":
    MONO = "Menlo"
else:
    MONO = "DejaVu Sans Mono"

# 2. Palette
BG = "#0B0F19"
PRIMARY = "#58C4DD"
SECONDARY = "#83C167"
ACCENT = "#FACC15"
ALERT = "#FF5964"
MUTED = "#64748B"
SURFACE = "#121726"
BORDER = "#1E293B"


class MainScene(Scene):
    def construct(self):
        # Background color is configured in manim.cfg, but set here as safety
        self.camera.background_color = BG

        # Title
        title = Text("Konsep Animasi Utama", font=MONO, font_size=36, color=ACCENT)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.2)
        self.wait(0.5)

        # Coordinate axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6.5,
            y_length=4.5,
            axis_config={"color": MUTED, "stroke_width": 2, "stroke_opacity": 0.35},
            tips=False,
        )
        self.play(Create(axes), run_time=1.0)

        # Animated function plot
        graph = axes.plot(lambda x: np.sin(x), color=PRIMARY, stroke_width=3.5)
        graph_label = MathTex(r"f(x) = \sin(x)", color=PRIMARY, font_size=28)
        graph_label.next_to(axes, DOWN, buff=0.4)

        self.play(Create(graph), Write(graph_label), run_time=1.5)
        self.wait(2.0)  # Breathing room

        # Clean Exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.3)
