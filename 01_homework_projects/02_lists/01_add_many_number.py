# Write a function that takes a list of numbers and returns the sum of those numbers.


list_of_Numbers: list[int] = [1, 2, 4, 6, 2]

def main(Numbers: list[int]):

  total_num =  0
  for i in Numbers:
    total_num += i
  return total_num 


if __name__ == '__main__':
    result = main(list_of_Numbers)
    print(result)