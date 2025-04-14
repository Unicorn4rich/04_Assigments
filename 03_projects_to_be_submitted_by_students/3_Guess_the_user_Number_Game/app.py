import random


def computer_guess():

  user_select_num: int = int(input("Enter your secret number: "))
  print("User SET Number: ", user_select_num)
  return user_select_num

user_num = computer_guess()




# class
class Game_class:

  def __init__(self, user_num):
    self.user_secret_num = user_num
    self.start_num = 1
    self.end_num = 99
    self.computer_guess_num = random.randint(self.start_num, self.end_num)


  def conditional(self):
    print(f"Computer Guess number is: {self.computer_guess_num }")

    user_hint = input("User hint: ").lower()

    if user_hint == "correct":
      print("Computer Win!")
      return True
    elif user_hint == "high":
     self.end_num = self.computer_guess_num - 1 
     return False
    elif user_hint == "low":
      self.start_num = self.computer_guess_num + 1 
      return False


  def update_range(self):
    
    if self.computer_guess_num > self.user_secret_num:
      self.computer_guess_num = random.randint(self.start_num, self.end_num)
    elif self.computer_guess_num < self.user_secret_num:
      self.computer_guess_num = random.randint(self.start_num, self.end_num)
    else:
            
        pass 
              



while True:
  result = Game_class(user_num)
  if result.conditional() == True:
    break
  result.update_range()  


