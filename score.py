from turtle import Turtle

from design import Design

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color(Design.score_color)
        self.font = Design.font
        self.penup()
        self.hideturtle()
        self.score = Design.start_score

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(self.score)

