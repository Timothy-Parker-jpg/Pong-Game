from turtle import Turtle
from ball import BORDER_DIMENSIONS_X

class Score_Board(Turtle):
    def __init__(self):
        self.player2 = 0
        self.player1 = 0
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-BORDER_DIMENSIONS_X - 50, 0)
        self.write(f"Score: {self.player1}")
        self.goto(BORDER_DIMENSIONS_X + 20, 0)
        self.write(f"Score: {self.player2}")


    def score(self, ball):
        if ball.xcor() <= -BORDER_DIMENSIONS_X:
            self.player2 += 1
            ball.home()
            self.write_score()
            ball.xcordinate *= -1
        elif ball.xcor() >= BORDER_DIMENSIONS_X:
            self.player1 += 1
            ball.home()
            self.write_score()
            ball.xcordinate *= -1

    def win_condition(self):
        if self.player1 == 10 or self.player2 == 10:
            self.goto(-60, 0)
            self.pendown()
            self.color('red')
            self.write(f"YOU LOSE", font=("Arial", 20, "normal"))
            return False
        else:
            return True