# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """


def in_range(n, low, high):
  if n >= low and n <= high:
    return True
  else: 
    return False  


def main():
  result = in_range(5, 3, 10)
  print(result)

if __name__ == '__main__':
    main()