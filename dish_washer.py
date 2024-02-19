import time

class Dishwasher:
    # How much room for each item
    def __init__(self):
        self.glass_places = 20
        self.plate_places = 20
        self.fork_places = 15
        self.knife_places = 15
        self.spoon_places = 15

    #function to input dishes
    def fill_dishwasher(self):
        item = input("Choose the dish to input: fork, knife, spoon, glass or plate")
        if hasattr(self, f"{item}_places"):
            setattr(self, f"{item}_places", getattr(self, f"{item}_places") - 1)
        else:
            print("Invalid dish choice.")

    def run_dishwasher(self):
        running = True
        while running:
            print("BrRrRrRrRrRrR...")
            time.sleep(10)
            print("Beep, Boop. Dishes are ready and clean!")
            running = False

    def empty_dishwasher(self):

