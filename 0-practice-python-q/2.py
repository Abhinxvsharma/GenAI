# 1 . Check Prime Number

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a Prime Number")
# else:
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num, "is a Prime Number")
#     else:
#         print(num, "is Not a Prime Number")

# 2 .Fibonacci Series Generator

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    
c = a + b
a = b
b = c
  