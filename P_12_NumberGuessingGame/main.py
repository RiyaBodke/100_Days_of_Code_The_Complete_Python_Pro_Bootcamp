# Imports
from art import logo
import random
import time



# Introduction 
print(logo)
time.sleep(1)
print("Welcome to number guessing game!")
time.sleep(1)
print("I'm thinking of a number between 1 and 100.")
time.sleep(1)

# Generating answer
answer = random.randint(1,100)
attempts = 0

# Deciding number of guess attempts
incorrect_input = True
while(incorrect_input):
  level = str(input("Choose a difficulty level. Type \"easy\" or \"hard\": "))
  if (level == "easy" or level == "Easy"):
    attempts = 10
    incorrect_input = False
  elif (level == "hard" or level == "Hard"):
    attempts = 5
    incorrect_input = False
  else:
    print("Enter a proper choice")

# Logic behind the program
guess = 101
while(guess != answer and attempts>0) :
  print(f"You have {attempts} attempts to guess the number.")
  guess = int(input("Make a guess: "))
  if(attempts != 1):
    if (guess > answer):
        print("Too high!\nGuess again.")
    elif(guess < answer):
        print("Too low!\nGuess again.")
    else:
        print(f"You got it! The answer was {answer}!")
  if(attempts == 1):
    if(guess == answer):
        print(f"You got it! The answer was {answer}!")
    else:
        print("You have run out of guesses!\nTry again by re-running the program")
  attempts -= 1
