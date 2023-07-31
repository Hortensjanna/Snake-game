import turtle
from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())
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
            with open("data.txt", mode='w') as data_file:
                data_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def track_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


