
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= "center", font= ("Arial", 20 , "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER." ,align= "center", font= ("Arial", 20 , "normal") )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
