# Imports
from turtle import Turtle
from random import randint , choice

# Constants
COLORS = ["red", "#e34f10", "green", "blue", "purple", "#04d1ce", "#b00767", "#5f687a"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Class
class CarManager:
    
    def __init__(self):
        self.car = []
        self.list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_creator()
    
    def car_creator(self):
        
        """ Function to create a car"""
        
        random_chance = randint(1,6)
        if random_chance == 1: 
        
            # Choosing random color for car
            color = choice(COLORS)
            
            x_cor = 500
            y_cor = randint(-325, 325)
            
            # Car Body
            square_cor = [(x_cor, y_cor), (x_cor-16, y_cor -16), (x_cor, y_cor -16), (x_cor+16, y_cor -16)]
            for i in square_cor:
                square = Turtle()
                square.penup()
                square.goto(i)
                square.color(color)
                square.shape("square")
                square.shapesize(0.8, 0.8)
                self.car.append(square)
                
            triangle_x_cor = [x_cor-8, x_cor+8]
            for i in triangle_x_cor:
                triangle = Turtle()
                triangle.penup()
                triangle.color(color)
                triangle.shape("triangle")
                triangle.shapesize(0.9, 0.9)
                triangle.right(30)
                triangle.goto(i, y_cor-2)
                self.list.append(triangle)
                
            # Car Windiws
            windows_cor = [(x_cor-4.5, y_cor), (x_cor+4.5, y_cor)]
            for i in windows_cor:
                windows = Turtle()
                windows.penup()
                windows.goto(i)
                windows.color("white")
                windows.shape("square")
                windows.shapesize(0.35, 0.3)
                self.car.append(windows)
                
            triangle_windows_x_cor = [x_cor-7.5, x_cor+7.5]
            for i in triangle_windows_x_cor:
                triangle_windows = Turtle()
                triangle_windows.penup()
                triangle_windows.color("white")
                triangle_windows.shape("triangle")
                triangle_windows.shapesize(0.39, 0.39)
                triangle_windows.right(30)
                triangle_windows.goto(i, y_cor-1.4)
                self.list.append(triangle_windows)
                
            handle_x_cor = [x_cor-4]
            for i in handle_x_cor:
                handle = Turtle()
                handle.penup()
                handle.color("white")
                handle.shape("square")
                handle.shapesize(0.05, 0.2)
                handle.goto(i, y_cor-8)
                self.car.append(handle)
                
            headlights_x_cor = [x_cor-26, x_cor+26]
            for i in headlights_x_cor:
                headlights = Turtle()
                headlights.penup()
                headlights.color("#f5d442")
                headlights.shape("square")
                headlights.shapesize(0.2, 0.21)
                headlights.goto(i, y_cor-19)
                self.car.append(headlights)
                
            wheels_x_cor = [x_cor-16, x_cor+16]
            for i in wheels_x_cor:    
                wheels = Turtle()
                wheels.penup()
                wheels.color(color)
                wheels.shape("circle")
                wheels.shapesize(0.4, 0.4)
                wheels.goto(i, y_cor-25)
                self.car.append(wheels)
                
            inner_wheels_x_cor = [x_cor-16, x_cor+16]
            for i in inner_wheels_x_cor: 
                inner_wheels = Turtle()
                inner_wheels.penup()
                inner_wheels.color("white")
                inner_wheels.shape("circle")
                inner_wheels.shapesize(0.1, 0.1)
                inner_wheels.goto(i, y_cor-25)
                self.car.append(inner_wheels)
                
            
    
    def move(self):
        
        """ Function to move a car"""
        
        for shape in self.car:
            shape.backward(self.car_speed)
        for tr in self.list :
            tr.right(-30)
            tr.backward(self.car_speed)
            tr.right(30)
            
    def level_up(self):
        
        """ Function to speed up when the level changes"""
        
        self.car_speed += MOVE_INCREMENT

