from turtle import (Turtle)
from math import fabs

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.setup_snake()
        self.head = self.segments[0]

    def setup_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        square = Turtle("square")
        square.penup()
        square.color("white")
        square.goto(position)
        self.segments.append(square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def face(self, angle):
        is_opposite_direction = abs(self.head.heading() - angle) == 180
        if not is_opposite_direction:
            self.head.setheading(angle)

    def up(self):
        self.face(UP)

    def down(self):
        self.face(DOWN)

    def left(self):
        self.face(LEFT)

    def right(self):
        self.face(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.setup_snake()
        self.head = self.segments[0]
