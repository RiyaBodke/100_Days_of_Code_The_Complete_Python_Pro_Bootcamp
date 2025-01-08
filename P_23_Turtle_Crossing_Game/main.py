from turtle import Screen
from background import Background
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from time import sleep

CARS = []

screen = Screen()
screen.title("The Turtle Crossing Game")
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.tracer(0)

background = Background()
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

scoreboard.start()

game_is_on = True
while (game_is_on):
    
    sleep(0.1)
    screen.update()
    
    screen.listen()
    screen.onkey(player.move, "Up")
    
    car_manager.car_creator()
    car_manager.move()
    
    # Detect Collision with Car
    for shapes in car_manager.car:
            if shapes.distance(player) < 10:
                scoreboard.end()
                game_is_on = False
                break
            
    # Detect Car Passing Finish Line
    if player.ycor() > 380:
        player.start()
        scoreboard.update()
        car_manager.level_up()
    
screen.exitonclick()