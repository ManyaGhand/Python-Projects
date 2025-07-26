from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.goto(0 , 270)
        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align = "center",font = ("Courier", 70 ,"normal") )
        self.goto(100 , 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 70, "normal"))


    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()