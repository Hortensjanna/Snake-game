import turtle
from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('gray20')
        self.goto(-245, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'SCORE: {self.score}', False, align=ALIGMENT, font=FONT)

    def track_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGMENT, font=FONT)
