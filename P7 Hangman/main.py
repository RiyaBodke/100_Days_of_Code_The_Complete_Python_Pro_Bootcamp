#Step 5

import os
import hangman_art
import hangman_words
import random


clear = lambda: os.system('cls')

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_letters = []

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

logo = hangman_art.logo
print(logo)


#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    
    while 5>3:
      guess = input("Guess a letter baby ◕‿↼ : ")
      guess.lower()
      if len(guess)==1:
        break
      print("Just a word dear ! Try again \n\n")
    
    clear()
      
    guessed_letters += guess
    
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
  
    
    if guessed_letters.count(guess) >= 2 :
      print(f"You have already guessed this letter. Your letter is {guess}")
    else :
      print(f"Your letter is {guess}\n")
      
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print("Wow ! You guessed a coreect letter ! Go for another one.\n")

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print("You guessed wrong letter. You lose a life\n")
        if lives == 0:
            end_of_game = True
            print("\nUh-oh! You lose.\n")
            print(f"The solution is {chosen_word}")
            end_of_game = True

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(f"You have {lives} lives\n")

    #Check if user has got all letters.
    
    if "_" not in display:
        end_of_game = True
        print("\nYay! You win.\n")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    
    stages = hangman_art.stages
    print(stages[lives])
