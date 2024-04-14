# Edge-a-sketch

from turtle import Turtle, Screen


def forward():
    timmy.forward(10)


def back():
    timmy.back(10)


def left():
    timmy.setheading(timmy.heading() + 10)


def right():
    timmy.setheading(timmy.heading() - 10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


timmy = Turtle()
screen = Screen()
screen.setup(1000, 1000)

screen.listen()
screen.onkey(forward, "w")
screen.onkey(left, "a")
screen.onkey(back, "s")
screen.onkey(right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
