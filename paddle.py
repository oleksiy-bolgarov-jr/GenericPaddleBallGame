from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.speed(0)
        self.goto(x_pos, 0)

    def move_up(self, paused: bool = False):
        if not paused and self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self, paused: bool = False):
        if not paused and self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)
