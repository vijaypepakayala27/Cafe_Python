class BakingMachine:
    def __init__(self):
        self.inventory = {
            "batter": 2000,  # grams
            "flavor": {"chocolate": 10, "vanilla": 10, "berry": 10},  # counts
            "shapes": {"round": 10, "square": 10, "love": 10}  # counts
        }

    def bake(self, item, flavor, shape):
        """
        Check inventory and bake the item.
        """
        if self.inventory["batter"] < 200:
            print("Sorry, not enough batter.")
            return False
        if flavor not in self.inventory["flavor"] or self.inventory["flavor"][flavor] <= 0:
            print(f"Sorry, we are out of {flavor} flavor.")
            return False
        if shape not in self.inventory["shapes"] or self.inventory["shapes"][shape] <= 0:
            print(f"Sorry, we are out of {shape} shapes.")
            return False

        # Deduct ingredients
        self.inventory["batter"] -= 200
        self.inventory["flavor"][flavor] -= 1
        self.inventory["shapes"][shape] -= 1
        print(f"{shape.capitalize()} {flavor.capitalize()} {item} baked successfully!")
        return True
