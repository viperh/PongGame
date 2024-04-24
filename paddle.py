from turtle import Turtle
from design import Design


def check_position(new_y) -> bool:
    if new_y > Design.screen_height // 2 or new_y < Design.screen_height // -2:
        return False
    else:
        return True


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(Design.paddle_base_shape)
        self.color(Design.paddle_color)
        self.shapesize(stretch_wid=Design.paddle_stretch_wid, stretch_len=1)
        self.penup()

    def move_down(self):
        new_y = self.ycor() - 20
        if check_position(new_y):
            self.goto(self.xcor(), new_y)

    def move_up(self):
        new_y = self.ycor() + 20
        if check_position(new_y):
            self.goto(self.xcor(), new_y)
