# Problem Statement
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5



def main():
    side_One = float(input("What is the length of side 1?: "))
    side_two = float(input("What is the length of side 2?: "))
    side_three = float(input("What is the length of side 3?: "))

    sum_total = side_One + side_two + side_three

    print(f"The perimeter of the triangle is: {sum_total}")


if __name__ == '__main__':
  main()  
  

# Output:  
# What is the length of side 1?: 3
# What is the length of side 2?: 4
# What is the length of side 3?: 5.5
# The perimeter of the triangle is: 12.5  