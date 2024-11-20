rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

usr_choice=input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
c=int(usr_choice)

if c>2 :
  print("Invalid Choice !!! Choose 0 for Rock, 1 for Paper or 2 for Scissors")
  exit()

else :
    if c==0 :
      print(rock)
    elif c==1 :
      print(paper)
    elif c==2 :
      print(scissors)

print("Computer choose:")

options = [rock, paper, scissors]
comp_choice = random.choice(options)

print(comp_choice)

if c == 0 :
  if comp_choice == rock :
    print("It's a draw")

  if comp_choice == paper :
    print("You lose")

  if comp_choice == scissors :
    print("You win")

elif c == 1 :
  if comp_choice == paper :
    print("It's a draw")

  if comp_choice == rock :
    print("You win")

  if comp_choice == scissors :
    print("You lose")

elif c==2 :
  if comp_choice == scissors :
    print("It's a draw")

  if comp_choice == rock :
    print("You lose")

  if comp_choice == paper :
    print("You win")
    