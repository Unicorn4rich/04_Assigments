#  you will learn how to work with Python's random module, build functions, work with while loops and conditionals, and get user input.




import random


def computer_guess_num():

  computer_random: int = random.randint(1, 99)
  # print("Computer Num: ", computer_random)


  while True:
    user_numberr = input("Enter your Guess Number: ")
    if user_numberr == "":
      print("Enter The Value!")
      continue

    try:
      user_number = int(user_numberr)  
    except ValueError:
      print("Tumhari mayya ka Enter correct value:")  
      continue


# class
    class Guess_Num:
       def __init__(self, user_number: int, computer_random: int):
         self.user_number = user_number
         self.computer_num = computer_random


       def conditional(self):
         if self.user_number == self.computer_num:
          return True
         elif self.user_number > self.computer_num:
          return False
         elif self.user_number < self.computer_num:
          return False 



    result = Guess_Num(user_number, computer_random)

    if result.conditional() == True:
      print(f"\nCongratulations You win! Computer number was {result.computer_num}")
      break
    else:
       if result.user_number > result.computer_num:
        print(f"Your number is too High!")
       elif result.user_number < result.computer_num:
        print(f"Your number is too Low!") 
      


computer_guess_num()