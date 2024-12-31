from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("classic")

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
def clear():
    tim.reset()
    tim.pensize()
    
def small_width():
    tim.pensize(1)

def medium_width():
    tim.pensize(5)
    
def large_width():
    tim.pensize(10)
    
def color_violet():
    tim.color("violet")
    
def color_indigo():
    tim.color("indigo")
    
def color_teal():
    tim.color("teal")
    
def color_green():
    tim.color("green")
    
def color_yellow():
    tim.color("yellow")
    
def color_orange():
    tim.color("orange")
    
def color_red():
    tim.color("red")
    
def color_black():
    tim.color("black")

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="b", fun=small_width)
screen.onkey(key="n", fun=medium_width)
screen.onkey(key="m", fun=large_width)
screen.onkey(key="v", fun=color_violet)
screen.onkey(key="i", fun=color_indigo)
screen.onkey(key="t", fun=color_teal)
screen.onkey(key="g", fun=color_green)
screen.onkey(key="y", fun=color_yellow)
screen.onkey(key="o", fun=color_orange)
screen.onkey(key="r", fun=color_red)
screen.onkey(key="f", fun=color_black)

screen.exitonclick()
