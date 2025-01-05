class Billing:
    def __init__(self):
        self.total = 0

    def add_to_bill(self, amount):
        self.total += amount
        print(f"${amount} added to your bill. Total bill: ${self.total}")

    def print_bill(self):
        print(f"Your final bill is ${self.total}. Thank you for visiting Py_cafe!")
        self.total = 0  # Reset the bill for the next customer
