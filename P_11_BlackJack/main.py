############### Our Blackjack House Rules #####################

## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## The cards in the list have an equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo  # Importing logo from art.py
import random  # Importing random module
import os  # Importing os module
import time  # Importing time module

cards = [
    "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "K♠",
    "Q♠", "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥",
    "K♥", "Q♥", "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣",
    "J♣", "K♣", "Q♣", "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦",
    "10♦", "J♦", "K♦", "Q♦"
]  # List containing card deck

# Variables to track user and dealer score
user_score = 0
dealer_score = 0


def create_card(x):
  # This function takes list - "cards" and generates ASCII style card template for visual representation
  n = " "
  s = " "
  h = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]
  for i in h:
    if i in x:
      n = i
      break
  j = ["♠", "♥", "♣", "♦"]
  for k in j:
    if k in x:
      s = k
      break
  template = ""

  # Adjusting unequal spacing
  if n == "10":
    template = f"""
   _____
  |{n}   | 
  |     |
  |  {s}  |
  |     |
  |___{n}|
  
    """
  else:
    template = f"""
   _____
  |{n}    | 
  |     |
  |  {s}  |
  |     |
  |____{n}|

    """
  return template


def card(player):
  # This function selects a random card for list - "cards" and assigns it to the player - either the user or dealer
  c = random.choice(cards)
  player.append(c)
  return player


def score(og_list, src):
  # This function takes a list of cards and calculates the score of the cards
  k = []
  list = og_list.copy()
  for i in list:
    if "A" in i:
      k.append(11)
    elif ("K" in i or "J" in i or "Q" in i or "10" in i):
      k.append(10)
    elif ("9" in i):
      k.append(9)
    elif ("8" in i):
      k.append(8)
    elif ("7" in i):
      k.append(7)
    elif ("6" in i):
      k.append(6)
    elif ("5" in i):
      k.append(5)
    elif ("4" in i):
      k.append(4)
    elif ("3" in i):
      k.append(3)
    elif ("2" in i):
      k.append(2)

  for i in k:
    src += i

  if (11 in k and src > 21):
    src -= 10
  return src


game = True


def play():
  # User Card allocation and printing
  print(logo)
  user = []
  card(user)
  card(user)
  print("User : ")
  print("\nScore = ", score(user, user_score))
  print(create_card(user[0]))
  print(create_card(user[1]))

  # Dealer Card allocation and printing
  dealer = []
  print("Dealer : ")
  card(dealer)
  print(create_card(dealer[0]))

  # User's blackjack
  user_den = True
  while (user_den):
    if (score(user, user_score) == 21):
      print("BlackJack!")
      user_den = False
      break
    else:
      print("Its your turn!\n\n")
      choice = int(input("\nChoose : \n1. Hit \n2. Stand \n\nUser : "))

      if (choice != 1 and choice != 2):
        print("Enter a valid choice")
      elif (choice == 2):
        user_den = False
        break
      elif (choice == 1):
        os.system('clear')
        print(logo)
        card(user)
        print("User : ")
        print("\nScore = ", score(user, user_score))

      for i in user:
        print(create_card(i))

      print("Dealer :")
      print("\nScore =", score(dealer, dealer_score))
      for i in dealer:
        print(create_card(i))
      if (score(user, user_score) >= 21):

        play = False
        break

  final_user_score = score(user, user_score)
  os.system('clear')
  print(logo)

  if(final_user_score > 21):
    print("User : ")
    print("\nScore =", score(user, user_score))
    for i in user:
      print(create_card(i))
    card(dealer)
    print("\nDealer : ")
    print("\nScore : ", score(dealer, dealer_score))
    for i in dealer:
      print(create_card(i))
    time.sleep(2)
    os.system('clear')
    print(logo)

  else:
    print("Its dealer's turn!\n\n")
  
    while (score(dealer, dealer_score) < 17):
      card(dealer)
      print("User : ")
      print("\nScore =", score(user, user_score))
      for i in user:
        print(create_card(i))
      print("\nDealer : ")
      print("\nScore : ", score(dealer, dealer_score))
      for i in dealer:
        print(create_card(i))
      time.sleep(2)
      os.system('clear')
      print(logo)

  print("And ...");time.sleep(0.1);print("Resuts ...");time.sleep(0.1);print("Are ...\n\n");time.sleep(0.1)
  print("User : ")
  print("\nScore =", score(user, user_score))
  for i in user:
    print(create_card(i))

  print("\nDealer : ")
  print("\nScore : ", score(dealer, dealer_score))
  for i in dealer:
    print(create_card(i))
  
  
  final_dealer_score = score(dealer, dealer_score)

  if (final_user_score <= 21):
    if (final_dealer_score <= 21):
      if (final_user_score == final_dealer_score):
        print("\nBusted! It's a tie!")
      elif (final_user_score > final_dealer_score):
        print("\nUser wins!")
      else:
        print("\nDealer wins!")
    else:
      print("\nUser wins!")
  else:
    if (final_dealer_score <= 21):
      print("\nDealer wins!")
    else:
      print("\nBusted! It's a tie!")

  another_game = input(
      "\nEnter E to exit the game or any other key to play another round\nUser : ")

  if (another_game == "E" or another_game == "e"):
    print("Thank you for playing!")
    game = False
    exit()

  else:
    os.system('clear')
    play()


while (game):

  #Initializing
  print(logo)
  time.sleep(1)
  print("Welcome to the Golden Ace Casino!")
  time.sleep(1)
  print("Ready for a game ?")
  time.sleep(1)
  print("Lets go...")
  time.sleep(1.8)
  os.system('clear')
  play()
