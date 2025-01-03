# Imports
from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

# Class ScoreBoard
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER!", align = ALIGNMENT, font = FONT)
        
    def update_score(self):
        self.write(f"Score = {self.score}", align = ALIGNMENT, font = FONT)
