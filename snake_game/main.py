from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_is_paused = False


def pause_game():
    global game_is_paused
    game_is_paused = not game_is_paused


def exit_game():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)  # no screen updates

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(pause_game, "p")
screen.onkey(exit_game, "q")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.4)

    if game_is_paused:
        pass
    else:
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # detect collision with wall
        if snake.head.xcor() < -290 or snake.head.xcor() > 290 or \
                snake.head.ycor() < -290 or snake.head.ycor() > 290:
            scoreboard.game_over()
            game_is_on = False

        # Detect collision with tail.
        # for segment in snake.segments:
        #     if segment == snake.head:
        #         pass
        #     elif snake.head.distance(segment) < 10:
        #         game_is_on = False
        #         scoreboard.game_over()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
