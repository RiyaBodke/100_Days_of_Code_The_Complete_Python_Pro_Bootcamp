from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard():
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.sb = Turtle()
        self.sb.hideturtle()
        self.sb.penup()
        self.sb.goto(-430, 390)
        self.sb.color("white")
        self.display()
        
    def display(self):
        self.sb.write(f"Score : {self.score}", False, "center", FONT)
        
    def update(self):
        self.sb.clear()
        self.score += 1
        self.display()
        
    def end(self):
        e = Turtle()
        e.color("red")
        e.write("GAME OVER", False, "center", FONT)
    
