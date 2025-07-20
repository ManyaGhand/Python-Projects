import turtle as turtle_module
import random

timmy=turtle_module.Turtle()
turtle_module.colormode(255)

color_list = [ (1, 10, 30), (229, 235, 242), (239, 232, 238), (122, 95, 41), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136), (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7)]

timmy.ht()

timmy.penup()
timmy.setheading(210)
timmy.forward(325)
timmy.setheading(0)

timmy.speed("fastest")
number_of_dots=100

for dots in range(1, number_of_dots + 1):
    timmy.penup()
    timmy.forward(50)
    timmy.dot(20 ,random.choice(color_list) )

    if dots % 10 ==0:
        timmy.penup()
        timmy.setheading(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.setheading(0)



screen=turtle_module.Screen()
screen.exitonclick()