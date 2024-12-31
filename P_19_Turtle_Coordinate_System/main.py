from turtle import Turtle, Screen
from random import randint

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")
user_bet = user_bet.lower()
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [120, 80, 40, 0, -40, -80]
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y = y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True
    
while is_race_on:
        
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You lost! The {winning_turtle} turtle is the winner!")
        
        random_distance = randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()