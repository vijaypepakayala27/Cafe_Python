class CoffeeMachine:
    def __init__(self):
        self.inventory = {
            "water": 1000,  # in ml
            "milk": 1000,   # in ml
            "espresso": 500 # in grams
        }

    def check_inventory(self, water, milk, espresso):
        if self.inventory["water"] < water:
            print("Sorry, not enough water.")
            return False
        if self.inventory["milk"] < milk:
            print("Sorry, not enough milk.")
            return False
        if self.inventory["espresso"] < espresso:
            print("Sorry, not enough espresso.")
            return False
        return True

    def brew(self, coffee_type, size):
        recipes = {
            "espresso": {"small": {"water": 50, "milk": 0, "espresso": 15},
                         "tall": {"water": 75, "milk": 0, "espresso": 20},
                         "grande": {"water": 100, "milk": 0, "espresso": 25}},
            "cappuccino": {"small": {"water": 50, "milk": 50, "espresso": 15},
                           "tall": {"water": 75, "milk": 75, "espresso": 20},
                           "grande": {"water": 100, "milk": 100, "espresso": 25}},
            "latte": {"small": {"water": 50, "milk": 100, "espresso": 15},
                      "tall": {"water": 75, "milk": 150, "espresso": 20},
                      "grande": {"water": 100, "milk": 200, "espresso": 25}}
        }

        if coffee_type not in recipes or size not in recipes[coffee_type]:
            print("Invalid coffee type or size.")
            return False

        required = recipes[coffee_type][size]
        if not self.check_inventory(required["water"], required["milk"], required["espresso"]):
            return False

        self.inventory["water"] -= required["water"]
        self.inventory["milk"] -= required["milk"]
        self.inventory["espresso"] -= required["espresso"]

        print(f"Your {size} {coffee_type} is ready!")
        return True

    def show_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item.capitalize()}: {quantity} ml/grams")
