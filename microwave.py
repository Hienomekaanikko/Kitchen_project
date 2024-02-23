import time

class Microwave:
    def __init__(self):
        self.space = 10 #liters
        self.dirt = 10 #in scale from 10 to being dirtiest to 1 being cleanest

    def run_microwave(self):
        timer = int(input("Set the timer in seconds: "))
        power = int(input("Set the power in watts: "))
        running = True
        while running:
            print("*microwave sound*...")
            for i in range(timer, 0, -1):
                time.sleep(1)
                print(f"\r{i} seconds left", end="", flush=True)
            print("\r             ", end="", flush=True)
            print("\rBeep, Beep, beep! Microwaving finished!")
            running = False
        print(f"Microwave ran for {timer} seconds with {power} watts.")
        return timer, power

    def input_food(self):
        pass

    def take_food(self):
        pass

    def beep_sound(self):
        pass

microwave = Microwave()
microwave.set_timer()