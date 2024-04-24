from turtle import Turtle
from time import sleep


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_pos = 0
        self.y_pos = 0
        self.vert_dir = True
        self.hor_dir = True

    def move(self):

        if self.vert_dir:
            self.y_pos += 10
        else:
            self.y_pos -= 10

        if self.hor_dir:
            self.x_pos += 10
        else:
            self.x_pos -= 10



        self.goto(self.x_pos, self.y_pos)
        sleep(0.1)

    def change_direction_(self):
        self.ascending = not self.ascending
