# Your all planet code

# earth weight get from user
# planet_weight get from user

planetry_weight_constant = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0,
}


def planetry_weight():
  earth_weight = int(input("Enter your earth weight: "))
  user_planet = str(input("Enter the name of planet you are going to visit: "))

  if user_planet in planetry_weight_constant:
    planetry_weight = earth_weight * planetry_weight_constant[user_planet] / 100
    rounded_weight: float = round(planetry_weight, 1)
    print(f"Your weight on planet {user_planet} {rounded_weight}.")

  else:
    print("We can only calculate solar system values.")

planetry_weight()



# check for all mile stones google colab
# https://colab.research.google.com/drive/1SH0TWAw8iOcUgL5VD63U8dOgETsUTwc5#scrollTo=WEQ21tHyrTR_