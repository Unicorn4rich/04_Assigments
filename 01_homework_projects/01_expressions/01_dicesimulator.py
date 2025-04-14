# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.


import random


num_six = 6

def roll_dice():
  random_dice1 = random.randint(1, num_six)
  random_dice2 = random.randint(1, num_six)
  
  total_dice = random_dice1 + random_dice2
  print("total of two dice:", total_dice)


def main():
  roll_dice()
  roll_dice()
  roll_dice()

if __name__ == '__main__':
  main()
  
  
# output:
    
# total of two dice: 12
# total of two dice: 8
# total of two dice: 6      