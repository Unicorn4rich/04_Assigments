# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.


MAX_LENGTH: int = 3

# user ki list ke start ke 3 elements ko chor kar baqi sab delete karta hai or print. 
def shorten(list_data):
  while len(list_data) > MAX_LENGTH:
    remove_elements = list_data.pop()
    print("removed: ", remove_elements)


# user se data ley kar return karne wala function
def get_list():
  
  lst = []
  user_values = input("Enter your values: ") 
  while user_values != "":
    lst.append(user_values)
    user_values = input("Enter your values: ")
  return lst



# main function yahn se sary functions chal rhy hain.
def main():
  list_data = get_list()
  shorten(list_data)


if __name__ == '__main__':
    main()