# Imports
from turtle import Turtle

# Constants
WIDTH_RATIO = 5
HEIGHT_RATIO = 1
Y_POSITION = 0

# Class Paddle
class Paddle(Turtle):
    
    def __init__(self, x):
        super().__init__()
        self.X_POSITION = x
        self.shape("square")
        self.shapesize(stretch_wid = WIDTH_RATIO, stretch_len = HEIGHT_RATIO)
        self.penup()
        self.color("white")
        self.setpos(self.X_POSITION, 0)
        
    def move_up(self):
        new_y = self.ycor() + 20
        self.setpos(self.X_POSITION, new_y)
        
    def move_down(self):
        new_y = self.ycor() - 20
        self.setpos(self.X_POSITION, new_y)
        