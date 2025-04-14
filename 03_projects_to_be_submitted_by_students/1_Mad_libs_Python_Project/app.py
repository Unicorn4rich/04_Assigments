# Mad libs Python Project
# you will learn how to get input from the user, work with f-strings, and see your results printed to the console.
# This is a great starter project to get comfortable doing string concatenation in Python.


class Madlibs:
    
    def __init__(self, user_name: str, user_age: int):
         self.user_name = user_name
         self.user_age = user_age
         
         
    def logic_wala(self):
        return f"Your name is {self.user_name} and your agr is {self.user_age}"     
     
     

user_name = input("Enter your name: ")        
user_age = int(input("Enter your age: "))        
        
        
user_tera_bera_gharaq = Madlibs(user_name, user_age)  

print(user_tera_bera_gharaq.logic_wala())      



