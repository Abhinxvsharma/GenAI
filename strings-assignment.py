#1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return ‘not a valid string’ instead of the empty string

# string="Abhinav Sharma"

# if len(string)<2:
#      print("not a valid string")
# else:
#      print(string[0:2],string[-2:])
     
#2. Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string

# string="coder"
# string2="roots"

# print(string.replace("c","r"),string2.replace("r","c"))


#3. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged

# string= input("Enter a string: ")

# if len(string)>=3:
#         if string.endswith("ing"):
#             print(string.replace("ing","ly"))
#         else:
#             print(string+"ing") 
