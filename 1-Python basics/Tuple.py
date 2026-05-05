# # tuple - (), ordered, indexed, immutable(cannot change during run time)
# l=("Hello",)
# print(type(l))


# a=12,13,14
# print(type(a))  

# # t=()
# t=(12,)  # tuple # without comma isski datatype - jo data hai wahhi type hai  
# print(type(t))
# t2=(12,13)
# print(type(t2))

# t1=(12,'hello', True, 7.89,45,22,11,10)
# print(t1)

# # slicing 
# print(t1[:])
# print(t1[1:5])
# print(t1[1:5:2])
# print(t1[1:5:2])

# print('print',t1[1::-1]) # 0 => stop-1 => 0-1



 #'tuple' object does not support item assignment
# t1[2]=10

# print(t1)
# t1= list(t1)
# t1[3]=100
# print(t1)
# t1.insert(2,350)
# t1=tuple(t1)
# print(t1)