# Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 10
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    },
}

coins = [0.01, 0.05, 0.10, 0.25]

water = 300
milk = 200
coffee = 100


def print_report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")


def refill_coffee():
    global coffee
    coffee = 100


def refill_milk():
    global milk
    milk = 200


def refill_water():
    global water
    water = 300


def verify_resources(choice):
    req_water = int(MENU[choice]["ingredients"].get("water", 0))
    req_milk = int(MENU[choice]["ingredients"].get("milk", 0))
    req_coffee = int(MENU[choice]["ingredients"].get("coffee", 0))

    if req_water > water:
        print(f"Not enough water. Got {water}, required: {req_water}")
        return False
    if req_milk > milk:
        print(f"Not enough milk. Got {milk}, required: {req_milk}")
        return False
    if req_coffee > coffee:
        print(f"Not enough coffee. Got {coffee}, required: {req_coffee}")
        return False
    return True


def adjust_resources(choice):
    global water
    global milk
    global coffee

    water -= MENU[choice]['ingredients']['water']
    milk -= MENU[choice]['ingredients'].get('milk', 0)
    coffee -= MENU[choice]['ingredients']['coffee']


def process_choice(choice):
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        result = verify_resources(choice)
        if not result:
            return None
        else:
            return True

    elif choice == 'report':
        print_report()
    elif choice == 'refill':
        refill_water()
        refill_milk()
        refill_coffee()
        print_report()


def process_payment(choice):
    print("Please insert coins.")
    quarters = 0.25 * int(input("How many quarters? "))
    dimes = 0.1 * int(input("How many dimes? "))
    nickles = 0.05 * int(input("How many nickles? "))
    pennies = 0.01 * int(input("How many pennies? "))

    req_coins = float(MENU[choice]['cost'])
    given_coins = quarters + dimes + nickles + pennies
    change = max(given_coins - req_coins, 0)
    if given_coins < req_coins:
        print("Not enough money. Refunded.")
    else:
        adjust_resources(choice)
        print(f"Given ${given_coins}.")
        if change > 0:
            print(f"Here's your ${change} change.")
        print(f"Enjoy your {choice.title()}")
    start()

def start():
    choice = input("What would you like? (espresso/latte/cappuccino? ")
    resources_okay = process_choice(choice)
    if resources_okay is not None:
        process_payment(choice)
    else:
        start()

start()
