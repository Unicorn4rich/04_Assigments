import random

# hmara function
def Random_word():

    Words_categories = {
        "language": ["python", "sanity"],
        "games": ["cricket", "hockey"],
        "movies": ["react", "sanity"],
    }

    # category
    random_category = random.choice(list(Words_categories.keys()))
    print("Random Category: ", random_category)

    # word
    random_word = random.choice(Words_categories[random_category])
    print("Random Word: ", random_word)

    word_length = len(random_word)
    print("Word Length: ", word_length)

    # underscore
    under_scores = "_" * word_length
    print(f"Please fill in the blanks: {under_scores}")

    return random_word, under_scores



# Class
class Random_class:

    def __init__(self, random_word, under_scores):
        self.random_word = random_word
        self.under_scores = under_scores
        self.chracter_list = []  


    def condition_func(self):
        while True:
            user_latter = input("\nGuess One letter only: ").lower()

            if len(user_latter) == 1 and user_latter.isalpha():
                if user_latter in self.random_word:
                    self.chracter_list.append(user_latter)

                    display_word = "".join([letter  if letter in self.chracter_list else "_" for letter in self.random_word])
                    print(f"Current word: {display_word}")

                    if display_word == self.random_word:
                        print("\nCongratulations! You've guessed the word correctly!")
                        break
                else:
                    print("Incorrect guess, try again!")
            else:
                print("Please enter a valid letter.")
        


# function ki return values yahn se ley rhy hain.
random_word, under_scores = Random_word()

# class ka instance bnaya hai
Game_ready = Random_class(random_word, under_scores)
# method chala le dekh rhy hain ke shoaib ne sahi bnaya hai ya nahi.
Game_ready.condition_func()











# SImple functions se bnaya gaya projectoropar wala class se bnaya hua hai.


# import random

# def Random_word():

#   Words_categories = {
#     "language": ["python", "sanity"],
#     "games": ["cricket", "hockey"],
#     "movies": ["react", "sanity"],
#   }


  
#   # category
#   random_category = random.choice(list(Words_categories.keys()))
#   print("random_category: ", random_category)

#   # word
#   random_word = random.choice(Words_categories[random_category])
#   print("random_word: ", random_word)


#   word_length = len(random_word)
#   print("word_length", word_length)

#   under_scores ="_" * word_length
#   print(f"Please fill in the blanks: {under_scores}")
 


#   chracter_list = []

#   # user input
#   while True:
#     user_latter = input("\nGuess One latter only: ").lower()

#     if len(user_latter) == 1 and user_latter.isalpha():
#       if user_latter in random_word:
#         chracter_list.append(user_latter)

#         deisplay_word = "".join([latter if latter in chracter_list else "_" for latter in random_word])
#         print(f"Currunt word: {deisplay_word}")

#         if deisplay_word == random_word:
#           print("\nCongratulations! You've guessed the word correctly!")
#           break

#       else:
#         print("Incorrect guess, try again!")


#     else:
#       print("Please enter a valid letter!")       
        
   



# Random_word()  