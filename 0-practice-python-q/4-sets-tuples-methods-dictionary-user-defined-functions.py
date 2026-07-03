# Question 1: Set De-duplication and Basic Operations

my_list = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = set(my_list)

even_numbers = {20, 40, 60, 80}

print("Unique:", unique_numbers)
print("Intersection:", unique_numbers.intersection(even_numbers))
print("Union:", unique_numbers.union(even_numbers))


# Question 2: Advanced Set Methods

my_set = set()

my_set.add(5)
my_set.add(10)

my_set.update([15, 20, 25])

my_set.remove(10)

print("Final Set:", my_set)
print("Is Subset:", my_set.issubset({5, 15, 20, 25, 30}))


# Question 3: Tuple Packing and Unpacking

student_info = ("Alice", 20, "A")

name, age, grade = student_info

print("Name:", name, "| Age:", age, "| Grade:", grade)

# Tuples are immutable, so values cannot be changed.
# student_info[0] = "Bob"


# Question 4: Tuple Methods and Indexing

scores = (85, 90, 85, 70, 85, 95)

print("Count of 85:", scores.count(85))
print("First index of 90:", scores.index(90))


# Question 5: Dictionary Creation and Manipulation

employee = {
    "name": "John",
    "department": "Sales",
    "salary": 50000
}

employee["salary"] = 60000

employee["role"] = "Manager"

del employee["department"]

print(employee)


# Question 6: Looping through Dictionaries

capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi"
}

print("Countries:")
for country in capitals:
    print(country)

print("Capitals:")
for capital in capitals.values():
    print(capital)

for country, capital in capitals.items():
    print("The capital of", country, "is", capital)


# Question 7: Basic Dictionary Comprehension

nums = [1, 2, 3, 4, 5]

squares_dict = {num: num * num for num in nums}

print("Squares Dict:", squares_dict)


# Question 8: Dictionary Comprehension with Conditions

marks = {
    "Alice": 85,
    "Bob": 40,
    "Charlie": 92,
    "David": 55
}

passed_students = {name: mark for name, mark in marks.items() if mark >= 60}

print("Passed Students:", passed_students)


# Question 9: User-Defined Functions (Basics)

def greet(name):
    return "Good Morning, " + name + "!"


def generate_table(n):
    table = []

    for i in range(1, 11):
        table.append(n * i)

    return table


print(greet("Alice"))
print("Table of 7:", generate_table(7))


# Question 10: Advanced Logic inside Functions

def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def remove_duplicates_and_sort(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers


print("Is 47 prime?", check_prime(47))
print("Is 10 prime?", check_prime(10))

sample_list = [5, 2, 8, 4, 2, 1, 6, 5]

print("Cleaned List:", remove_duplicates_and_sort(sample_list))