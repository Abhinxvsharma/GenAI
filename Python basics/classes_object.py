# a constructor is a special method that is called automatically when an object is created from a class. Its main role is to initialize the object by setting up its attributes or state.20  //__init__()

# students_details=[]
# class Student:
#     # print("Hello class")
    # def __init__(self,n,r): 
        # print("Hello this is constructor")
#         # print(self)
#         self.name=n 
#         self.rollno=r
#         print(f"Name is {self.name} and rollno is {self.rollno}")
#         pass 
#     def getPriyanshu(self):
#         self.name=input("Enter Name ")
#         self.rollno=int(input("Enter Rollno "))  
#     def printValues(self):
#         # print(f"Name is {self.name} and rollno is {self.rollno}")
#         students_details.append({self.name:self.rollno})
        
# stu1=Student()
# stu2=Student()
# stu1.getPriyanshu()
# stu2.getPriyanshu()

# # stu2.printValues()
# # # stu1.printValues()



# stu1=Student("Sourav",12) 
# stu2=Student("Arsh",13) 
# print(stu1)
# print(stu2)
# stu1.printValues()
# stu2.printValues()
# print(students_details)
# stu1.getPriyanshu()
# stu2.getPriyanshu()

# stu1.printValues()
# stu2.printValues()
# print(students_details)



# class Car:
#     def __init__(self,name,color,year):
#         self.name=name
#         self.color=color
#         self.year=year


#     def printDetails(self):
#         print(f"Car name is {self.name} and color is {self.color} and year is {self.year}")


# car1=Car("KIA","Black",2025)
# car2=Car("BMW","White",2024)


# print(car1.name)
# print(car2.color)

# car1.printDetails()

        



#------   class questions    ------

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display_details(self):
#         print("name:",self.name)
#         print("age:",self.age)

# p1=person("abhinav",21)

# p1.display_details()



# class car:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price

#     def display_detail(self):
#         print("brand:",self.brand)
#         print("price:",self.price)    

# c1=car("thar",20000)
# c1.display_detail()



# class bank_account:

#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance += amount
#         print("deposited:",amount)
#         print("new balance:",self.balance)

#     def withdraw(self,amount):
#         if amount <=self.balance:
#             self.balance-=amount
#             print("withdraw:",amount)
#             print("remaining balance:",self.balance)
#         else:
#             print("insufficient balance")

# b1=bank_account("Abhinav",1000)

# b1.deposit(500)
# b1.withdraw(300)
# b1.withdraw(1500)
        
            

# class employee:

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def increment(self):
#         self.salary += self.salary*0.10
#         print("salary after increase by 10%")
#         print("new salary:", self.salary)


# e1=employee("Abhinav",1000)

# e1.increment()
