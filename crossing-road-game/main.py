import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.car_movement()

    screen.onkey(player.go_up, "Up")
    
    #Detect collisions
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #Detect level up
    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.go_to_start()
        car_manager.increase_car_speed()
        
screen.exitonclick()
