# Animating the plot and saving it
from manimlib import *

class monteCarlo(Scene):
    def construct(self):
        axes = Axes(x_range = [-0.1, 1.1, 0.1],
                    y_range = [-0.1, 1.1, 0.1])
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio = 0.01, run_time = 1))

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)