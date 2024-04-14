
# Pong

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PLAYER_1_POS = (-360, 0)
PLAYER_2_POS = (360, 0)
WIDTH = 800
HEIGHT = 600
TITLE = "Pong"
BG_COLOR = "black"


def setup_screen():
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(BG_COLOR)
    screen.tracer(0)


def add_listeners():
    screen.listen()
    screen.onkey(player1.up, "w")
    screen.onkey(player1.down, "s")

    screen.onkey(player2.up, "Up")
    screen.onkey(player2.down, "Down")


screen = Screen()
setup_screen()

player1 = Paddle(PLAYER_1_POS)
player2 = Paddle(PLAYER_2_POS)
ball = Ball()
score = Scoreboard()

screen.update()

add_listeners()

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect top/bottom wall collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(player2) < 50 and ball.xcor() > PLAYER_2_POS[0] - 20:
        ball.bounce_x()

    # Detect collision with right paddle
    elif ball.distance(player1) < 50 and ball.xcor() < PLAYER_1_POS[0] + 20:
        ball.bounce_x()

    # Player 1 scores
    if ball.xcor() > 400:
        score.score_left()
        ball.reset()
        ball.bounce_x()
    # Player 2 scores
    elif ball.xcor() < -400:
        score.score_right()
        ball.reset()
        ball.bounce_x()

screen.exitonclick()


