from turtle import Turtle
import random

MOVE_DISTANCE = 2
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.get_start_dir()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def bounce(self):
        # if self.heading() == 0:
        #     self.setheading(LEFT)
        # else:
        #     self.setheading(RIGHT)
        new_angle = 0

        if self.heading() == 0:
            new_angle = 180
        elif self.heading() <= 180:
            if self.ycor() > 290:
                new_angle = 360 - self.heading()
                self.setheading(new_angle)
            elif (self.xcor() > 270) or (self.xcor() < -280):
                new_angle = 180 - self.heading()
                self.setheading(new_angle)
        elif self.heading() < 360:
            if self.ycor() < -290:
                new_angle = 360 - self.heading()
            elif (self.xcor() < -280) or (self.xcor() > 270):
                new_angle = ((360 - self.heading()) + 180)
        
        self.setheading(new_angle)


        # if self.heading() <= 180:
        #     new_heading = 180 - self.heading()
        #     self.setheading(new_heading)

        # if self.heading() > 180:
        #     new_heading = 180 + self.heading()
        #     if new_heading >= 360:
        #         heading = new_heading - 360
        #         self.setheading(heading)
        #     else:
        #         self.setheading(new_heading)

        #     self.setheading(new_heading)
 


    def get_start_dir(self):
        random_dir = random.randint(0, 360)
        self.setheading(random_dir)



    # def start(self):
    #     game_is_on = True
    #     while game_is_on:
    #         screen.update()
    #         time.sleep(.1)
    #         self.move()