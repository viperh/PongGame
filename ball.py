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
        self.speed = 10
        self.move_vert = self.speed
        self.move_hor = self.speed

    def move(self):
        self.y_pos += self.move_vert
        self.x_pos += self.move_hor
        self.goto(self.x_pos, self.y_pos)
        sleep(0.1)

    def bounce_y(self):
        self.move_vert *= -1

    def bounce_x(self):
        self.move_hor *= -1
