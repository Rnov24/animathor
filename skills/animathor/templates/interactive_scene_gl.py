"""
Animathor Interactive Scene Template (ManimGL / 3b1b Edition)
Engine: ManimGL (pip install manimgl)
Launch command: manimgl interactive_scene_gl.py InteractiveDemo -se 30
"""

from manimlib import *

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


class InteractiveDemo(InteractiveScene):
    def construct(self):
        # 1. Title fixed to screen space
        title = Text("ManimGL Interactive Development", font=MONO, font_size=32)
        title.to_edge(UP, buff=0.5)
        title.fix_in_frame()
        self.add(title)

        # 2. 3D Coordinate axes
        axes = ThreeDAxes()
        self.play(ShowCreation(axes))

        # 3. Interactive Camera Reorientation
        self.play(self.frame.animate.reorient(60, -45, 0))
        self.wait(1.0)

        # 4. LaTeX equation using capital R and t2c mapping
        equation = Tex(
            R"\vec{F} = m \vec{a}",
            t2c={R"\vec{F}": ALERT, "m": PRIMARY, R"\vec{a}": ACCENT}
        )
        equation.next_to(title, DOWN, buff=0.5)
        equation.fix_in_frame()

        self.play(Write(equation))
        self.wait(1.5)

        # Line 35: Breakpoint for interactive development (-se 35)
        # Type checkpoint_paste() in the terminal shell to execute code live!
        # self.embed()
