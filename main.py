RIGHT_COR = (375, 0)
LEFT_COR = (-375, 0)

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

line = Turtle()
line.pencolor("white")
line.penup()
line.hideturtle()
line.goto(0, 300)
line.right(90)
for i in range(0, 60):
    line.pendown()
    line.forward(5)
    line.penup()
    line.forward(5)

r_paddle = Paddle(RIGHT_COR)
l_paddle = Paddle(LEFT_COR)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with the wall
    ball.check_wall_collision()

    # detect collision with paddle
    if ball.xcor() > 350 and ball.distance(r_paddle) < 50 or ball.xcor() < -350 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # detect r_paddle missed
    if ball.xcor() > 380 #and ball.distance(r_paddle) > 50:
        score.increase_l_score()
        ball.center()
        ball.bounce_x()
        time.sleep(1)

    # detect l_paddle missed
    if ball.xcor() < -380 #and ball.distance(r_paddle) > 50:
        score.increase_r_score()
        ball.center()
        ball.bounce_x()
        time.sleep(1)

screen.exitonclick()