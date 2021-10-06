from turtle import Turtle

BORDER_DIMENSIONS_X = 600
BORDER_DIMENSIONS_Y = 400


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.goto(-BORDER_DIMENSIONS_X, BORDER_DIMENSIONS_Y)
        self.pendown()
        self.goto(-BORDER_DIMENSIONS_X, -BORDER_DIMENSIONS_Y)
        self.goto(BORDER_DIMENSIONS_X, -BORDER_DIMENSIONS_Y)
        self.goto(BORDER_DIMENSIONS_X, BORDER_DIMENSIONS_Y)
        self.goto(-BORDER_DIMENSIONS_X, BORDER_DIMENSIONS_Y)
        self.goto(0, BORDER_DIMENSIONS_Y)
        self.goto(0, -BORDER_DIMENSIONS_Y)