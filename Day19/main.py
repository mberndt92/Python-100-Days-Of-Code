
# Turtle Race

from turtle import Turtle, Screen
import random


def setup_turtles():
    turtles = []
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    padding = 20
    x_start = -250
    y_start = -100

    for color in colors:
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(x_start + padding, y_start)
        turtles.append(turtle)
        y_start += (200 / len(colors))

    return turtles


def start_race(turtles):
    is_racing = True
    while is_racing:
        for turtle in turtles:
            turtle.goto(turtle.xcor() + random.randint(1, 10), turtle.ycor())
            if turtle.xcor() >= 230:
                is_racing = False
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    print(f"You won! The winning turtle is {winning_color}")
                else:
                    print(f"The Winner is {winning_color}")


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make your bet", "Which turtle is going to win (color): ")

turtles = setup_turtles()
start_race(turtles)

screen.exitonclick()