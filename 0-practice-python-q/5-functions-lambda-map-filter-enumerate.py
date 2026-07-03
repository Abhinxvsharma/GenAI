# Part 1: Basic Functions & Arguments

def multiply_numbers(num1, num2=10):
    return num1 * num2


print("Multiply (5, 4):", multiply_numbers(5, 4   ))
print("Multiply (7):", multiply_numbers(7))


def sum_all(*args):
    total = 0

    for num in args:
        total = total + num

    return total


print("Sum all (1,2,3):", sum_all(1, 2, 3))
print("Sum all (10,20,30,40):", sum_all(10, 20, 30, 40))


def top_student(**kwargs): 
    highest = max(kwargs, key=kwargs.get)
    return highest


print("Top Student:", top_student(alice=85, bob=92, charlie=78))


# Part 2: Lambda Functions

uppercase = lambda text: text.upper()

print("Uppercase String:", uppercase("hello world"))


# Part 3: Map, Filter, and Enumerate

mixed_list = [1, "hello", 3.14, "world", 42]

filtered_strings = list(filter(lambda x: isinstance(x, str), mixed_list))

print("Filtered Strings:", filtered_strings)


celsius_temps = [0, 20, 37, 100]

fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius_temps))

print("Fahrenheit Temps:", fahrenheit)


words = ["apple", "bat", "cat", "elephant"]

word_dict = {}

for index, word in enumerate(words, start=1):
    if len(word) > 4:
        word_dict[index] = word

print("Enumerated Words:", word_dict)


# Part 4: Combining Special Functions

numbers = list(range(1, 21))

squared_even_numbers = list(
    map(
        lambda x: x * x,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print("Squared Even Numbers:", squared_even_numbers)