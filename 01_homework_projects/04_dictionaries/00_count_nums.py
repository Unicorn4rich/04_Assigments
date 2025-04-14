# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.
# An example run of the program looks like this (user input is in blue):
# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.



def main():

  dictionory = {}

  while True:
    user_numbers = input("Enter your numbers: ")

    if user_numbers == "":
      print("Goodby!")
      break


# adding data in dictionory
    number = int(user_numbers)

    if number in dictionory:
      dictionory[number] += 1
    else: 
      dictionory[number] = 1  


  for num, count in dictionory.items():
    print(f"{num}: apears in {count} times")
  



if __name__ == '__main__':
    main()