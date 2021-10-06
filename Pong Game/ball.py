from turtle import Turtle
from border import BORDER_DIMENSIONS_X, BORDER_DIMENSIONS_Y
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(.5, .5)
        self.setheading(90)
        self.speed(1)
        self.xcordinate = -1
        self.ycordinate = 1

    def move(self):
        new_xcor = self.xcor() + self.xcordinate
        new_ycor = self.ycor() + self.ycordinate
        self.goto(new_xcor, new_ycor)

    def bounce(self):
        if self.ycor() >= BORDER_DIMENSIONS_Y or self.ycor() <= -BORDER_DIMENSIONS_Y:
            self.ycordinate *= -1



    def paddle_collision(self, player1, player2):
        if self.distance(player1) < 25:
            self.xcordinate *= -1
        elif self.distance(player2) < 25:
            self.xcordinate *= -1
