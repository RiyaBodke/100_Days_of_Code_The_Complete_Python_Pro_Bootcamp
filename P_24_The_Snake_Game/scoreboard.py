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
        with open("data.txt") as hs :
            self.high_score = int(hs.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("GAME OVER!", align = ALIGNMENT, font = FONT)
    
    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode = "w") as hs :
                hs.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update_score()
        
    def update_score(self):
        self.write(f"Score = {self.score} High Score = {self.high_score}", align = ALIGNMENT, font = FONT)
