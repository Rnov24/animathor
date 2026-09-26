# 04. Core Patterns & Implementation Recipes

This guide catalogs the most vital, battle-tested animation patterns in Manim.

---

## 1. Dynamic Updaters & ValueTrackers

Updaters allow objects to dynamically recalculate their geometry or text on every frame based on changing parameters.

### 1.1 Moving Tangent Line & Secant
```python
from manim import *

class TangentTracker(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[-1, 9, 2], x_length=7, y_length=5)
        curve = axes.plot(lambda x: x**2, color=BLUE)
        self.play(Create(axes), Create(curve))

        # Value tracker for the x-coordinate
        x_tracker = ValueTracker(-2.0)

        # Dot pinned to the curve
        dot = always_redraw(lambda: Dot(
            point=axes.c2p(x_tracker.get_value(), (x_tracker.get_value())**2),
            color=YELLOW
        ))

        # Dynamic tangent line
        tangent = always_redraw(lambda: axes.get_secant_slope_group(
            x = x_tracker.get_value(),
            graph = curve,
            dx = 0.001,
            secant_line_length = 3,
            secant_line_color = RED
        ))

        self.add(dot, tangent)
        self.play(x_tracker.animate.set_value(2.0), run_time=4, rate_func=linear)
        self.wait(1)
```

### 1.2 Dynamic Number Counters
```python
counter = ValueTracker(0)

# DecimalNumber automatically renders formatting
number_display = DecimalNumber(0, num_decimal_places=2, color=YELLOW)
number_display.add_updater(lambda mob: mob.set_value(counter.get_value()))

self.add(number_display)
self.play(counter.animate.set_value(100), run_time=3)
```

---

## 2. LaTeX Equation Derivation & Morphing

To make equation morphing look seamless, always match math components using `TransformMatchingTex`.

```python
class EquationDerivation(Scene):
    def construct(self):
        # Step 1: Initial formula
        eq1 = MathTex(
            r"\frac{d}{dx}\left[ f(x) \cdot g(x) \right] = \lim_{h \to 0} \frac{f(x+h)g(x+h) - f(x)g(x)}{h}",
            font_size=32
        )
        eq1.set_color_by_tex("f", BLUE)
        eq1.set_color_by_tex("g", GREEN)

        self.play(Write(eq1))
        self.wait(1.5)

        # Step 2: Product rule result
        eq2 = MathTex(
            r"\frac{d}{dx}\left[ f(x) \cdot g(x) \right] = f'(x)g(x) + f(x)g'(x)",
            font_size=36
        )
        eq2.set_color_by_tex("f", BLUE)
        eq2.set_color_by_tex("g", GREEN)

        # Transform matching substrings seamlessly
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)
```

---

## 3. Function Plotting, Coordinate Systems & Area Fills

### 3.1 Plotting with Riemann Rectangles
```python
axes = Axes(x_range=[0, 5], y_range=[0, 10], x_length=6, y_length=4)
graph = axes.plot(lambda x: 0.5 * x**2, color=CYAN)

# Area under curve
area = axes.get_area(graph, x_range=[1, 4], color=BLUE, opacity=0.3)

# Riemann sums approximation
rects = axes.get_riemann_rectangles(
    graph,
    x_range=[1, 4],
    dx=0.25,
    stroke_color=WHITE,
    fill_opacity=0.5
)

self.play(Create(axes), Create(graph))
self.play(FadeIn(area))
self.play(ReplacementTransform(area, rects))
```

---

## 4. Layout, Grouping & Alignment

### 4.1 Arranging Mobjects
```python
# Arrange in grid or row
shapes = VGroup(Square(), Circle(), Triangle()).arrange(RIGHT, buff=0.8)
self.play(Create(shapes))

# Aligning elements relative to one another
label = Text("Target Area", font="Consolas", font_size=20)
label.next_to(shapes, DOWN, buff=0.5)
```

### 4.2 Clean Scene Teardown (Clean Exit)
Always clean up mobjects before transitioning to the next scene or ending:
```python
# Cleans all on-screen mobjects smoothly in 0.5 seconds
self.play(FadeOut(Group(*self.mobjects)), run_time=0.5)
self.wait(0.2)
```
