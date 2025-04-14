# Write a function that takes two numbers and finds the average between the two.




def main(num1: int, num2: int):

  total = num1 + num2 
  average_val = total / 2
  print("Average: ", average_val)


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if num1 == "" and num2 == "":
  print("please enter a number")
  exit()

try:
  num1s = int(num1)
  num2s = int(num2)
except ValueError:
  print("Invalid input! Please enter a number")
  exit()


if __name__ == '__main__':
    main(num1s, num2s)