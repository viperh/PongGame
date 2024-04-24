from turtle import Turtle


class Design:
    font = ("Arial", 24, "normal")
    bg_color = "black"
    paddle_base_shape = "square"
    ball_shape = "circle"
    paddle_color = "white"
    ball_color = "white"
    score_color = "white"
    start_score = 0
    screen_width = 800
    screen_height = 600
    paddle_stretch_wid = 5
    paddle_stretch_len = 1

    base_paddle_position = screen_width // 2 - 20

    @classmethod
    def get_position_right_paddle(self):
        return self.base_paddle_position, 0

    @classmethod
    def get_position_left_paddle(self):
        return -self.base_paddle_position, 0

    @classmethod
    def draw_middle_line(self):
        t = Turtle()
        t.color("white")
        t.speed("fastest")
        t.hideturtle()
        t.penup()
        t.goto(0, Design.screen_height // 2)
        t.setheading(270)

        dash_length = self.screen_height // 20

        for _ in range(10):
            t.pendown()
            t.forward(dash_length)
            t.penup()
            t.forward(dash_length)
