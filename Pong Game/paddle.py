from turtle import Turtle
from border import BORDER_DIMENSIONS_Y

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(.5, 2.5)
        self.color("white")
        self.penup()
        self.setheading(90)

    def player1(self):
        self.goto(-530, 0)

    def player2(self):
        self.goto(530, 0)

    def w(self):
        self.setheading(90)
        if self.ycor() >= BORDER_DIMENSIONS_Y - 45:
            self.fd(0)
        else:
            self.fd(40)

    def s(self):
        self.setheading(270)
        if self.ycor() <= -BORDER_DIMENSIONS_Y + 45:
            self.fd(0)
        else:
            self.fd(40)
    def paddle_ai(self, ball):
        self.goto(530, ball.ycor())