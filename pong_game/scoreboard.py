from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.color("white")
        self.left_score = 0
        self.right_score = 0

    def write_score(self):
        self.clear()
        self.write(arg=f"{self.left_score} : {self.right_score}", align="center", font=("currier", 60, "normal"))

    def increase_right_score(self):
        self.right_score += 1
        self.write_score()

    def increase_left_score(self):
        self.left_score += 1
        self.write_score()
