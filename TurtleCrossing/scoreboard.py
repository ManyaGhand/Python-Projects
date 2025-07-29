from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.font = FONT
        self.penup()
        self.goto(0 , 260)
        self.update_level()
        self.increase_level()
        self.hideturtle()

    def update_level(self):
        self.write(f"Level: {self.level}", align="center", font = self.font)

    def increase_level(self):
        self.clear()
        self.update_level()
        self.level += 1

    def game_over(self):
        self.clear()
        self.write("GAME OVER.", align = "center", font = self.font)

