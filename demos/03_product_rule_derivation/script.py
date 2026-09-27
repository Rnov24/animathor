"""
Animathor Demo: Product Rule Derivation
Engine: Manim Community Edition (ManimCE)
Aspect Ratio: 1920x1080 (16:9 Widescreen)
"""

from manim import *
import platform

if platform.system() == "Windows":
    MONO = "Consolas"
elif platform.system() == "Darwin":
    MONO = "Menlo"
else:
    MONO = "DejaVu Sans Mono"

BG = "#0B0F19"
PRIMARY = "#58C4DD"
SECONDARY = "#83C167"
ACCENT = "#FACC15"
ALERT = "#FF5964"
MUTED = "#64748B"


class ProductRuleDerivationScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Header
        title = Text("Product Rule Derivation", font=MONO, font_size=32, color=ACCENT)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        self.wait(0.5)

        # Step 1: Definition of derivative
        eq1 = MathTex(
            r"\frac{d}{dx}[f(x)g(x)]",
            r"=",
            r"\lim_{h \to 0}",
            r"\frac{f(x+h)g(x+h) - f(x)g(x)}{h}",
            font_size=36,
        )
        eq1.set_color_by_tex("f", PRIMARY)
        eq1.set_color_by_tex("g", SECONDARY)

        note1 = Text("Derivative limit definition", font=MONO, font_size=20, color=MUTED)
        note1.next_to(eq1, DOWN, buff=0.6)

        self.play(Write(eq1), FadeIn(note1), run_time=1.5)
        self.wait(2.0)

        # Step 2: Add and subtract trick: + f(x+h)g(x) - f(x+h)g(x)
        eq2 = MathTex(
            r"\frac{d}{dx}[f(x)g(x)]",
            r"=",
            r"\lim_{h \to 0}",
            r"\frac{f(x+h)[g(x+h)-g(x)] + g(x)[f(x+h)-f(x)]}{h}",
            font_size=32,
        )
        eq2.set_color_by_tex("f", PRIMARY)
        eq2.set_color_by_tex("g", SECONDARY)

        note2 = Text("Factor f(x+h) and g(x)", font=MONO, font_size=20, color=MUTED)
        note2.next_to(eq2, DOWN, buff=0.6)

        self.play(
            TransformMatchingTex(eq1, eq2),
            ReplacementTransform(note1, note2),
            run_time=1.8,
        )
        self.wait(2.0)

        # Step 3: Final formulation
        eq3 = MathTex(
            r"\frac{d}{dx}[f(x)g(x)]",
            r"=",
            r"f(x)g'(x)",
            r"+",
            r"f'(x)g(x)",
            font_size=42,
        )
        eq3.set_color_by_tex("f", PRIMARY)
        eq3.set_color_by_tex("g", SECONDARY)

        note3 = Text("Product Rule Complete", font=MONO, font_size=22, color=ACCENT, weight=BOLD)
        note3.next_to(eq3, DOWN, buff=0.6)

        surround = SurroundingRectangle(eq3, color=ACCENT, buff=0.3, corner_radius=0.1)

        self.play(
            TransformMatchingTex(eq2, eq3),
            ReplacementTransform(note2, note3),
            Create(surround),
            run_time=1.8,
        )
        self.wait(3.0)  # Breathing room for retention

        # Clean Exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.3)
