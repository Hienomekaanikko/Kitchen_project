import time

class Microwave:
    def __init__(self):
        self.space = 10 #liters
        self.dirt = 10 #in scale from 10 to being dirtiest to 1 being cleanest

    def set_timer(self):
        timer = int(input("Set the timer in seconds: "))
        running = True
        while running:
            print("*microwave sound*...")
            for i in range(timer, 0, -1):
                time.sleep(1)
                print(f"\r{i} seconds left", end="", flush=True)
            print("\r             ", end="", flush=True)
            print("\rBeep, Beep, beep! Microwaving finished!")
            running = False

    def set_power(self):
        pass

    def input_food(self):
        pass

    def take_food(self):
        pass

    def beep_sound(self):
        pass

microwave = Microwave()
microwave.set_timer()