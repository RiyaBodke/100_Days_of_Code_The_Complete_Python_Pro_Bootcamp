#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

choice = input("Would you like random order of characters in your passsword ?\nIf yes press y or if no press n\n")
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
if choice == "n" :
  password= ""

  for i in range(0,nr_letters) :
    l = random.choice(letters)
    password += l
  
  for j in range(0,nr_symbols):
    s = random.choice(symbols)  
    password += s
  
  
  for k in range(0,nr_numbers):
    n = random.choice(numbers)  
    password += n
  
  print("Here is your password: ", password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
elif choice == "y" :
  password = []
  for i in range(0,nr_letters) :
    l = random.choice(letters)
    password += l
  
  for j in range(0,nr_symbols):
    s = random.choice(symbols)  
    password += s
  
  for k in range(0,nr_numbers):
    n = random.choice(numbers)  
    password += n
  
  random.shuffle(password)
  
  passcode = ""
  for i in password:
    passcode += i
  
  print("Here is your password: ", passcode)

else:
  print("Press a valid option")
  exit()

print("\n\n\nSafety tip :\nUsing the same password leaves you and your information vulnerable to financial and identity theft , so it’s important to use a unique one for each of your accounts.\nStay Safe!")