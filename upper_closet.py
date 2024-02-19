class UpCloset:
    def __init__(self):
        self.glass = 10
        self.food_plate = 10
        self.shallow_plate = 10
        self.bread_plate = 10

    #choosing appropriate dish
    def take_dish(self):
        choice = input("Which dish would you need? glass/foodplate/shallowplate/breadplate?")

    #how many dishes available/how many in dishwasher
    def check_inventory(self):