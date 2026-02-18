# 1. What will be the output of the following code?

# x = 10
# y = 3
# print(x // y, x / y)

# Explain the difference between the two operators.
# ans-- modulas operator , division operator


# 2. Predict the output:

# a = 5
# b = 10
# print(a > 3 and b < 5)

# Why does the expression evaluate to this result?
# ans-- false first operator is true and second is false so and operator gives false 


# 3. What is the result of this expression?

# print(2 ** 3 ** 2)

# Explain how operator precedence works here.
# ans--512 first 3**2 then 2**9


# 4. What will be printed?

# x = 4
# x += 3 * 2
# print(x)

# Why does this happen?
# ans--10 because multiplication has higher precedence than addition so first 3*2=6 then 4+6=10


# 5. Predict the output:

# print(not True == False)

# Explain how `not` and `==` are evaluated.
# ans-- true 


# 6. What is the output?

# a = 5
# b = 5
# print(a is b)

# Is it always safe to use `is` for comparing numbers? Why or why not?
# ans-- 'is' 256 taq hi check krda a, agar zada hoi value tn false output deni  --- 'is' di jagah '==' use krna chahida a


# 7. What will this code output?

# print(5 & 3)

# Explain how bitwise AND works.
# ans-- 5= 101 , 3=011 , and operation krn te 001 bnda a , jo decimal vich 1 hunda a 


# 8. Predict the result:

# x = 7
# print(x > 5 or x < 3 and x == 7)

# Explain operator precedence in logical operators.
# ans-- true


# 9. What is the data type of the following?

# x = [1, 2, 3]
# y = (1, 2, 3)
# z = {1, 2, 3}

# Explain one key difference between them.
# ans-- x=list, y=tuple, z=set


# 10. What will be the output?

# x = "10"
# y = 5
# print(x * y)

# Why doesn’t this cause an error?
# ans-- "10" is string , 5 is int


# 11. Predict the output:

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# Explain what is happening in memory.
# ans-- append means insert krna


# 12. What will be printed?

# x = 10
# y = 10.0
# print(type(x) == type(y))

# Why is the result True or False?
# ans--false , first is int and second is float


# 13. What is the output?

# print(bool(""))
# print(bool(0))
# print(bool("False"))

# Explain Python’s truthy and falsy values.
# ans-- pehla and second falsy a , third truthy a kyoki non empty string a


# 14. Predict the result:

# data = {"a": 1, "b": 2}
# print("a" in data)
# print(1 in data)

# Why do these statements behave differently?
# ans-- "a" in data checks if the key "a" exists in the dictionary, which returns True.
# 1 in data checks if the value 1 exists in the dictionary, which returns False because 1 is a value, not a key.


# 15. What will be the output?

# x = None
# print(type(x))
# print(x == None)
# print(x is None)

# Which comparison is recommended and why?
# ans-- <class 'NoneType'>, true , true , 'is' operator is recommended for comparing with None because it checks for identity, ensuring that you are checking if the variable points to the None object itself.

