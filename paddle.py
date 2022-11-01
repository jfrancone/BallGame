from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position, player_num):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.player_num = player_num
        self.shapesize(stretch_len = .5, stretch_wid = 4) # 80 x 10
        self.ht()
        self.penup()
        self.goto(position)
        self.st()
        self.speed("fastest")
        self.username = f"Player {player_num}"

    def check_top_border(self):
        if (self.ycor() > 240):
            at_border = True
        else:
            at_border = False

        return at_border

    def check_bot_border(self):
        if (self.ycor() < -240):
            at_border = True
        else:
            at_border = False

        return at_border

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        at_border = self.check_top_border()
        if not at_border:
            x = self.xcor()
            new_y = ((self.ycor()) + 10)
            self.goto(x, new_y)

    def down(self):
        at_border = self.check_bot_border()
        if not at_border:
            x = self.xcor()
            new_y = ((self.ycor()) - 10)
            self.goto(x, new_y)

# class AI_Paddle(Paddle):

#     def __init__(self, ball):
#         super().__init__(position, player_num)
#         self.username ="Computer"
#         self.ball = ball
        
#     def detect_ball(self):
#         if self.ball.position()