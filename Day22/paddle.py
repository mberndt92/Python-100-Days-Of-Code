
from turtle import Turtle

MOVE_DISTANCE = 30

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position[0], position[1])

    def move(self, distance):
        self.goto(self.xcor(), self.ycor() + distance)

    def up(self):
        self.move(MOVE_DISTANCE)

    def down(self):
        self.move(-MOVE_DISTANCE)

