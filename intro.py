# # single line comment
# ''' multi line comments
# line 2
#  line 3
#  '''

#  # print function

# print("hello world")

#     # variables and data types

# a=10
# b=11.111111111111111111111111
# print(type(a)) # type function is used to check data type
# print(type(b)) 


# identifiers
# _name= "hello"
# print(_name)

# Name= "hello"
# print(Name)

# data types

''' 
1. String ==== " " ---exmaple " Abhinav"
2. List ==== [ ] --- example [1,2,3,4]
3. Tuple ==== ( ) --- example (1,2,3,4)
4. Dictionary ==== { } --- example {"name":"Abhinav", "age":21
5. Set ==== { } --- example {1,2,3,4}
6. Array ==== array() --- example array([1,2,3,4])
'''

# a=[4,5,6,7,8]
# print(type(a))

# arithmetic operators
# a=10
# b=3 
# c= a+b
# d=a-b
# print("a+b =",c,"This is addition")
# print(f"a-b = {d} this is subtraction")  # f string

# print(a%b) # Modulus operator, it will print the remainder

# print(a//b) # Floor division, it will print the quotient without decimal

# print(a**b) # Exponentiation operator, it will print a raised to the power b
# print(pow(a,b)) # same as a**b
# print("-------------------")

# comparison operators
# print(a==b) # equal to
# print(a!=b) # not equal to  
# print(a>b)  # greater than
# print(a<b)  # less than
# print(a>=b) # greater than or equal to
# print(a<=b) # less than or equal to
# print("-------------------")

# # logical operators
# print((a>b) and (a!=b)) # and operator
# print((a>b) or (a!=b))  # or operator
# print(not(a>b))         # not operator
# print("-------------------")

# # assignment operators
# c=a  # c=10
# c+=b # c=c+b => c=10+3=13
# print(c)
# c-=b # c=c-b => c=13-3=10
# print(c)
# c*=b # c=c*b => c=10*3=30
# print(c)
# c//=b # c=c//b => c=30//3=10
# print(c)
# c**=b # c=c**b => c=10**3=1000
# print(c)
# c%=b  # c=c%b => c=1000%3=1
# print(c)
# print("-------------------")

# e=10
# d=5
# e+=d
# print(e) #15

# print("-------------------")

# a=[1,2,3,4,5]
# b=5
# print(b in a)  # in operator
# print(b not in a) # not in operator

# naam="Gurminder singh"
# print("urm" in naam)
# print("urm" not in naam)

# print(a is b)  # is operator
# print(a is not b) # is not operator
# a='c'
# print(type(a))

# print("-------------------")

# a= input("Enter your nanme: ")
# print(a)
# b=int(input("Enter your age: "))
# print(b)

# id concept 
# i=10
# j=10
# print(id(i))
# print(id(j))
# print("-----")
# k='hi'
# l='hi'
# print(id(k))
# print(id(l))

# # i=int(input("enter i "))
# # j=int(input("enter j "))
# i=input("enter i ")
# j=input("enter j ")
# print(id(i))
# print(id(j))