# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2


def main():
  first_number = int(input("Please enter an integer to be divided: "))
  second_number = int(input("Please enter an integer to divide by: "))

  devided = first_number // second_number
  remainder = first_number % second_number
  print(f"The result of the devision is: ({devided}) and the reminder is: ({remainder})")


if __name__ == '__main__':
    main()