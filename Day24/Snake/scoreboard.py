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
        self.high_score = 0
        self.read_high_score()
        self.update_score()
        self.hideturtle()

    def read_high_score(self):
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())

    def write_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.score}")

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def scored(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()

        self.score = 0
        self.update_score()
