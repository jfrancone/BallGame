from turtle import Turtle

STYLE= ('Rog Fonts', 15, 'italic')
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self, paddle, position):
        super().__init__()
        self.paddle_score = 0
        self.paddle = paddle
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(position)
        self.print_score()

    def print_score(self):
        self.write(f"{self.paddle.username}: {self.paddle_score}", align = ALIGNMENT, font = STYLE)

    def add_point(self):
        self.paddle_score += 1
        self.clear()
        self.print_score()