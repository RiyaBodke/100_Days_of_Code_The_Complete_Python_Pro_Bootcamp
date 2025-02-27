import turtle
from analysis import states_list, state_info, save_states
from time import sleep

screen = turtle.Screen()                            # Turtle Screen
screen.bgcolor("black")
screen.title("U.S. States Game")

image = "blank_states_img.gif"                      # Path to Image

screen.addshape(image)
turtle.shape(image)

guessed_states = []

# To get Co-ordinate values of States :
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

while len(guessed_states) < 50:                         # Loop to run the game
    
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt= "What's another state's name?" )   # Getting User Answer
    answer_state = answer_state.title()                 # Converting User Answer to Title Case

    if answer_state == "Exit":                          # Condition to Stop the Game
        break
    
    else:
        
        if answer_state in states_list:                 # Checking if User's Answer is Correct
            
            if answer_state in guessed_states:          # If State is guessed Already
                tl = turtle.Turtle()
                tl.hideturtle()
                tl.color("red")
                tl.penup()
                coor = state_info(answer_state)
                tl.goto(coor[0], coor[1] - 10)
                tl.write("Already Guessed !", align='center', font=('Arial', 8, 'bold'))
                sleep(1)
                tl.clear()
                
            else :                                      # If State is not guessed Previously
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                coor = state_info(answer_state)
                t.goto(coor[0], coor[1])
                t.write(answer_state, align='center', font=('Arial', 8, 'bold'))
                guessed_states.append(answer_state)

if len(guessed_states) == 50:
    f = turtle.Turtle()
    f.hideturtle()
    f.color("red")
    f.penup()
    f.goto(0, 250)
    f.write("Congratulations Genius ! You have guessed all states !", align='center', font=('Arial', 18, 'bold'))
    sleep(10)

else:
    
    missing_states = [state for state in state_list if state not in guessed_states]    # List for Missing States (Using list comprehension)
    
    # Alternate code for above line(without using list comprehension)
    # missing = []
    # for state in states_list:                           # Calculating Missing States
    #     if state not in guessed_states:
    #         missing.append(state)
    # missing_states = pd.DataFrame(missing)
    
    save_states(missing_states, "missing_states.csv")   # Saving Missing States in a CSV files
