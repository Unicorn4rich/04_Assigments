# Simulate rolling two dice, and prints results of each roll as well as the tota


import random

def main():
  first_dice =  random.randint(1, 6)
  second_dice = random.randint(1, 6) 

  print(f"Dice1: {first_dice}")
  print(f"Dice2: {second_dice}")

  total = first_dice + second_dice
  print("total of two dice:", total)

 


if __name__ == '__main__':
    main()