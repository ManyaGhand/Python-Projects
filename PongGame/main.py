from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time


screen=Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(height = 600, width = 800)
screen.tracer(0)


r_paddle=Paddle((350, 0))
l_paddle=Paddle((-350, 0))
ball=Ball()
line=Line()
line.draw()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun= r_paddle.go_up, key= "Up")
screen.onkey(fun= r_paddle.go_down, key= "Down")
screen.onkey(fun= l_paddle.go_up, key= "w")
screen.onkey(fun= l_paddle.go_down, key= "s")

is_on = True

while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect the collision.
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with the paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    #Increases score only when the ball doesn't hit the paddle.

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()