from art import logo
import os
from time import sleep

water  = 1000
milk   = 1000
coffee = 500
money  = 3.00

cost = 0.00
open = True

def clear():
    """A function to clear the console"""
    
    # For Windows :
    if os.name == "nt":
        os.system("cls")
    # For Linux & Apple:
    else:
        os.system("clear")

def report():
    """Function to print the contents of the report"""
    
    print(f"\nWater = ", water, "ml\nMilk = ", milk, "ml\nCoffee = ", coffee, "g\nMoney = $", money, "\n")

def money_calc(required):
    """Function to handle the money"""
    
    global money
    # Asking money from the user:
    print("\nPlease insert coins 🪙 :")
    try:
        quarters = int(input("Quarters :"))
    except ValueError:
        print("Enter a valid currency 🪙. Just use numbers.")
        quarters = int(input("Quarters :"))
    try:
        dimes = int(input("Dimes :"))
    except ValueError:
        print("Enter a valid currency 🪙. Just use numbers.")
        dimes = int(input("Dimes :"))
    try:
        nickles = int(input("Nickels :"))
    except ValueError:
        print("Enter a valid currency 🪙. Just use numbers.")
        nickles = int(input("Nickels :"))
    try:
        pennies = int(input("Pennies :"))
    except ValueError:
        print("Enter a valid currency 🪙. Just use numbers.")
        pennies = int(input("Pennies :"))
        
    # Calculating money:
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    
    # Checking the total:
    if(total < required): # Less money 
        print("\nSorry, thats not enough money. Please collect your refund.")
        print("🪙🪙🪙🪙🪙")
        signal = "red"
    elif(total > required): # More money
        extra = total - required
        extra = round(extra, 2)
        print(f"\nHere are {extra} dollars in exchange.")
        print("🪙🪙🪙🪙🪙")
        signal = "green"
        money += required
    elif(total == required): # Equal money
        money += required
        signal = "green"
        
    return signal

def espresso():
    
    # Deducting used material from the report
    global water, coffee, money
    if(water < 50 or coffee < 18):
        print("Sorry, there aren't enough ingredients. Try after sometime. Here is your refund")
        print("🪙🪙🪙🪙🪙")
        money -= 1.50
    else:
        water -= 50
        coffee -= 18
        print("Here is your Espresso ☕! Have a nice day!")

def latte():
    
    # Deducting used material from the report
    global water, coffee, milk, money
    if(water < 200 or coffee < 24 or milk < 150):
        print("Sorry, there aren't enough ingredients. Try after sometime. Here is your refund")
        print("🪙🪙🪙🪙🪙")
        money -= 2.50
    else:
        water -= 200
        milk -= 150
        coffee -= 24
        print("Here is your Latte ☕! Have a nice day!")

def cappuccino():
    # Deducting used material from the report
    global water, coffee, milk, money
    if(water < 250 or coffee < 24 or milk < 100):
        print("Sorry, there aren't enough ingredients. Try after sometime. Here is your refund")
        print("🪙🪙🪙🪙🪙")
        money -= 2.50
    else:
        water -= 250
        milk -= 100
        coffee -= 24
        print("Here is your Cappuccino ☕! Have a nice day!")

def off():
    off = True
    while(off):
        clear()
        print(logo)
        t = input("The System is under maintenance. Please wait\n")
        if(t == "on" or t== "on " or t=="On" or t == "On "):
            off = False

def refill():
    global milk, water, money, coffee
    print("\nRefill ingredients:")
    print("Water : ", water)
    water += int(input("Add : "))
    print("Milk : ", milk)
    milk += int(input("Add : "))
    print("Coffee : ", coffee)
    coffee += int(input("Coffee : "))
    
    withdraw = input("Want to withdraw cash (Yes/No) : ")
    if(withdraw == "Yes" or withdraw == "yes"):
        passcode = "ilovecoffee"
        ask_passcode = input("Enter password : ")
        if(password != ask_passcode):
            print("Wrong Password! You cant withdraw money as you are not authorised!")
        elif(password == ask_passcode):
            print("Total : ",money)
            cash = int(input("Withdraw : "))
            while(cash > money):
                print("There isn't sufficient money in the machine. Enter appropriate amount")
                cash = int(input("Withdraw : "))
            money -= cash
            print("New total : ",money)
            print("Refilled Ingredients and Withdrawed Cash!")
        report()
    else:
        print("Refilled Ingredients!")
        report()

def coffee_machine():
    requirement = input("What would you like ? (espresso/latte/cappuccino) : ")
    global cost
    if(requirement == "report" or requirement == "Report" or requirement == "report " or requirement == "Report "):
        report()
        
    elif (requirement == "espresso" or requirement == "Espresso" or requirement == "espresso " or requirement == "Espresso "):
        cost = 1.50
        signal = money_calc(cost)
        if signal == "green":
            espresso()
        
    elif (requirement == "latte" or requirement == "Latte" or requirement == "latte " or requirement == "Latte "):
        cost = 2.50
        signal = money_calc(cost)
        if signal == "green":
            latte()
        
    elif (requirement == "cappuccino" or requirement == "Cappuccino" or requirement == "cappuccino " or requirement == "Cappuccino "):
        cost = 3.00
        signal = money_calc(cost)
        if signal == "green":
            cappuccino()
        
    elif (requirement == "off" or requirement == "Off" or requirement =="off " or requirement == "Off "):
        off()
        
    elif (requirement == "refill"):
        refill()
    
    elif (requirement == "close"):
        print("The coffee machine is closed for today.")
        global open
        open = False
        
    else:
        print("You have entered an invalid choice. Please enter a valid option.")
        

while(open):
    
    clear()
    print(logo)
    coffee_machine()
    sleep(3)

