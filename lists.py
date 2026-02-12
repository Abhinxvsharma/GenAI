# list - data Type - multiple data types ki values 
# [], indexed based, ordered, mutable(can change during run time)

# l=[23,56,'hello',9.8,True,21,12,'hi',99.1]
# print(l)
# print(type(l))

# print(l)
# slicing 
# print(l[:]) # start:stop:step
# print(l[:5]) 
# print(l[1:])
# print(l[3:10])
# print(l[::]) # step
# print(l[::1]) # step
# print(l[::2]) # step

# print(l[10:1:-1])   # stop-1 = 1-(-1)

# methods and functions 
# l=[34,56,12,11,10,56,33,20,100,59]
# print(l)

# l.insert(3,77) # index, value
# print(l)

#append and extend
# l.append(33)
# l.append([16,17,'abhinav','jasbir'])
print(l)

# l.extend([16,17,'abhinav','jasbir'])
# print(l)

# value replacement 
# l[3]=100
# print(l)

# sort a list 
# l.sort()
# print(l)

# l2=[34,'hello','Arsh',99,10]
# l2.sort()
# print(l2)  # got error 
# print("Before Pop",l)
# # l.pop()  # by default last value remove
# l.pop(4)  # by default last value remove
# # Remove and return item at index (default last).
# # Raises IndexError if list is empty or index is out of range.
# print("After Pop",l)
# print(l)
# l.remove(56)
# l.remove(51)
# # Remove first occurrence of value.
# # Raises ValueError if the value is not present.
# print(l)


# print("Reverse",l[::-1])
# l.reverse()
# print(l)


# n=[]
# for i in range(0,30):
#     if i%3==0:
#         n.append(i)
# print(n)


# zip function in list 

# a=[12,13,15,10,90,89]
# b=[4,6,8,2,8]
# for i in zip(a,b):
#     print(i)
# for i,j in zip(a,b):
#     print(i,"--",j)
    
# list comprehension 
# lc=[]
# for i in range(0,10):
#     lc.append(i)
# print(lc)


# lc= [i for i in range(0,10)]
# print(lc)




# n=[]
# for i in range(0,30):
#     if i%3==0:
#         n.append(i)
# print(n)

# n=[i for i in range(0,30) if i%3==0]
# print(n)

# eo=[i if i%2==0 else i**2 for i in range(0,20)]
# print(eo)

# eo=[i+2 for i in eo]
# print(eo)

# l1=[2,3,4,5,6]
# l2=[4,5,8,9,1]

#output - [(4,4),(5,5)]  or [4,5] 
# 1st method 
# ans=[(i,i) for i in l1 if i in l2]
# ans= [(i,j) for i in l1 for j in l2 if i==j]
# print(ans)