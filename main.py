RIGHT_COR = (375, 0)
LEFT_COR = (-375, 0)

from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(RIGHT_COR)
l_paddle = Paddle(LEFT_COR)

game_is_on = True

while game_is_on:
    screen.listen()
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.update()

screen.exitonclick()