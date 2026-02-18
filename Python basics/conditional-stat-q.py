# x=int(input("Enter a number: "))
# if x==1:
#     print("January")
# elif x==2:
#     print("February")
# elif x==3:
#     print("March")
# elif x==4:
#     print("April")
# elif x==5:
#     print("May")
# elif x==6:
#     print("June")
# elif x==7:
#     print("July")
# elif x==8:
#     print("August")
# elif x==9:
#     print("September")
# elif x==10:
#     print("October")
# elif x==11:
#     print("November")
# elif x==12:
#     print("December")
# else:
#     print("Invalid month number")




x=input("Enter the first name: ")
y=input("Enter the surname: ")


if(x==y):
    print("Both names are equal")
else:
    print("Both names are not equal")

    if(x>y):
        print(f"{x} is greater than {y}")
    else:
        print(f"{y} is greater than {x}")

# if(x<y):  

#     print(f"{x} is smaller than {y}")
# else:
#      print(f"{y} is equal to {x}")


# x=(input("Enter the first string: "))
# y=(input("Enter the second string: "))
 
# a=int(x)
# b=int(y)

# if a is b:
#     print("Both numbers are equal")
# else:
#     print("Both numbers are not equal")



# if x>y:
#     for i in range(5):
#         print("Abhinav")
# else:
#     for i in range(3):
#         print("Sharma")


# q2

# a=input("enter the first string: ")
# b=input("enter the second string: ")

# if(a==b):
#     print("Both names are same")
# else:
#     print("Both names are not equal")

# if(a is b):
#     print("both are equal")
# else:
#     print("both are not equal")


# x=4
# sum=0
# for i in range(1,x+1):
#     sum=sum+i
# print(f"The sum of first {x} numbers is: {sum}")


# x=int(input("Enter a number: "))
# print("even number upto",x,"are:")
# for i in range(1,x+1):
#     if i%2==0:
#         print(i)


# x=int(input("Enter a number: "))
# op=input("enter the opertor (+ or -): ")
# if op=='+':
#  for i in range(0,x):
#     print(i)
# elif op=='-':
#     for i in range(x,0,-1):
#         print(i)
#     else:
#         print("not valid operator")




# python beginner practice questions

# IF–ELSE / ELIF Questions

# 1. Write a program that takes a number from the user and checks whether it is
# even or odd.

# x=int(input("Enter a number: "))
# if x%2==0:
#     print(f"{x} is even")
# else:
#     print(f"{x} is odd")




# 2. Take a number as input and print Positive, Negative, or Zero.

# x=int(input("Enter a number: "))
# if x>0:
#     print(f"{x} is Positive")
# elif x<0:
#     print(f"{x} is Negative")
# else:
#     print("The number is Zero")




# 3. Take two numbers from the user and print the greater number. If both areequal, print 'Both are equal'.

# x=int(input("Enter first number: "))
# y=int(input("Enter second number: "))

# if x>y:
#     print(f"{x} is greater")
# elif y>x:
#     print(f"{y} is greater")
# else:
#     print("Both are equal")


# 4. Take marks as input and print grade: A (>=90), B (>=75), C (>=50), Fail (<50).

# marks=int(input("Enter your marks: "))
# if marks>=90:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# elif marks>=50:
#     print("Grade C")
# elif marks<50:
#     print("Fail")
# else:
#     print("Invalid marks")    

# 5. Take a character from the user and check whether it is a vowel or a
# consonant.

# char=input("Enter a character: ")
# if char in ['a','e','i','o','u']:
#     print(f"{char} is a vowel") 
# else:
#     print(f"{char} is a consonant")


# FOR Loop Questions
# 1. Print numbers from 1 to 10 using a for loop.


# x=int(input("Enter a number: "))
# for i in range(1,x+1):
#     print(i)



# 2. Take a number n and calculate the sum of numbers from 1 to n.

# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(f"The sum of first {n} numbers is: {sum}")



# 3. Take a number and print its multiplication table up to 10.

# n=int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")



# 4. Take a string and count the number of characters using a for loop.

# x=input("Enter a string: ")
# count=0
# for char in x:
#     count+=1
# print(f"The number of characters in the string is: {count}")



# 5. Print all even numbers between 1 and 20

# x=int(input("Enter a number: "))
# for i in range(1,x+1):
#     if i%2==0:
#         print(i)





# while Loop Questions


# x=int(input("Enter a number: "))
# count=1
# while count<=x:
#     print(count)
#     count+=1



# x=int(input("Enter a number: "))
# sum=0
# while x!=0:
#     sum=sum+x
#     x=int(input("Enter a number: "))
# print(f"The sum is: {sum}")




# x=int(input("Enter a number: "))
# count=10
# while count>=x:
#     print(count)
#     count-=1



# a=3
# while True:
#     x=int(input("Enter your guess: "))
#     if x==a:
#         print("Congratulations! You guessed it right.")
#         break
#     else:
#         print("Try again.")



# x=5
# i=1
# while i<=50:
#     print(f"{x} x {i} = {x*i}")
#     i=i+1



# nested loops questions


# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()






# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end='')
#     print()



# 1
# 22
# 333
# 4444
# 55555

# n=5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i, end="")
#     print()



# Question 1: Write a program to print a 5x5 multiplication table using nested loops

# x=int(input("Enter a number: "))
# for i in range(1,x+1):
#     for j in range(1,x+1):
#         print(f"{i*j}", end="\t")
#     print()




# Question 2: Create a nested loop to print a pyramid pattern with stars (*)

# n=5
# for i in range(1, n+1):
#     for j in range(1,n-i+1):
#         print(" ", end=" ")
#     for x in range(1, i+1):
#             print("*", end=" ")
#     print()





# Question 3: Write nested loops to find all pairs of numbers from 1-10 that sum to 15

# for i in range(1,11):
#      for j in range(1,11):
#           if i+j==15:
#                print(f"{i}, {j}")





# Question 4: Use nested loops to print a checkerboard pattern of alternating characters

# n=8
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i+j)%2==0:
#             print("X", end=" ")
#         else:
#             print("O", end=" ")
#     print()



# Question 5: Write nested loops to find the largest element in a 2D list/matrix






# Question 6: Create nested loops to generate all combinations of numbers 1-5 taken 2 at a time






# Question 7: Use nested loops to print the multiplication table for numbers 1-12 in a formatted grid