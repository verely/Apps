from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)  # turn off animation, required manual update

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

ball = Ball()
scoreboard = Scoreboard()

scoreboard.write_score()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Handle collision with wall (top or bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Handle collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Handle right paddle missing ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()

    # Handle left paddle missing ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()


screen.exitonclick()
