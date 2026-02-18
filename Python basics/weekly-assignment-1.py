# q1
# for i in range(1,51):
#     if i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%3==0 and i%5==0:
#         print("FizzBuzz")



# q2 Write a program to print all prime numbers between 1 and 100


# for i in range(1,101):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print("Prime",i)
    


#q3 
# x=int(input("Enter the first number: "))
# if x>90:
#     print("A grade")
# elif x>80:
#     print("B grade")
# elif x>70:
#     print("C grade")    
# elif x>60:
#     print("D grade")
# else:
#     print("F grade")

# q4

# x=int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{x} x {i} = {x*i}")

# q5

# x=int(input("Enter the number: "))
# y=[i**2 for i in range(1,x+1) if i%2==0]
# print(y)
 
#  q6

# x=int(input("Enter the number: "))
# if x%4==0:
#     print("Leap year")
# elif x%100==0:
#         print("Not a leap year")
# elif x%400==0:
#         print("Leap year")
# else:
#     print("Not a leap year")

# q7  Write a program that takes the lengths of three sides of a triangle as input and determines the type of triangle (equilateral, isosceles,  scalene or right angle tringle ).
# solutions:

# a=float(input("Enter the length of side a: "))
# b=float(input("Enter the length of side b: "))
# c=float(input("Enter the length of side c: "))
# if a==b==c:
#     print("Equilateral triangle")
# elif a==b or b==c or a==c:
#     print("Isosceles triangle")
# elif (a**2+b**2==c**2) or (b**2+c**2==a**2) or (a**2+c**2==b**2):
#     print("Right angle triangle")
# else:
#     print("Scalene triangle")


#q8
# x=int(input("Enter the number: "))
# if x<0:
#     print("Negative number")
# elif x>0:
#     print("Positive number")    
# else:
#     print("Zero")


# q10

# BMI=(float(input("Enter your weight in kg: ")))
# if BMI<18.5:
#     print("Underweight")
# elif BMI>=18.5 and BMI<24.9:
#     print("Normal weight")
# elif BMI>=25 and BMI<29.9:
#     print("Overweight")
# else:
#     print("Obesity")


# q11

# x=int(input("Enter the day:"))

# if x==1:
#     print("Monday")
# elif x==2:
#     print("Tuesday")
# elif x==3:
#     print("Wednesday")
# elif x==4:
#     print("Thursday")
# elif x==5:
#     print("Friday")
# elif x==6:
#     print("Saturday")
# elif x==7:
#     print("Sunday")
# else:
#     print("Invalid input")


# q12
# x=int(input("Enter the number: "))
# if x>1000:
#     discount=x*0.1
#     final_price=x-discount
#     print(f"Final price after discount is: {final_price}")
# elif x>500:
#     discount=x*0.05
#     final_price=x-discount
#     print(f"Final price after discount is: {final_price}")
# else:
#     print(f"No discount applicable. Final price is: {x}")


# q13 
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# q14



# q15
# x=input("Enter the string: ")
# count=0
# for i in x:
#     if i in 'aeiouAEIOU':
#         count=count+1
# print("Number of vowels in the string is:",count)

# q16

# x=int(input("Enter the number: "))

# sum=0
# while x>0:
#     digit=x%10
#     sum=sum+digit
#     x=x//10
# print("Sum of digits is:",sum)

# q17

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()


# q18  

from random import random


a=random.randint(1,100)
print("Guess the number between 1 and 100")
while True:
    guess=int(input("Enter your guess: "))
    if guess<a:
        print("Too low! Try again.")
    elif guess>a:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break

# q19

# x=int(input("Enter the number: "))
# print([i for i in range(1,x+1) if i%2==0])

# q20

# x=[2,34,45,22,36,25,25,10,8,15]
# if 25 in x:
#     print("25 is exist")
# else:
#     print("25 is not exist")

# y=len(x)
# print("Length of the list is:",y)

# print(x.count(25))

# for i in x:
#     print(i)

# z=[i for i in x if i%2==0]
# print("even number in list is:",z)



# q21




# def odd_even(a):
#     if a%2==0:
#         return("Even number")
#     else:   
#         return("Odd number")

# b=int(input("enter the value: "))

# print(odd_even(b))