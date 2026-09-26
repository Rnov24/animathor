# 03. Dual-Engine Rosetta Stone (ManimCE vs ManimGL)

Manim exists in two major active branches:
1. **Manim Community Edition (ManimCE)**: Maintained by the community, highly documented, cross-platform, modular, CLI-driven, headless render friendly.
2. **ManimGL (3b1b)**: Maintained by Grant Sanderson (3Blue1Brown), powered by modern OpenGL / ModernGL, supports interactive live coding (`-se` flag, `checkpoint_paste()`).

This Rosetta Stone guide provides direct syntax translations between both engines.

---

## 1. Quick Equivalence Table

| Capability | Manim Community Edition (ManimCE) | ManimGL (3b1b) |
|---|---|---|
| **Package / PyPI** | `pip install manim` | `pip install manimgl` |
| **CLI Command** | `manim` | `manimgl` |
| **Import** | `from manim import *` | `from manimlib import *` |
| **Scene Base Class** | `class MyScene(Scene):` | `class MyScene(InteractiveScene):` |
| **3D Scene Class** | `class My3D(ThreeDScene):` | `class My3D(InteractiveScene):` |
| **Math Text Object** | `MathTex(r"\int_a^b f(x)dx")` | `Tex(R"\int_a^b f(x)dx")` |
| **Regular Text** | `Text("Hello", font=MONO)` | `Text("Hello", font=MONO)` |
| **Color Map in Math** | `formula.set_color_by_tex("x", RED)` | `Tex(..., t2c={"x": RED})` |
| **Draw / Create Anim** | `self.play(Create(mob))` | `self.play(ShowCreation(mob))` |
| **Write Anim** | `self.play(Write(text))` | `self.play(Write(text))` |
| **Morph Anim** | `ReplacementTransform(A, B)` | `ReplacementTransform(A, B)` |
| **Formula Morphing** | `TransformMatchingTex(eq1, eq2)` | `TransformMatchingTex(eq1, eq2)` |
| **Camera Frame** | `self.camera.frame` | `self.frame` |
| **Camera Reorient** | `self.move_camera(phi=..., theta=...)` | `self.frame.reorient(phi, theta, gamma)` |
| **Fixed HUD / Screen Space** | `self.add_fixed_in_frame_mobjects(mob)` | `mob.fix_in_frame()` |
| **Interactive Debugger** | `self.interactive_embed()` | `manimgl scene.py Scene -se 20` |
| **Live Code Paste** | *(Not natively supported)* | `checkpoint_paste()` |
| **Clean Scene Exit** | `self.play(FadeOut(Group(*self.mobjects)))` | `self.play(FadeOut(Group(*self.mobjects)))` |

---

## 2. In-Depth Syntax Comparisons

### 2.1 Math Equations and Color Mapping

#### ManimCE Pattern:
```python
from manim import *

# Raw string with lowercase 'r'
eq1 = MathTex(r"E", r"=", r"m", r"c^2")
eq1.set_color_by_tex("E", BLUE)
eq1.set_color_by_tex("m", GREEN)
eq1.set_color_by_tex("c", YELLOW)

# Or isolated substrings for TransformMatchingTex:
step1 = MathTex(r"a^2 + b^2", r"=", r"c^2", substrings_to_isolate=["a", "b", "c"])
step2 = MathTex(r"c", r"=", r"\sqrt{a^2 + b^2}", substrings_to_isolate=["a", "b", "c"])
self.play(TransformMatchingTex(step1, step2))
```

#### ManimGL Pattern:
```python
from manimlib import *

# Capital 'R' string and t2c dictionary mapping
eq1 = Tex(
    R"E = m c^2",
    t2c={"E": BLUE, "m": GREEN, "c": YELLOW}
)

# TransformMatchingTex works similarly
step1 = Tex(R"a^2 + b^2 = c^2")
step2 = Tex(R"c = \sqrt{a^2 + b^2}")
self.play(TransformMatchingTex(step1, step2))
```

---

### 2.2 3D Cameras and Frame Manipulation

#### ManimCE Pattern:
```python
from manim import *

class Scene3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes))
        
        # Animate camera rotation
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        # Fixed 2D HUD element over 3D space
        label = Text("3D Coordinate System", font="Consolas", font_size=24)
        label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(label)
```

#### ManimGL Pattern:
```python
from manimlib import *

class Scene3D(InteractiveScene):
    def construct(self):
        axes = ThreeDAxes()
        self.play(ShowCreation(axes))
        
        # Camera is directly accessible via self.frame
        self.play(self.frame.animate.reorient(75, 30, 0))
        
        # Fixed 2D HUD element
        label = Text("3D Coordinate System", font="Consolas", font_size=24)
        label.to_corner(UL)
        label.fix_in_frame()
        self.add(label)
```

---

### 2.3 Interactive Development Mode

#### ManimGL Killer Feature:
Run directly from terminal to freeze at line 25:
```powershell
manimgl scene.py MyScene -se 25
```
An IPython shell opens while the OpenGL window stays interactive. You can modify code in your editor, copy it to clipboard, and run:
```python
checkpoint_paste()           # Executes with animation
checkpoint_paste(skip=True)  # Executes instantly without animation
checkpoint_paste(record=True) # Records the segment into video
```

#### ManimCE Equivalent:
```python
def construct(self):
    circle = Circle()
    self.play(Create(circle))
    self.interactive_embed()  # drops into an interactive shell
```

---

## 3. Decision Matrix: Which Engine to Pick?

| Requirement | Recommended Engine |
|---|---|
| Creating animated short videos (Shorts/Reels) | **ManimCE** (flexible configuration, stable headless CLI) |
| YouTube standard explainer videos | **ManimCE** |
| Live math exploration, lectures, interactive talks | **ManimGL** |
| Complex custom GLSL shader programming | **ManimGL** |
| Automated CI/CD or server-side video rendering | **ManimCE** |
