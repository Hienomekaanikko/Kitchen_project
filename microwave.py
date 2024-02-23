import time

class Microwave:


    def __init__(self):
        self.space = 10  #liters
        self.dirt = 1  #in scale from 10 to being dirtiest to 1 being cleanest

    def run_microwave(self):
        food = self.input_food()
        timer = int(input("Set the timer in seconds: "))
        power = int(input("Set the power in watts: "))
        running = True
        while running:
            self.dirt += 1
            print("*microwave sound*...")
            for i in range(timer, 0, -1):
                time.sleep(1)
                print(f"\r{i} seconds left", end="", flush=True)
            print("\r             ", end="", flush=True)
            print(f"\rBeep, Beep, beep! Microwaving {food} finished!")
            running = False
        print(f"Microwave ran for {timer} seconds with {power} watts.")
        return timer, power

    def input_food(self):
        food = input("What food would you like to microwave?")
        print(f"Alright, lets heat the {food} up!")
        return food

    def take_food(self):
        pass


microwave = Microwave()

microwave.run_microwave()