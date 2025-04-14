# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


def main():
  user_feet: float = float(input("Enter foot/feet number to convert inches: "))

  result = user_feet * 12
  print("This is", result, "Inches")



if __name__ == '__main__':
    main()
    
# Enter foot/feet number to convert inches: 2
# This is 24.0 Inches    