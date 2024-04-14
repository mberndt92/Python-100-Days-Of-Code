
# OOP Coffee Machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
drink_names = menu.get_items()
money_machine = MoneyMachine()

def start_coffe_machine():
    while True:
        choice = input(f"What would you like to drink? ({drink_names}) \n")
        if choice == 'report':
            coffe_maker.report()
            money_machine.report()
            start_coffe_machine()

        drink = menu.find_drink(choice)
        if drink is None:
            exit()

        if coffe_maker.is_resource_sufficient(drink):
            print(f"Price: ${drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)


start_coffe_machine()