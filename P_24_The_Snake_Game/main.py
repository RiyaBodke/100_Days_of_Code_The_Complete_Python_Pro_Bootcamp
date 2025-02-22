# Imports
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen
import time

# Screen Settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# Create a snake - local object for class "Snake"
snake = Snake()

# Create food - local object for class "Food"
food = Food()

# Display scoreboard - local object for class "ScoreBoard"
scoreboard = ScoreBoard()

# Move snake wrt keys
screen.listen()

screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

# Turn game on
game_is_on = True

while game_is_on :
    
    screen.update()
    time.sleep(0.1)
    
    # Animate Snake
    snake.move_snake()
    
    # Detect collision with food:
    if snake.head.distance(food) < 15:
        snake.extend_snake()
        food.refresh()
        scoreboard.add_score()
        
    # Detect collision with food:
    if (snake.head.xcor() > 299 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()
        
    # Detect collision with tail:
    for square in snake.segment[1::] : 
        if snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()