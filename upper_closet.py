class UpCloset:
    def __init__(self):
        self.glass = 10
        self.foodplate = 10
        self.shallowplate = 10
        self.breadplate = 10

    #choosing appropriate dish
    def take_dish(self):
        choosing = True
        while choosing:
            choice = input("Which dish would you need? glass/foodplate/shallowplate/breadplate?")
            if hasattr(self, f"{choice}"):
                setattr(self, f"{choice}", getattr(self, f"{choice}") -1)
                choosing = False
            else:
                print("Don't have this one")

    #how many dishes available/how many in dishwasher
    def check_inventory(self):