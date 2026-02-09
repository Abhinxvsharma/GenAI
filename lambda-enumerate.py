# #default parameters 
# def newFunc(a,b):
#     return(a+b)
    
# print(newFunc(10,12))

# #lambda functions - anonymous function - single line function
#   #lambda (parameters): print() or return 
# s= lambda a,b:a+b
# s= lambda a,b:print(a+b)

# x= lambda x : x**2
# print(x(5))
# print(s(10,12))


# def oddNumberr(a):
#     if a%2!=0:
#         # return "Odd"
#         print("Odd")
#     else:
#         print("Even")
#         # return "Even"

# oddNumber=lambda a:"Odd" if a%2!=0 else "Even"
# print(oddNumber(12))


# # Enumerate function 
# l=[12,35,11,10,4,32]
# # l2=[23,45,67,89]
# print(l)
# for i in enumerate(l):
#     print(i)
# for i,j in enumerate(l):  # i=index and j=value
#     print(i,"--",j)

# di= {'name':'Sourav','class':'btech','rollno':123}
# for i in di.items():
#     print(i)
# for i,j in enumerate(di.items()):  # .keys or .values
#     print(i,"--",j)