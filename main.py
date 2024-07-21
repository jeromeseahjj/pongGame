from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        # Bounce
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 \
        or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.reset_position()

    # Detect L paddle misses
    if ball.ycor() < -380:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.reset_position()


screen.exitonclick()