# Sets  - {}, heterogenous, unique elements, unordered 

#s =set() # sets can be defined using the following function

# set1={23,45,True,'hi','surbhi',45,6.78,100}
# print(set1)

# s=set()
# print(type(s))

# print("--------after add")
# set1.add(33)
# print(set1)

# print("--------after update")
# set1.update({38,99,88})
# set1.update([38,99,88])
# set1.update([99])
# print(set1)

# print("----------after pop")
# set1.pop()
# print(set1)
# set1.pop()
# print(set1)

# set1.remove()  # raise error if value is not present
# print(set1)

# # set1.remove(122)
# # print(set1)

# set1.discard(122) #does not raise error if value is not present
# print(set1)

# set1.discard(25)
# print(set1)

# frozen sets 
#These are the sets that are immutable 

# s= frozenset(("a","b","c","d"))
# print(s)
# s.add("e")
# print(s)

# methods in sets
#1. Union
# setA={1,2,3,4,5}
# setB={4,5,6,7,8}
# setC= setA.union(setB)
# print("Union:",setC)

# # 2. Intersection
# setD= setA.intersection(setB)
# print("Intersection:",setD) 

# # 3. Difference 
# setE= setA.difference(setB)
# print("Difference:",setE)

# # 4. Symmetric Difference
# setF= setA.symmetric_difference(setB)
# print("Symmetric Difference:",setF)

# # 5. Subset
# setG={1,2}
# is_subset= setG.issubset(setA)
# print("Is Subset:",is_subset)

# # 6. Superset
# is_superset= setA.issuperset(setG)
# print("Is Superset:",is_superset)

# # 7. Disjoint
# setH={9,10} #setA={1,2,3,4,5}
# is_disjoint= setA.isdisjoint(setH)
# print("Is Disjoint:",is_disjoint)
# # # 8. Copy
# # setI= setA.copy()