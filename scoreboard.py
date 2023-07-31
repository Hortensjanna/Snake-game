import turtle
from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color('gray20')
        self.goto(-140, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'SCORE: {self.score}        HIGH SCORE: {self.high_score}', False, align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def track_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


