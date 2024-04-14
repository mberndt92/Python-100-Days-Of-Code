import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()

screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    # if player.ycor() >= 280:
    #     score.scored()
    time.sleep(0.1)
    screen.update()
    car_manager.tick()

    # Detect car collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()


    # Detect finish line
    if player.is_at_finish_line():
        player.go_to_start()
        score.scored()
        car_manager.speed_up()


screen.exitonclick()