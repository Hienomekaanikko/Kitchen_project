class Fridge:
    def __init__(self):
        self.supply = {}
        self.space = 150  # liters
        self.shelf = 5  # shelf's
        self.temperature = 6  # celsius

    # Update bought groceries into the current supply of refrigerator
    def input_groceries(self):

        # Start unloading the shopping bags
        not_finished = True
        while not_finished:
            purchase = input("Purchase: (type 'finished' when done.)")
            if purchase == "finished":
                not_finished = False
            else:
                amount = int(input("Amount in liters: "))
                self.space -= amount

                # Check if space available in the refrigerator
                if self.space < 0:
                    return f"No more space in the fridge left."
                self.supply[purchase] = self.supply.get(purchase, 0) + amount
        current_supply = self.supply
        return current_supply
