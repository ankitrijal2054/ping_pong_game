RIGHT_COR = (375, 0)
LEFT_COR = (-375, 0)

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(RIGHT_COR)
l_paddle = Paddle(LEFT_COR)
ball = Ball()

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


screen.exitonclick()