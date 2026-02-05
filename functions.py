# pre-defined - print, input 
# user-defined 
# def - keyword 

# print("Hello World")
# math.sum(25,26)
# int()
# len()
# range()


# def greet():
#     print("Hello User")
#     print("Welcome to Functions in Python")

# greet()

    
# # sumss()
# # print(sumss())

# a=sumss()
# print(a)

# def sums(a,b):
#     return a+b
    
# i=int(input("Enter i "))
# j=int(input("Enter j "))
# ans=sums(i,j)  # arguments
# print(ans)


# function with default parameter

# def multi(a,b=10):
#     return a*b

# a=int(input("Enter a "))
# option=input("Do you want to enter b value (y/n) ")
# if option.lower()=='y':
#     b=int(input("Enter b "))
#     print(multi(a,b))
# else:
#     print("Using default value of b")
#     print(multi(a))


# function with keyword arguments 
# def printnumber(a,b,c):
#     print(a,b,c)
    
# i=10
# j=20
# k=30
# printnumber(i,j,k)
# printnumber(i=10,j=20,k=30) # error
# printnumber(c=10,b=20,a=30)


# print("----------------")

# def checkOddEven(a):
#     if a%2==0:
#         return "Even"
#     else:
#         return "Odd"
    
# n=int(input("Enter Number "))
# print(checkOddEven(n))


# print("------------------")

# def listSum(l):
#     print(l)
#     sum=0
#     for i in range(len(l)):
#         sum+=l[i]
#     return sum
    
# n=int(input("Enter the list size: "))
# l=[]
# for i in range(n):
#     a=int(input("enter the element "))
#     l.append(a)    
# print(listSum(l))

print("------------------")

#args -  keyword arguments  *a
# def sumRet(*a):
#     print(a)
#     sum=0
#     for i in a:
#         sum+=i
#     return sum
#     # return a+b+c

# print(sumRet(45,56,88))
# print(sumRet(45,56,88,90))
# print(sumRet(45,56,88,90,100))
# print(sumRet(45,56))
# print(sumRet(45,56,10,23,56,78,98))

#** kwargs  - keyword abitrary arguments
def sumRet(**a):
    print(a)
    sum=0
    for i in a.values():
        sum+=i
    return sum

print(sumRet(a=45,b=56,c=88))
print(sumRet(a=45,b=56,c=88,d=20))
print(sumRet(a=45,b=56,c=88,d=20,e=45))
print(sumRet(a=45,b=56))
