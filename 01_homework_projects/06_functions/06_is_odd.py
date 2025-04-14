# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd


def main():
  Evodd_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

  for i in Evodd_list:
    if i % 2 == 0:
      print(f"{i} even ", end="")
    else:
      print(f"{i} odd ", end="")    


if __name__ == '__main__':
    main()