"""
Animathor Vertical Shorts Template (9:16 Portrait / Shorts / Reels / TikTok)
Engine: Manim Community Edition (ManimCE)
Resolution: 1080x1920 (9:16)
"""

from manim import *
import platform

# 1. Canvas Configuration: Vertical 9:16 Portrait
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

# 2. Typography Standard
if platform.system() == "Windows":
    MONO = "Consolas"
elif platform.system() == "Darwin":
    MONO = "Menlo"
else:
    MONO = "DejaVu Sans Mono"

# 3. Palette
BG = "#0B0F19"
PRIMARY = "#58C4DD"
SECONDARY = "#83C167"
ACCENT = "#FACC15"
ALERT = "#FF5964"
MUTED = "#64748B"
SURFACE = "#121726"
BORDER = "#1E293B"


class VerticalShortsScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        # =====================================================================
        # TOP SAFE ZONE: CATEGORY PILL & TITLE (UP * 6.8 to UP * 7.2)
        # =====================================================================
        pill_box = RoundedRectangle(
            corner_radius=0.15,
            width=3.8,
            height=0.55,
            color=PRIMARY,
            fill_color="#09222E",
            fill_opacity=0.9,
            stroke_width=1.5,
        ).move_to(UP * 7.0)

        pill_text = Text(
            "MATEMATIKA & SINYAL",
            font=MONO,
            font_size=18,
            weight=BOLD,
            color=PRIMARY,
        ).move_to(pill_box.get_center())

        header = VGroup(pill_box, pill_text)

        title = Text(
            "Fenomena Gibbs",
            font=MONO,
            font_size=36,
            weight=BOLD,
            color=ACCENT,
        ).next_to(pill_box, DOWN, buff=0.35)

        self.play(FadeIn(header), Write(title), run_time=1.2)
        self.wait(0.5)

        # =====================================================================
        # CENTRAL VISUAL ZONE (Y: -3.0 to +4.5, X: -3.8 to +3.8)
        # =====================================================================
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-1.8, 1.8, 1],
            x_length=7.2,
            y_length=5.5,
            axis_config={"color": MUTED, "stroke_width": 2, "stroke_opacity": 0.35},
            tips=False,
        ).move_to(UP * 0.5)

        # Structural reference (Target step function)
        target = VGroup(
            DashedLine(axes.c2p(-3.5, -1), axes.c2p(0, -1), color=SECONDARY, stroke_opacity=0.6, dash_length=0.1),
            DashedLine(axes.c2p(0, 1), axes.c2p(3.5, 1), color=SECONDARY, stroke_opacity=0.6, dash_length=0.1),
        )

        self.play(Create(axes), Create(target), run_time=1.0)

        # Main animated curve
        curve = axes.plot(lambda x: (4 / np.pi) * np.sin(x), color=PRIMARY, stroke_width=3.5)
        curve_badge = Text("Harmonik N = 1", font=MONO, font_size=20, color=PRIMARY)
        curve_badge.next_to(axes, UP, buff=0.2)

        self.play(Create(curve), FadeIn(curve_badge), run_time=1.2)
        self.wait(1.0)

        # Transform to higher frequency
        curve_high = axes.plot(
            lambda x: (4 / np.pi) * sum(np.sin(k * x) / k for k in range(1, 21, 2)),
            color=PRIMARY,
            stroke_width=3.5
        )
        curve_badge_high = Text("Harmonik N = 19", font=MONO, font_size=20, color=PRIMARY)
        curve_badge_high.next_to(axes, UP, buff=0.2)

        self.play(
            ReplacementTransform(curve, curve_high),
            ReplacementTransform(curve_badge, curve_badge_high),
            run_time=1.5
        )
        self.wait(1.0)

        # Attention: Peak overshoot indicator
        peak_dot = Dot(point=axes.c2p(0.16, 1.18), color=ALERT, radius=0.12)
        overshoot_label = Text("Overshoot ~8.95%!", font=MONO, font_size=22, color=ALERT, weight=BOLD)
        overshoot_label.next_to(peak_dot, UR, buff=0.2)

        self.play(GrowFromCenter(peak_dot), Write(overshoot_label), run_time=1.0)
        self.wait(2.0)  # Insight pause

        # =====================================================================
        # BOTTOM SAFE ZONE: SUBTITLE CARD (DOWN * 6.0)
        # =====================================================================
        sub_card = RoundedRectangle(
            corner_radius=0.2,
            width=7.8,
            height=1.2,
            color=BORDER,
            fill_color=SURFACE,
            fill_opacity=0.92,
            stroke_width=1.5,
        ).move_to(DOWN * 6.0)

        sub_text = Text(
            "Lonjakan di dekat tebing patahan\ntidak akan pernah hilang!",
            font=MONO,
            font_size=20,
            color=WHITE,
            line_spacing=0.8,
        ).move_to(sub_card.get_center())

        subtitle_group = VGroup(sub_card, sub_text)
        self.play(FadeIn(subtitle_group), run_time=0.8)
        self.wait(2.5)

        # Clean Exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.5)
