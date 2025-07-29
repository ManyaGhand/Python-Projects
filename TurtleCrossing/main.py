import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:

    car_manager.car_movement()
    car_manager.create_cars()
    time.sleep(0.1)
    screen.update()

    #Detect collision with car.
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect a successful crossing.
    if player.successful():
        player.goto_start()
        car_manager.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()
