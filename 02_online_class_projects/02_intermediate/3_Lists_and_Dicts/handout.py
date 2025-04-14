from typing import Union

def Text_Game():

  Data_list: list[Union[str, int]] = ["shoaib", "Ali", 23, "Taha", "ahmed", 20, "malik", 22, "year", 2025]


  print("1.access")
  print("2.modify")
  print("3.slice")
  user_Input = input("Please Chose Option 1 to 3 for modify list: ")


  if user_Input == "1":
    index_value = int(input("Please Enter index number to show Item: "))
    if index_value < len(Data_list):
      print("\n This is your index value: ",Data_list[index_value])
    else:
      print("\n Please enter Correct index number")

  elif user_Input == "2":
      update_index = int(input("Enter your index number: "))
      update_value = input("Write your value to update the list element: ")
      if update_index < len(Data_list):
        Data_list[update_index] = update_value
        print("\n Updated List: ", Data_list)
      else:
        print("\n Please enter correct index for update value")

  elif user_Input == "3":
    start_index = int(input("please enter starting index: "))
    end_index = int(input("please enter ending index: "))
    if start_index <= len(Data_list) and end_index <= len(Data_list) and start_index < end_index:
      new_list = Data_list[start_index : end_index]
      print("\n Slice List: ", new_list)
    else:
      print("\n Index sahi Dalo Bhai Jaan")


if __name__ == "__Text_Game__":
  Text_Game()
  
  
  
  
# google colab link  
# https://colab.research.google.com/drive/1WwRZ4EVQfYH-KpIgo92q3K4lcx5WtFYj#scrollTo=kv3JhkJkZ1Bh  