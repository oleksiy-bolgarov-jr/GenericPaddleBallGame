from turtle import Screen, Turtle
import random
import sys
import time

from constants import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def draw_dotted_line_in_middle():
    turtle = Turtle(visible=False)
    turtle.color("white")
    turtle.penup()
    turtle.speed(0)
    turtle.goto(0, SCREEN_HEIGHT / 2)
    turtle.setheading(270)

    while turtle.ycor() > -SCREEN_HEIGHT / 2:
        turtle.pendown()
        turtle.forward(BALL_DIAMETER)
        turtle.penup()
        turtle.forward(BALL_DIAMETER)


def quit_game():
    global user_quit
    user_quit = True


def pause_game():
    global paused
    paused = not paused


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Generic Paddle Ball Game")
screen.tracer(0)

draw_dotted_line_in_middle()

left_paddle = Paddle(-SCREEN_WIDTH / 2 + PADDLE_OFFSET)
right_paddle = Paddle(SCREEN_WIDTH / 2 - PADDLE_OFFSET)
scoreboard = Scoreboard()

is_going_right = random.random() < 0.5
user_quit = False
paused = False

ball = Ball(is_going_right)

screen.listen()
screen.onkeypress(lambda: left_paddle.move_up(paused), "w")
screen.onkeypress(lambda: left_paddle.move_down(paused), "s")
screen.onkeypress(lambda: right_paddle.move_up(paused), "Up")
screen.onkeypress(lambda: right_paddle.move_down(paused), "Down")
screen.onkeypress(quit_game, "q")
screen.onkeypress(pause_game, "p")

while True:
    screen.update()
    time.sleep(0.01)
    if user_quit:
        sys.exit()
    if paused:
        continue

    ball.move()

    if ball.is_in_right_paddle_zone() and ball.collided_with_paddle(right_paddle.ycor()):
        ball.bounce_off_paddle(is_right_paddle=True, paddle_y=right_paddle.ycor())
    elif ball.is_in_left_paddle_zone() and ball.collided_with_paddle(left_paddle.ycor()):
        ball.bounce_off_paddle(is_right_paddle=False, paddle_y=left_paddle.ycor())
    elif ball.is_out_of_bounds(is_right_side=True):
        scoreboard.increment_score(is_right_score=False)
        screen.update()
        time.sleep(0.5)
        is_going_right = not is_going_right
        ball.initialize_position(is_going_right)
    elif ball.is_out_of_bounds(is_right_side=False):
        scoreboard.increment_score(is_right_score=True)
        screen.update()
        time.sleep(0.5)
        is_going_right = not is_going_right
        ball.initialize_position(is_going_right)
