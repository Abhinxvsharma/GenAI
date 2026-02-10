# #default parameters 
# def newFunc(a,b):
#     return(a+b)
    
# print(newFunc(10,12))

# #lambda functions - anonymous function - single line function
#   #lambda (parameters): print() or return 
# s= lambda a,b:a+b
# # s= lambda a,b:print(a+b)

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
# l=["apple", "banana", "cherry"]
# l2=[23,45,67,89]
# print(l)
# for i in enumerate(l):
#     print(i)
# for i,j in enumerate(l):
#     print(i,"--",j)

# di= {'name':'Sourav','class':'btech','rollno':123}
# for i in di.items():
#     print(i)
# for i,j in enumerate(di.items()):  # .keys or .values
#     print(i,"--",j)

#map function - map(function, iterable)
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, numbers))
print(squares)

# # filter function - filter(function, iterable)
# numbers = [1, 2, 3, 4, 5]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)


# # #sorted function - sorted(iterable, key=function)
# students = [("John", 85), ("Emma", 92), ("Sam", 78)]
# print(students)
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

    