# a constructor is a special method that is called automatically when an object is created from a class. Its main role is to initialize the object by setting up its attributes or state.20

students_details=[]
class Student:
    # print("Hello class")
    def __init__(self,n,r): 
        # print("Hello this is constructor")
        # print(self)
        self.name=n 
        self.rollno=r
        print(f"Name is {self.name} and rollno is {self.rollno}")
        pass 
    def getPriyanshu(self):
        self.name=input("Enter Name ")
        self.rollno=int(input("Enter Rollno "))  
    def printValues(self):
        # print(f"Name is {self.name} and rollno is {self.rollno}")
        students_details.append({self.name:self.rollno})
        
# stu1=Student()
# stu2=Student()
# stu1.getPriyanshu()
# stu2.getPriyanshu()

# # stu2.printValues()
# # # stu1.printValues()



stu1=Student("Sourav",12) 
stu2=Student("Arsh",13) 
print(stu1)
print(stu2)
stu1.printValues()
stu2.printValues()
print(students_details)
stu1.getPriyanshu()
stu2.getPriyanshu()

stu1.printValues()
stu2.printValues()
print(students_details)



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

        