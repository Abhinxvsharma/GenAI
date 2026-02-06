# def sum_even_numbers(n):
#     sum=0
#     for i in n:
#         if i%2==0:
#             sum+=i
#     return sum

  
# n=int(input("Enter the list size: "))
# l=[]
# for i in range(n):
#     a=int(input("enter the element "))
#     l.append(a) 

# print(l)
# print(sum_even_numbers(l))



# def is_palindrome(s):
#     return s==s[::-1]
# s=input("Enter a string: ")
# if is_palindrome(s):
#     print(f"{s} is a palindrome")
# else:
#     print(f"{s} is not a palindrome")




# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# n=int(input("Enter a number to find factorial: "))
# print(f"The factorial of {n} is {factorial(n)}")



# def second_largest(numbers):
#     if len(numbers) < 2:
#         return "List must contain at least two elements"

#     numbers.sort()          
#     return numbers[-2]      

# n= [10, 20, 30, 40, 50]

# result = second_largest(n)
# print("Second largest element is:", result)



# def list_of_tuples_to_dict(tuple_list):
#     return dict(tuple_list)
# data = [("a", 1), ("b", 2), ("c", 3)]
# result = list_of_tuples_to_dict(data)
# print(result)
