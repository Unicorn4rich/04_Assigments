
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


def get_last_element(lst):
  print(lst[-1])


lst = []

input_num = int(input("Please enter total inputs number: "))
for i in range(input_num):
      user_value = input("Please enter value: ")
      lst.append(user_value)


get_last_element(lst)