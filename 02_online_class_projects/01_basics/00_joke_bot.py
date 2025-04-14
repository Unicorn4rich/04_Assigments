joke: str = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
prompt: str = "What do you want?"
sorry: str = "Sorry I only tell jokes"


def bot():
   userAnswer: str = input(f"{prompt}: ")

   if "joke" in userAnswer.lower():
    print(joke)
   else:
    print(sorry)

bot()