# Extracting colors from imag.jpeg using colorgram

# import colorgram # A Python library used to extract colors from an image

# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 40)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

# Final color_list of colors values in rgb tuples (eliminating white colors) -
color_list = [(29, 41, 60), (49, 92, 143), (145, 81, 44), (170, 14, 28), (160, 56, 87), (227, 154, 8), (209, 162, 105), (235, 217, 75), (66, 30, 43), (37, 142, 47), (222, 225, 4), (48, 36, 30), (46, 47, 96), (95, 193, 168), (120, 161, 172), (19, 54, 47), (243, 89, 22), (161, 16, 13), (18, 97, 45), (212, 58, 79), (49, 169, 80), (189, 146, 159), (231, 173, 186), (226, 177, 168), (45, 153, 195), (160, 212, 184), (74, 77, 43), (116, 122, 156), (20, 74, 105), (184, 189, 203)]

from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)
def random_color():
    return (choice(color_list))

timmy_the_turtle = Turtle()
screen = Screen()

timmy_the_turtle.hideturtle()
timmy_the_turtle.speed(200)
timmy_the_turtle.penup()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(250)
timmy_the_turtle.setheading(0)
timmy_the_turtle.pendown()

for i in range(10):
    for j in range(10):
        timmy_the_turtle.dot(20, random_color())
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
        timmy_the_turtle.pendown()
    timmy_the_turtle.penup()
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(180)
    timmy_the_turtle.forward(500)
    timmy_the_turtle.setheading(0)
    timmy_the_turtle.pendown()

screen.exitonclick()