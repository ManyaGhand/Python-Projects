from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.goto(position)


    def go_up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)


    def go_down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)
