# Imports
from turtle import Turtle

# Constants
STARTING_POSITION = (0, -400)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 450


class Player(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.color("#4fe878")
        self.penup()
        self.start()
        self.setheading(90)
        self.speed("fastest")
    
    def move(self) :
        self.forward(MOVE_DISTANCE)
        
    def start(self) :
        self.goto(STARTING_POSITION)