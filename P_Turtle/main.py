from turtle import Turtle, Screen, colormode
from random import randint,choice

timmy_the_turtle = Turtle() # Turtle object is created
screen = Screen()           # Screen is created

# Comment out the required Challenge code. Also refer Python Turtle Documentation.

# Challenge 1: Draw a Square

# timmy_the_turtle.forward(100) # Moves Forward 100 px
# timmy_the_turtle.right(90)    # Turns Right 90 degrees
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# Challenge 2: Draw a Dashed Line

# i = 0
# while(i<50):
#     timmy_the_turtle.forward(3)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(3)
#     timmy_the_turtle.pendown()
#     i += 1

# Challenge 3: Drawing different Shapes

# color = ["violet", "indigo", "blue", "green", "yellow", "orange", "red", "pink", "black"]
# c=0
# for n in range(3,12):
#     for i in range(n):
#         timmy_the_turtle.forward(50)
#         timmy_the_turtle.right(360/n)
#     timmy_the_turtle.pencolor(color[c])
#     c += 1

# Challenge 4: Generate a random walk

# timmy_the_turtle.speed(200)  
# directions = [0, 90, 180, 270]
# colormode(255)

# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)

# for i in range(200):
#     timmy_the_turtle.pensize(10)
#     timmy_the_turtle.forward(50)
#     timmy_the_turtle.setheading(choice(directions))
#     timmy_the_turtle.pencolor(random_color())

# Challenge 5: Draw a Spirograph

# timmy_the_turtle.speed(200)
# colormode(255)

# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)

# def spirograph(size_of_gap):
    
#     for i in range(int(360/size_of_gap)):
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
#         timmy_the_turtle.pencolor(random_color())

# spirograph(6)

screen.exitonclick() # Screen disappears on click
