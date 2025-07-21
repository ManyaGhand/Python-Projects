from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)

is_race_on=False
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle do you think will win the race?")


colors=["red", "blue", "purple" ,"green", "orange" ,"yellow" ]
y_positions=[ -70, 50, -40, 80, -10, 20]
all_turtles=[]


for turtle_index in range(0, 6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x = -230, y= y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color =  turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your {winning_color} turtle won.")
            else:
                print(f"You lose, {winning_color} turtle won.")
        random_number=random.randint(0,10)
        turtle.forward(random_number)

screen.exitonclick()