# string - '', ""
#     0----------11
# naam="Jasbir Singh"
# print(len(naam))
# print(naam[3])


#pal
# in forward indexing
# P=0
# a=1
# l=2
# in backward indexing
# l=-1      
# a=-2
# P=-3

# # index slicing 

# string_name[start : stop : step]

# naam="Jasbir Singh"

# print(naam[:]) # start, stop, step 
# print(naam[0:4]) # start, stop, step 
# print(naam[:5]) # by default start-0
# print(naam[1:5]) # by default start-0
# print(naam[1:]) 
# print(naam[2:15]) # 
# print(naam[1:6:2])  
# print(naam[1:10:-1])
# print(naam[11:1:-1])  

# print(naam[2])
# #

# methods 
print("-----------------")
# print(naam)
# print(naam.upper())
# print(naam.lower())
# print(naam.capitalize())
# print(naam.title())
# print(naam.swapcase())
# print(naam.endswith('ar'))  # end - substring- True or False - Case sensitive 
# print(naam.startswith('Ja'))

# print("------------")
# str1= '       hello    hi      '
# print(str1.strip())  # remove extra space from both side 
# print(str1.lstrip())  # left space removed 
# print(str1.rstrip())  # right extra space removed 

# print("-------------------")
# n="Himanshu Dhiman"
# print(n)
# # replace 
# print(n.replace(' ',''))

# print("-----------split----------")
# i="Hello, how are you class"
# print(i.split()) # by default space 
# print(i.split('o')) 

# j="bfhdsg#brjhfb#dbdh#dhgkfjvhdkl#ndfkjvhd#ndkjfhdfkjnd"
# print(j.split('#'))

name= input("Enter Your name ")
print(len(name))
for i in range(0,len(name)):
    print(name[i],end=" ")


# name= input("Enter Your name ") 
# for i in name: print(name,i)
