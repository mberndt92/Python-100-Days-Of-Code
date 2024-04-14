import turtle
from turtle import Turtle, Screen
import random
import colorgram

def draw_square():
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)

def draw_dashed_line():
    for _ in range(50):
        timmy.forward(2)
        timmy.penup()
        timmy.forward(2)
        timmy.pendown()


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.right(angle)
        timmy.forward(80)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_fancy_shapes():
    for sides in range(3, 9):
        timmy.color(random_color())
        draw_shape(sides)


def random_walk():
    timmy.pensize(10)
    directions = [0, 90, 180, 270]
    while True:
        timmy.color(random_color())
        timmy.setheading(random.choice(directions))
        timmy.forward(25)


def draw_circles(gap):
    for circle in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)


def extract_colors():
    colors = colorgram.extract('hirst_spot_painting.jpg', 30)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors

def draw_spot_painting(spots):
    colors = extract_colors()

    spacing = 70
    size = 20
    # turtle.setworldcoordinates(-spacing, -spacing, 1000, 1000)
    timmy.speed("fastest")
    timmy.hideturtle()
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(350)
    timmy.setheading(0)

    start_pos = (timmy.xcor(), timmy.ycor())

    for y in range(10):
        timmy.penup()
        timmy.goto(start_pos[0] - spacing, start_pos[1] - spacing + y * spacing)
        timmy.pendown()
        for x in range(10):
            color = random.choice(colors)
            timmy.dot(size,random.choice(colors))
            timmy.penup()
            timmy.forward(spacing)
            timmy.pendown()



timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
turtle.colormode(255)
screen = Screen()
screen.setup(1000, 1000)
timmy.color("Green")

random_walk()
# draw_spot_painting(10)

screen.exitonclick()

