from turtle import Turtle
class Line(Turtle):
    def __init__(self):
        super().__init__()
    def draw(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.setheading(270)
        self.width(5)

        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)