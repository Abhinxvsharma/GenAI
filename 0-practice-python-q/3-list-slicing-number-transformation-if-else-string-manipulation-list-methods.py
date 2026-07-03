# Part 1: List Basics & Slicing

fruits = ["Apple", "Banana", "Pineapple", "Orange", "Grapes", "Papaya"]

fruits[2] = "Mango"

print("Original Slice (first 3):", fruits[:3])
print("Last 2 fruits:", fruits[-2:])
print("Reversed list:", fruits[::-1])


# Part 2: Number Transformations (List Comprehensions)

numbers = [2, 5, 8, 11, 14, 17, 20, 25]

squares = [num * num for num in numbers]
evens = [num for num in numbers if num % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)


# Part 3: If-Else Logic in List Comprehensions

temps = [35, 12, 40, 8, 22, 45, 18]

weather = ["Hot" if temp > 30 else "Cool" for temp in temps]

print("Weather:", weather)


# Part 4: String Manipulation

names = ["alice", "bob", "charlie", "diana", "edward"]

capitalized_names = [name.upper() for name in names]
filtered_names = [name for name in names if len(name) >= 5]

print("Capitalized Names:", capitalized_names)
print("Names with 5+ chars:", filtered_names)


# Part 5: List Methods (Adding, Removing, Sorting)

my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)

my_list.insert(1, 15)

my_list.remove(20)

popped_element = my_list.pop()

unordered = [8, 3, 1, 5, 4]

unordered.sort()

print("Popped Element:", popped_element)
print("My List:", my_list)
print("Sorted Unordered List:", unordered)


# Part 6: Advanced List Comprehensions

words = ["python", "data", "science", "machine", "learning"]

word_lengths = [len(word) for word in words]

prices = [100, 250, 45, 300, 80]

discounted_prices = [price * 0.9 if price > 150 else price for price in prices]

print("Word Lengths:", word_lengths)
print("Discounted Prices:", discounted_prices)