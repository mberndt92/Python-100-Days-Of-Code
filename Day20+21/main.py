import turtle
# Snake Game

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def run_snake(snake, screen, scoreboard):
    is_game_on = True
    food = Food()
    screen.update()
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            scoreboard.scored()
            food.refresh()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            is_game_on = False
            scoreboard.game_over()

        # Detect collision with tail.
        # if head collides with any segment in the tail:
            # trigger game over

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                scoreboard.game_over()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Metal Gear Solid: Snake's Return")
screen.tracer(0)
screen.listen()

snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = Scoreboard()

screen.update()
run_snake(snake, screen, scoreboard)

screen.exitonclick()