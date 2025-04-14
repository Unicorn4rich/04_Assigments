# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48



import random

def main():

  random_number = random.randint(0, 99)
  # print(random_number)

  while True:
   user_guess = input("Enter a new number: ")
   if user_guess == "":
    print("Please enter a number")
    continue
    
   try:
    user_number = int(user_guess)
   except ValueError:
    print("Invalid input! Please enter a Valid number")
    continue 

   if user_number == random_number:
    print("Congrats You win! The number was: ", random_number)
    break
   elif user_number > random_number:
    print("Your guess is too high")
   elif user_number < random_number:
    print("Your guess is too low")  



if __name__ == '__main__':
    main()