# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!


# function 1
def count_even(lst):
  count = 0

  for i in lst:
    if i % 2 == 0:
      count += 1
      # 3
  
  print("Total Even number: ", count)
  print("user main list: ", lst)  


# function 2
def main():

  lst = []

  while True:
    user_list = input("Enter an integer or press enter to stop: ")
    if user_list == "":
      break
    else:
      try:
        user_list = int(user_list)
        lst.append(user_list) 
      except ValueError:
        print("Invalid input! please enter a number")
        continue  

  count_even(lst)    


if __name__ == '__main__':
    main()