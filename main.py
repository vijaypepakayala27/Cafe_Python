import time
from CoffeeMachine import CoffeeMachine
from menu import *
from inventory import coffee_inventory, baking_inventory
from Baking_Machine import BakingMachine
from Billing_Machine import Billing

# Initialize objects
coffee_machine = CoffeeMachine()
baking_machine = BakingMachine()
billing = Billing()

items = list(menu.keys())

def slow_print(message):
    """Simulate slow printing for realistic experience."""
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

# Main Cafe Loop
cafe = 'open'
order_number = 1  # Track order numbers
while cafe == 'open':
    print("\nWelcome to Py_cafe")
    order = input(f"What would you like to order today? Options: {items}: ").lower()

    if order in ["espresso", "cappuccino", "latte"]:
        size = input(f"What size would you like? {sizes}: ").lower()
        if size in sizes:
            if coffee_machine.brew(order, size):
                billing.add_to_bill(menu[order]['price'])
                print(f"Thank you! Your order no. #{order_number} is being prepared...")
                slow_print("......")
                print("Thanks for ordering. Next customer, please!")
                order_number += 1
            else:
                print(f"Sorry, we are out of ingredients for {order}.")
        else:
            print("Invalid size. Please try again.")

    elif order == "cake":
        shape = input(f"What shape would you like? Available shapes: {shapes}: ").lower()
        flavour = input(f"What flavour would you like? Available flavours: {flavours}: ").lower()
        if shape in shapes and flavour in flavours:
            if baking_machine.bake(order, flavour, shape):
                billing.add_to_bill(menu[order]['price'])
                print(f"Thank you! Your order no. #{order_number} is being prepared...")
                slow_print("......")
                print("Thanks for ordering. Next customer, please!")
                order_number += 1
            else:
                print(f"Sorry, we are out of ingredients for {shape} {flavour} cake.")
        else:
            print("Invalid shape or flavour. Please try again.")

    elif order == "muffin":
        flavour = input("What flavour would you like? (banana, chocolate): ").lower()
        if flavour in ["banana", "chocolate"]:
            if baking_machine.bake(order, flavour, "round"):
                billing.add_to_bill(menu[order]['price'])
                print(f"Thank you! Your order no. #{order_number} is being prepared...")
                slow_print("......")
                print("Thanks for ordering. Next customer, please!")
                order_number += 1
            else:
                print(f"Sorry, we are out of ingredients for {flavour} muffin.")
        else:
            print("Invalid flavour. Please try again.")

    elif order == "exit":
        billing.print_bill()
        cash_given = float(input("Enter the cash amount you are giving: $"))
        change = cash_given - billing.total
        if change >= 0:
            print(f"Please collect your change: ${change:.2f}")
            print("Thank you for visiting Py_cafe!")
            billing.total = 0  # Reset the bill
        else:
            print(f"Insufficient amount. You still owe ${-change:.2f}.")
        cafe = 'closed'

    else:
        print("Invalid input. Please try again.")
