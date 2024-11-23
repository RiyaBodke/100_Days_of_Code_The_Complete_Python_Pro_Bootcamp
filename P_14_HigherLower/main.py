from game_data import data
from art import logo, vs
from random import randint
from time import sleep
import os

def clear():
    """Function to clear the console"""
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")

def random_personality():
    """To generate data of random personalities"""
    
    n = randint(0,114)
    name = data[n]["name"]
    insta_handle = data[n]["insta_handle"]
    follower_count = data[n]["follower_count"]
    country = data[n]["country"]
    description = data[n]["description"]
    
    info = f"{name}({insta_handle}), {description}, from {country}"
    person = [info, follower_count]
    
    return(person)

def animation():
    """Function for animation effect before result"""
    print(logo)
    print("Thinking .")
    sleep(1)
    clear()
    print(logo)
    print("Thinking ..")
    sleep(1)
    clear()
    print(logo)
    print("Thinking ...")
    sleep(1)

def result(i,j):
    """A function to return result of the quiz"""

    if (i > j):
        return "A"
    elif (j > i):
        return "B"

def game():
    """Algorithm for game"""
    
    score = 0   # Tracking Score of the user
    den = True  # Boolean Variable to implement conditions on the game
    
    while(den):
        
        a = random_personality()
        b = random_personality()
        
        print("\n\n\nCompare A : ", a[0])
        print(vs)
        print("Against B: ", b[0])
        print("\n\n\n")
        
        guessing = True

        while(guessing):
            guess = input("Who hast more instagram followers? Type A or B : ")
            if(guess == "A" or guess == "a" or guess == "A " or guess == "a "):
                guessing = False
            elif(guess == "B" or guess == "b" or guess == "B " or guess == "b "):
                guessing = False
            else:
                print("You have enterend an invalid value which not an option. Please try aggain.")

        
        answer = result(a[1], b[1])
        
        if(guess == answer):
            score +=1
            clear()
            animation()
            clear()
            print(logo)
            print("\nYou're Right!\nCurrent Score :", score)
            
        elif(guess != answer):
            
            cheering = ""
            if(score < 3):
                cheering = "Better luck next time bud!"
            elif(score >= 3 and score < 5):
                cheering = "Well tried!"
            elif(score >= 5 and score < 7):
                cheering = "Not bad huhh!"
            elif(score >= 7 and score < 9):
                cheering = "You are getting pro at this!"
            elif(score > 9):
                cheering = "Still a Champion!"
                
            clear()
            animation()
            clear()
            print(logo)
            print("\nSorry, that's a wrong answer! ",cheering,"\n\nFinal Score :", score)
            den = False
        
    

# Start of the program -

clear() # Clearing console screen

print(logo) 
sleep(1)

game() #Executing the trivia game
