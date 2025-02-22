# Imports
from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Snake Class
class Snake():
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    # Body of Snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    # Adding Square to Snake Body
    def add_square(self, position):
        square = Turtle()
        square.shape("square")
        square.color("#50d969")
        square.penup()
        square.goto(position)
        self.segment.append(square)
        
    # Reset
    def reset(self):
        for old_snakes in self.segment:
            old_snakes.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    # Extending the Snake
    def extend_snake(self):
        self.add_square(self.segment[-1].position())

    # Animation of Snake
    def move_snake(self):
        for square_index in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[square_index - 1].xcor()
            new_y = self.segment[square_index - 1].ycor()
            self.segment[square_index].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)
        
    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        