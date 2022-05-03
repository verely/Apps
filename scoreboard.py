from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(x=0, y=270)
        self.high_score = 0
        self.update_high_score()
        self.update_scoreboard()

    def update_high_score(self):
        try:
            with open("data.txt") as file:
                self.high_score = int(file.read())
        except (OSError, ValueError):
            with open("data.txt", "w") as file:
                file.write("0")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.high_score < self.score:
            with open("data.txt", "w") as file:
                file.write(str(self.score))

        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


