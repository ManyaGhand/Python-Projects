from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.turtlesize(1, 2)
            new_car.penup()
            y_pos = random.randint(-250, 250)
            new_car.setx(300)
            new_car.sety(y_pos)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            self.cars.append(new_car)

    def car_movement(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
