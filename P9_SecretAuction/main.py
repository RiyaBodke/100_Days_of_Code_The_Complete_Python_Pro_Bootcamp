from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
bidders = {}

print(logo)
print("Welcome to the Secret Auction Program.")

def winner_bidder(bidders_info):
  highest = 0
  for bidder in bidders:
    bidding_amount = bidders[bidder]
    if bidding_amount > highest :
      highest += bidding_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {highest}.\nCongratulations {winner}!")

while(5>3):
  name_of_bidder=input("What is your name?: ")
  bid_ =int(input("Now enter a complete bid-amount without floats.\nWhat's your bid? : ₹"))
  bidders[name_of_bidder] = bid_
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()
  if other_bidders == "no" :
    break
    
winner_bidder(bidders)

