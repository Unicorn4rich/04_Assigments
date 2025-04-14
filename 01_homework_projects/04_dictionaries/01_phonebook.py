# In this program we show an example of using dictionaries to keep track of information in a phonebook.


def read_phone_book():

# func1. user se name or number ley kar dict mein store krwa rhy hain.
  phonebook = {}

  while True:
    name = input("Name: ")

    if name == "":
        break

    number = input("Number: ")
    phonebook[name]= number

  return phonebook     


# func2. data laa kar yahn print krwaya.
def print_phonebook(phonebook):
  for name in phonebook:
    print(f"{str(name)} -> {str(phonebook[name])}")



def lookup_numbers(phonebook):

  while True:
    name = input("Enter name lookup: ")

    if name == "":
      break

    if name not in phonebook:
      print(f"{name} is not in the phonebook")
    else:
      print(phonebook[name])    



# func3.
def main():
  phonebook = read_phone_book()
  print_phonebook(phonebook)
  lookup_numbers(phonebook)


if __name__ == '__main__':
    main()