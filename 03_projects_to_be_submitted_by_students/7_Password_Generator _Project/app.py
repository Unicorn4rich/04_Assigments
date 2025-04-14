# Password Generator Python Project
# In this Code With Tomi tutorial, you will learn how to build a random password generator. You will collect data from the user on the number of passwords and their lengths and output a collection of passwords with random characters.

# This project will give you more practice working with for loops and the random Python module.



import random
import string


def Random_Password():
  
  while True:
    total_pass = input("Enter the number how many passwrds you want: ")
    if total_pass == "":
      print("Please enter a number")
      continue

    pass_length = input("Enter the Length of each password: ")
    if pass_length == "":
      print("Please enter a number")
      continue

    try:
        total_pass = int(total_pass)
        pass_length = int(pass_length)
        if total_pass <= 0 or pass_length <= 0:
          print("Please enter positive number!")
          continue
    except ValueError:
      print("Invalid input please enter a number")   

    break  

  return total_pass, pass_length



return_val = Random_Password()  
total_pass, pass_length = return_val



# class 
class Genrate_pass:

  def __init__(self, total_pass: int, pass_length: int):
    self.total_pass = total_pass
    self.pass_length = pass_length
    self.password_pool = string.ascii_letters + string.ascii_letters + string.digits + string.punctuation

  def conditional(self):

    for i in range(self.total_pass):
      password = "".join(random.choice(self.password_pool) for _ in range(self.pass_length))
      print(password)
    print(f"This is your total number of passwords ({self.total_pass}) and each length ({self.pass_length})")  




instance = Genrate_pass(total_pass, pass_length) 
instance.conditional() 