# Countdown Timer Python Project
# In this Code With Tomi tutorial, you will learn how to build a countdown timer using the time Python module. This is a great beginner project to get you used to working with while loops in Python.


import time

def countdown_timer():

  while True:
    print("\n1.Enter seconds.")
    print("2.Enter minutes.")

    # for option chose
    user_chose = input("Please select option: (1/2): ")
    if user_chose not in ['1', '2']:
      print("Please select valid number (1 or 2)")
      continue

    
    # for timinh chose
    user_input = input("Enter your countdown time : ")
    if user_input == "":
      print("Please enter a value!")
      continue

    # for error handling
    try:
      user_chose = int(user_chose)
      user_time = int(user_input)
      return user_chose, user_time
    except ValueError:
      print("Invalid input please enter only numbers")


return_values = countdown_timer()
user_chose, user_time = return_values



# class
class Count_manage:

  def __init__(self, user_chose, user_time):
    self.user_chose = user_chose
    self.user_time = user_time


  def conditional_func(self):

    # for seconds
    if self.user_chose == 1:
      while self.user_time >= 0:
        print(self.user_time)
        time.sleep(1)
        self.user_time -= 1
      print("Times-Up Bro!")  

    # for minutes
    if self.user_chose == 2:
      self.user_time = self.user_time * 60
      while self.user_time >= 0:
        print(self.user_time)
        time.sleep(1)
        self.user_time -= 1
      print("Times-Up Bro!")    



instance = Count_manage(user_chose, user_time)
instance.conditional_func()