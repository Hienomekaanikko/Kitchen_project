class BotCloset:
  def __init__(self):
    self.smallcattle = 2
    self.bigcattle = 2

  def take_cattle(self):
    choice = input("Do you want a small cattle or big cattle? Type: small/big: "
    if choice == "small":
        self.smallcattle -= 1
    elif choice == "big" :
        self.bigcattle -= 1
    else:
        return f"This is not available."
  

class DryFood:
  def __init__(self):
    self.supply = {}
    self.space = 200 #liters

  def input_groceries(self):

  # Start unloading the shopping bags
  not_finished = True
  while not_finished:
      purchase = input("Dryfood Purchase: (type 'finished' when done.)")
      if purchase == "finished":
          not_finished = False
      else:
          amount = int(input("Amount in liters: "))
          self.space -= amount

          # Check if space available in the refrigerator
          if self.space < 0:
              return f"No more space in the closet left."
          self.supply[purchase] = self.supply.get(purchase, 0) + amount
  current_supply = self.supply
  return current_supply


    
