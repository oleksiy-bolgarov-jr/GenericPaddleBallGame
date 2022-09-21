from turtle import Turtle

from constants import *

FONT_ALIGNMENT = "center"
FONT = ("Courier", 80, "bold")


class Scoreboard:
    def __init__(self):
        self._left_score = 0
        self._right_score = 0

        self.turtle = Turtle(visible=False)
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.speed(0)

        self.refresh()

    def refresh(self):
        self.turtle.clear()

        x = -SCORE_OFFSET_FROM_MIDDLE_LINE
        y = SCREEN_HEIGHT / 2 - SCORE_OFFSET_FROM_MIDDLE_LINE
        self.turtle.goto(x, y)
        self.turtle.write(self._left_score, align=FONT_ALIGNMENT, font=FONT)

        x = SCORE_OFFSET_FROM_MIDDLE_LINE
        self.turtle.goto(x, y)
        self.turtle.write(self._right_score, align=FONT_ALIGNMENT, font=FONT)

    def increment_score(self, is_right_score: bool):
        if is_right_score:
            self._right_score += 1
        else:
            self._left_score += 1
        self.refresh()
