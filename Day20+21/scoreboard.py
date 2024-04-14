import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.goto(0, 270)
        self.score = 0
        self.print_score()
        self.hideturtle()


    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def scored(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
