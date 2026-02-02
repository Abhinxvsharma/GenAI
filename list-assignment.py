# 1.   Create a list with 5 friends and ask user a friend name and
# add that name in the friend list,
# and print the list
# after that ask user to most important friend and add that friend
# at user choice

# x=input('Enter friend name: ')
# l=['ram','sham','papu','kaka','pritam']
# l.append(x)
# print(l)
# y=input('Most imp friend: ')
# z=int(input('Friend location: '))
# l.insert(z,y)
# print(l)




# 2. Create a list of first 10 natural numbers

# l=[1,2,3,4,5,6,7,8,9,10]
# print(l)


# 3.  Create a list [1,10,100,3,6,8] and add 59 on 3 location after
# that append 5 and print list and length of list

# l=[1,10,100,3,6,8]
# l.insert(3,59)
# l.append(5)
# print(l)
# print(len(l))   

#4. Find all of the words in a list of strings that are less than 4 letters


# x = ["cat", "dog", "elephant", "bird", "butterfly"]
# y = [i for i in x if len(i) < 4]
# print(y)

#5 Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,'even',........ 

# x = range(20)
# y = ['even' if i % 2 == 0 else 'odd' for i in x]
# print(y)

#6 Find all of the numbers from 1-1000 that are divisible by 7 
# n=[]
# for i in range(1,1000):
#     if i%7==0:
#         n.append(i)
# print(n)


#7 Count the number of spaces in a string 
# s = "my name is abhinav"
# count = s.count(' ')
# print(count)   


#8 Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]

# x = [(i,j) for i in list_a for j in list_b if i==j]
# print(x)