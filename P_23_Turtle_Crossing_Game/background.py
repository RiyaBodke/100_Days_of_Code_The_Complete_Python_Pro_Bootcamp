from turtle import Turtle

class Background:
    
    def __init__(self):
        self.flag()
        self.race_line()
        
    def flag(self):
        
        triangle = Turtle()
        triangle.penup()
        triangle.shape("triangle")
        triangle.color("red")
        triangle.goto(460, 410)
        
        stick = Turtle()
        stick.penup()
        stick.shape("square")
        stick.color("white")
        stick.shapesize(2, 0.1)
        stick.goto(450, 400)
        
    def race_line(self):
        
        y = [-360, 370]
        for i in y:
            for n in range(-494, 510, 20):
                
                sq_red = Turtle()
                sq_red.penup()
                sq_red.shape("square")
                sq_red.color("red")
                sq_red.shapesize(1, 0.5)
                sq_red.goto(n,i)
                
                sq_white = Turtle()
                sq_white.penup()
                sq_white.shape("square")
                sq_white.color("white")
                sq_white.shapesize(1, 0.5)
                sq_white.goto(n+10,i)