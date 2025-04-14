list_of_Numbers: list[int] = [1, 2, 4, 3, 2]

UPDATE_VAR = 0

def main(Numbers: list[int]):

  for i in Numbers:
    UPDATE_VAR = i * 2
    print(UPDATE_VAR)




if __name__ == '__main__':
  main(list_of_Numbers)
