from turtle import Screen
from paddle import Paddle
from user_paddle import User_Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"

class Engine:

    def __init__(self):
        self.screen = self.create_screen()
        self.paddle_1 = Paddle(position = (-290, 0), player_num = 1)
        self.paddle_2 = Paddle(position = (280, 0), player_num = 2)
        self.ball = Ball()
        self.get_usernames()
        self.paddle1_scoreboard = Scoreboard(paddle = self.paddle_1, position = (-220, -280))
        self.paddle2_scoreboard = Scoreboard(paddle = self.paddle_2, position =(200, -280))


    def get_usernames(self):
        self.paddle_1.username = self.screen.textinput(title = "Username", prompt = "What is your username, Player 1?")
        self.paddle_2.username = self.screen.textinput(title = "Username", prompt = "What is your username, Player 2?")


    def create_screen(self):
        self.screen = Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor(SCREEN_COLOR)
        self.screen.title("Let me see that pong")
        self.screen.tracer(0)
        return self.screen


    def add_key_controls(self):
        self.screen.onkeypress(self.paddle_1.up, "w")
        self.screen.onkeypress(self.paddle_1.down, "s")
        self.screen.onkeypress(self.paddle_2.up, "Up")
        self.screen.onkeypress(self.paddle_2.down, "Down")
        self.screen.onkey(self.start_game, "space")


    def start_game(self):
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(.0000001)

            self.ball.move()

            # if (self.ball.distance(self.paddle_1) < 5) or (self.ball.distance(self.paddle_2) < 5):
            #     self.ball.bounce()
            if self.ball.xcor() > 270:
                if (self.ball.ycor() > (self.paddle_2.ycor() - 40)) and (self.ball.ycor() < (self.paddle_2.ycor() + 40)):
                    self.ball.bounce()

            if self.ball.xcor() < -280:
                if (self.ball.ycor() > (self.paddle_1.ycor() - 40)) and (self.ball.ycor() < (self.paddle_1.ycor() + 40)):
                    self.ball.bounce()

            if (self.ball.ycor() > 290) or (self.ball.ycor() < -290):
                self.ball.bounce()

            if self.ball.xcor() > 300:
                game_is_on = False
                self.paddle1_scoreboard.add_point()

            if self.ball.xcor() < -300:
                game_is_on = False
                self.paddle2_scoreboard.add_point()
        
        self.new_round()

    
    def new_round(self):
        self.paddle_1.penup()
        self.paddle_1.goto((-290, 0))
        self.paddle_2.penup()
        self.paddle_2.goto((280, 0))
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.get_start_dir()
        self.paddle1_scoreboard.print_score()
        self.paddle2_scoreboard.print_score()
        self.screen.update()
        self.screen.listen()
                


def main():
    game_is_on = False
    engine = Engine()
    engine.screen.listen()
    engine.add_key_controls()
    engine.start_game()



    engine.screen.exitonclick()
    