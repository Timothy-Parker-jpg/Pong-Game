from turtle import Screen
import time
from paddle import Paddle
from border import Border
from ball import Ball
from score import Score_Board
screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

player1 = Paddle()
player2 = Paddle()
border = Border()
ball = Ball()
sb = Score_Board()

player1.player1()
player2.player2()
screen.onkeypress(player1.w, "w")
screen.onkeypress(player1.s, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    ball.bounce()
    player2.paddle_ai(ball)
    ball.paddle_collision(player1, player2)
    sb.score(ball)
    game_is_on = sb.win_condition()
border












screen.exitonclick()