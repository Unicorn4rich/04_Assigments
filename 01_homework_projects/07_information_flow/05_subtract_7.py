# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.


def subtract_seven(num):
  return num - 7


def main():
  user_number = int(input("Enter your number: "))
  value = subtract_seven(user_number)
  print(f"The result after subtracting 7: {value}")


if __name__ == '__main__':
    main()