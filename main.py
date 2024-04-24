from turtle import Screen

from ball import Ball
from design import Design
from paddle import Paddle
from score import Score

screen = Screen()

screen.setup(width=Design.screen_width, height=Design.screen_height)
screen.bgcolor(Design.bg_color)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle()
left_paddle.goto(Design.get_position_left_paddle())

right_paddle = Paddle()
right_paddle.goto(Design.get_position_right_paddle())

ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")


game_is_on = True

Design.draw_middle_line()

while game_is_on:
    screen.update()
    ball.move()


screen.exitonclick()
