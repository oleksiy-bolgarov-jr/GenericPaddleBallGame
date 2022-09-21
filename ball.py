from turtle import Turtle
import random

from constants import *

INITIAL_MOVE_INCREMENT = 2
MOVE_INCREMENT_INCREASE_BY = 1


class Ball(Turtle):
    def __init__(self, start_on_right: bool = True):
        super().__init__("circle")
        self.penup()
        self.color("white")
        self.speed(0)

        self.move_increment = INITIAL_MOVE_INCREMENT    # To make the linter happy
        self.initialize_position(is_going_right=start_on_right)

    def initialize_position(self, is_going_right: bool):
        lower_bound = -SCREEN_HEIGHT / 2 + BALL_DIAMETER
        upper_bound = SCREEN_HEIGHT / 2 - BALL_DIAMETER

        if is_going_right:
            angle = random.randint(-MAX_INIT_ANGLE, MAX_INIT_ANGLE)
        else:
            angle = random.randint(180 - MAX_INIT_ANGLE, 180 + MAX_INIT_ANGLE)
        y_pos = random.randint(lower_bound, upper_bound)

        self.goto(0, y_pos)
        self.setheading(angle)

        self.move_increment = INITIAL_MOVE_INCREMENT

    def move(self):
        if self.ycor() <= (-SCREEN_HEIGHT + BALL_DIAMETER) / 2 or self.ycor() >= (SCREEN_HEIGHT - BALL_DIAMETER) / 2:
            self.bounce_off_wall()
        self.forward(self.move_increment)

    def bounce_off_wall(self):
        self.setheading(-self.heading())

    def is_in_left_paddle_zone(self) -> bool:
        return -SCREEN_WIDTH / 2 + PADDLE_OFFSET < self.xcor() < -(SCREEN_WIDTH - BALL_DIAMETER) / 2 + PADDLE_OFFSET

    def is_in_right_paddle_zone(self) -> bool:
        return SCREEN_WIDTH / 2 - PADDLE_OFFSET > self.xcor() > (SCREEN_WIDTH - BALL_DIAMETER) / 2 - PADDLE_OFFSET

    def is_out_of_bounds(self, is_right_side: bool) -> bool:
        return (self.xcor() > SCREEN_WIDTH / 2) if is_right_side else (self.xcor() < -SCREEN_WIDTH / 2)

    def collided_with_paddle(self, paddle_y: float) -> bool:
        return abs(self.ycor() - paddle_y) < (PADDLE_LENGTH + BALL_DIAMETER) / 2

    def bounce_off_paddle(self, is_right_paddle: bool, paddle_y: float):
        if is_right_paddle:
            bottom_angle = 180 + MAX_BOUNCE_ANGLE
        else:
            bottom_angle = -MAX_BOUNCE_ANGLE
        bounce_range = 2 * MAX_BOUNCE_ANGLE

        distance_from_bottom = self.ycor() - (paddle_y - PADDLE_LENGTH / 2)
        paddle_proportion_from_bottom = distance_from_bottom / PADDLE_LENGTH
        angle_from_bottom = bounce_range * paddle_proportion_from_bottom
        if is_right_paddle:
            new_angle = bottom_angle - angle_from_bottom
        else:
            new_angle = bottom_angle + angle_from_bottom

        self.setheading(new_angle)
        self.move_increment += MOVE_INCREMENT_INCREASE_BY
