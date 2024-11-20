#Basic Calculator with logo
from art import logo

def add(a, b):
  """Adds 2 numbers"""
  return a+b

def subtract(a, b):
  """Subtracts 2 numbers"""
  return a-b

def multiply(a, b):
  """Multiplies 2 numbers"""
  return a*b

def divide(a, b):
  """Divides 2 numbers"""
  return a/b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  """Calculates the result of a mathematical operation by starting a new calculation"""
  a = float(input("What\'s the first number?: "))
  for symbol in operations:
    print(symbol)
  choice = True
  
  while (choice):
    flag = True
    while(flag):
      operation_symbol = input("Pick an operation : ")
      if operation_symbol not in operations:
        print("Invalid Operation")
      else :
        flag = False
    b = float(input("\nWhat\'s the second number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(a,b)
    print(f"\n{a} {operation_symbol} {b} = {first_answer}")
    
    continue_choice = input("\nType- \n\"y\" to continue\n\"n\" to start a new calculation\n\"e\" to exit : ")
    if (continue_choice == "c"):
      a = first_answer
      print("\n")
    elif(continue_choice == "n") :
      choice = False
      print("\n")
      calculator()
    else :
      choice = False
      print("\nBye")

calculator()
