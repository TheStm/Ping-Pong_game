from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
score = ScoreBoard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(screen.exitonclick, "Escape")

game_is_on = True
while game_is_on:
    if ball.ycor() >= 282 or ball.ycor() <= -282:
        ball.bounce_vertically()

    if ball.xcor() >= 350:
        time.sleep(0.6)
        score.increase_l_score()
        ball.restart()
        screen.update()
        time.sleep(0.6)

    if ball.xcor() <= -350:
        time.sleep(0.6)
        score.increase_r_score()
        ball.restart()
        screen.update()
        time.sleep(0.6)

    if (ball.xcor() >= 335 and ball.distance(r_paddle) < 50) or (ball.xcor() <= -335 and ball.distance(l_paddle) < 50):
        ball.bounce_horizontally()
    time.sleep(ball.speed_move)
    ball.move()
    screen.update()

screen.exitonclick()