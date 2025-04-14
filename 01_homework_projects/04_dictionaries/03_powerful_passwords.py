from hashlib import sha256


# function 1
def login(email, stored_logins, password_to_check):


  if stored_logins[email] == hash_password(password_to_check):
    return True

  return False  


# function 2
def hash_password(password):

  return sha256(password.encode()).hexdigest()



# function 3
def main():

  stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
  }


  print(login("example@gmail.com", stored_logins , "word"))
  print(login("example@gmail.com", stored_logins, "password"))

  print(login("code_in_placer@cip.org", stored_logins, "Karel"))
  print(login("code_in_placer@cip.org", stored_logins, "karel"))
    
  print(login("student@stanford.edu", stored_logins, "password"))
  print(login("student@stanford.edu", stored_logins, "123!456?789"))


if __name__ == '__main__':
    main()





# 🎯 Execution Flow (Step-by-Step)
# 1️⃣ User Email aur Password Input Hota Hai
# 2️⃣ Stored Hashed Password Fetch Hota Hai
# 3️⃣ User ka Password Hash Kiya Jata Hai
# 4️⃣ Dono Hashes Compare Hote Hain
# 5️⃣ Agar Hashes Match → Login Successful ✅
# 6️⃣ Agar Hashes Match Nahi Hote → Login Failed ❌

