from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()

menu = Menu()

is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    elif choice in ["latte", "cappuccino", "espresso"]:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink) 
    else:
        print("Wrong Input")
