import random

user_score = 0
computer_score = 0



def Heigh_Low():
   global user_score, computer_score, rounds

   print(f"""Welcome to the High-Low Game!
-----------------------------""")


   rounds_input = int(input("How many rounds do you play?: "))
   rounds = 1

   while rounds <= rounds_input:
    print(f"\n Round {rounds}/{rounds_input}")

    user_Number = random.randint(1, 100)
    computer_Number = random.randint(1, 100)

    print(f"Your Number is: {user_Number}")
    # print(f"computer Number is: {computer_Number}")

    user_answer = input("Do you think your number is higher or lower than the computer's?: ")

    if user_answer == "higher" and user_Number > computer_Number:
     user_score += 1
     print(f"You were right! The computer's number was: {computer_Number}")
     print(f"Your score is now: {user_score}")

    elif user_answer == "higher" and user_Number < computer_Number:
     computer_score += 1
     print(f"Aww, that's incorrect. The computer's number was: {computer_Number}")
     print(f"Computer score is: {computer_score}")

    elif user_answer == "lower" and user_Number < computer_Number:
        user_score += 1
        print(f"You were right! The computer's number was: {computer_Number}")
        print(f"Your score is now: {user_score}")

    elif user_answer == "lower" and user_Number > computer_Number:
        computer_score += 1
        print(f"Aww, that's incorrect. The computer's number was: {computer_Number}")
        print(f"Computer score is: {computer_score}")

    rounds += 1 # condition of loop for breaking

   if user_score > computer_score:
    print(f"\n Congratulations You Win: {user_score} 🎉")
   else:
    print(f"\n Oops You lose Computer Win: {computer_score} 😥")

Heigh_Low()