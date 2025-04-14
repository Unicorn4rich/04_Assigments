# Rock, paper, scissors Python Project
# In this Kylie Ying tutorial, you will work with random.choice(), if statements, and getting user input. This is a great project to help you build on the fundamentals like conditionals and functions.


import random

def R_P_S_Game():

  choice_list = ["rock", "paper", "scissors"]

  
  user_choice = input("Enter your Choice (rock/paper/scissors) : ")
  while user_choice not in choice_list:
    print("Invalid input! Please chose: (rock/paper/scissors)")
    user_choice = input("Enter your Choice (rock/paper/scissors) : ")

  computer_choice = random.choice(choice_list)

  print("You chose", user_choice)
  print("Computer chose:", computer_choice)

  return user_choice, computer_choice


user_comp_values = R_P_S_Game() 
# return values unpacking
user_chose, computer_choice = user_comp_values



class Game_class:

  def __init__(self, user_chose, computer_chose):
    self.user_chose = user_chose
    self.computer_chose = computer_chose

  def condition_func(self):
    if user_chose == self.computer_chose:
      print("Match tie!")
    elif (self.user_chose == "rock" and self.computer_chose == "scissors") \
      or (self.user_chose == "scissors" and self.computer_chose == "paper") \
      or (self.user_chose == "paper" and self.computer_chose == "rock"):
      print("Congratulations You Win!")
    else:
      print("You lose Computer win!")

    agian = input("\nDo you want to play more? (yes/no): ") 
    if agian == "yes":
      return True
    else:
      return False  



while True:
  result = Game_class(user_chose, computer_choice)   
  if result.condition_func() == True:
    R_P_S_Game()
  else:
    print("Hava A Good day By! janu")
    break  
