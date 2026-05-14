# 1. check number is even or odd

# a=int(input("Enter a number= "))
# if a % 2==0:
#     print(a, "is even")
# else:
#     print(a, "is odd")     


# 2. take three input from use and find the largest number 

a=int(input('Enter the first number= '))
b=int(input('Enter the second number= '))
c=int(input('Enter the third number= '))

if a>=b and a>=c:
    print('the largest number is',a)
elif b>=a and b>=c:
    print('the largest number is',b)
elif c>=a and c>=b:
    print('the largest number is',c)

    