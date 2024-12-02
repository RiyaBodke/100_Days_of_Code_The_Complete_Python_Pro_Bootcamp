from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

list = menu.get_items()

espresso = MenuItem("espresso", "50", "0", "18", "1.50")
latte = MenuItem("latte", "200", "150", "24", "2.50")
cappuccino = MenuItem("cappuccino", "250", "100", "24", "3.00")

game = True
while(game):
    user_choice = input(f"What would you like to drink ? ({list}) : ")
    if(user_choice == "report"):
        coffeemaker.report()
        moneymachine.report()
            
    elif(user_choice == "off"):
        print("Closing the machine for today !")
        game = False 
    
    else:
        drink = menu.find_drink(user_choice)
        if( drink != None):
            material = coffeemaker.is_resource_sufficient(drink)
            if(material == True):
                print("Great ! Insert coins now !")
                cost = drink.cost
                payment = moneymachine.make_payment(cost)
                
                if(payment == True):
                    coffeemaker.make_coffee(drink)