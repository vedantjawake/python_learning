# 🐍 Python Learning

> **My Python Learning Journey — From Basics to Advanced**

Welcome to my **Python Learning** repository! 🚀

This repository contains my Python practice programs, notes, and mini projects as I learn Python step by step.

---

## 📚 About

The goal of this repository is to:

- Learn Python from scratch
- Build strong programming fundamentals
- Practice coding every day
- Create mini projects
- Prepare for internships and technical interviews

---

## 🛠️ Tech Stack

- Python 3
- Visual Studio Code
- Git
- GitHub

---

## 📂 Repository Structure

```text
python_learning/
│
├── README.md
│
├── python_frm_basics/
│   ├── hellow.py
│   ├── variables.py
│   ├── Operator.py
│   ├── Statement.py
│   ├── String.py
│   ├── lists.py
│   └── number.py
│
└── mini_projects/
```

---

## 📖 Topics Covered

- ✅ Hello World
- ✅ Variables
- ✅ Data Types
- ✅ Operators
- ✅ Conditional Statements
- ⏳ Loops
- ⏳ Functions
- ⏳ Lists
- ⏳ Tuples
- ⏳ Dictionaries
- ⏳ Strings
- ⏳ File Handling
- ⏳ Exception Handling
- ⏳ OOP
- ⏳ Modules & Packages
- ⏳ Mini Projects

---

## ▶️ Run the Project

Clone the repository

```bash
git clone https://github.com/vedantjawake/python_learning.git
```

Go inside the project

```bash
cd python_learning
```

Run a Python file

```bash
python python_frm_basics/hellow.py
```

---

## 📈 Progress

| Topic | Status |
|-------|--------|
| Python Setup | ✅ |
| Hello World | ✅ |
| Variables | ✅ |
| Operators | ✅ |
| Statements | ✅ |
| Strings | ⏳ |
| Lists | ⏳ |
| Functions | ⏳ |
| OOP | ⏳ |

---

## 🎯 Future Goals

- Build Calculator
- Number Guessing Game
- Password Generator
- File Manager
- Weather App
- Flask Projects
- FastAPI Projects
- Automation Scripts
- AI Projects

---

## 🤝 Contributing

Suggestions and improvements are always welcome.

---

## ⭐ Support

If you found this repository helpful,

- ⭐ Star this repository
- 🍴 Fork it
- 📢 Share it with your friends

---

## 👨‍💻 Author

**Vedant Jawake**

- 🎓 MCA Student
- 💻 Aspiring Software Developer
- 🚀 Learning Python & Full Stack Development

---

<div align="center">

### ⭐ Happy Coding! ⭐

Made with ❤️ by **Vedant Jawake**

</div># 🐍 Python Learning

> **My Python Learning Journey — From Basics to Advanced**

Welcome to my **Python Learning** repository! 🚀

This repository contains my Python practice programs, notes, and mini projects as I learn Python step by step.

---

## 📚 About

The goal of this repository is to:

- Learn Python from scratch
- Build strong programming fundamentals
- Practice coding every day
- Create mini projects
- Prepare for internships and technical interviews

---

## 🛠️ Tech Stack

- Python 3
- Visual Studio Code
- Git
- GitHub

---

## 📂 Repository Structure

```text
python_learning/
│
├── README.md
│
├── python_frm_basics/
│   ├── hellow.py
│   ├── variables.py
│   ├── Operator.py
│   ├── Statement.py
│   ├── String.py
│   ├── lists.py
│   └── number.py
│
└── mini_projects/
```

---

## 📖 Topics Covered

- ✅ Hello World
- ✅ Variables
- ✅ Data Types
- ✅ Operators
- ✅ Conditional Statements
- ⏳ Loops
- ⏳ Functions
- ⏳ Lists
- ⏳ Tuples
- ⏳ Dictionaries
- ⏳ Strings
- ⏳ File Handling
- ⏳ Exception Handling
- ⏳ OOP
- ⏳ Modules & Packages
- ⏳ Mini Projects

---

## ▶️ Run the Project

Clone the repository

```bash
git clone https://github.com/vedantjawake/python_learning.git
```

Go inside the project

```bash
cd python_learning
```

Run a Python file

```bash
python python_frm_basics/hellow.py
```

---

## 📈 Progress

| Topic | Status |
|-------|--------|
| Python Setup | ✅ |
| Hello World | ✅ |
| Variables | ✅ |
| Operators | ✅ |
| Statements | ✅ |
| Strings | ⏳ |
| Lists | ⏳ |
| Functions | ⏳ |
| OOP | ⏳ |

---

## 🎯 Future Goals

- Build Calculator
- Number Guessing Game
- Password Generator
- File Manager
- Weather App
- Flask Projects
- FastAPI Projects
- Automation Scripts
- AI Projects

---

## 🤝 Contributing

Suggestions and improvements are always welcome.

---

## ⭐ Support

If you found this repository helpful,

- ⭐ Star this repository
- 🍴 Fork it
- 📢 Share it with your friends

---

## 👨‍💻 Author

**Vedant Jawake**

- 🎓 MCA Student
- 💻 Aspiring Software Developer
- 🚀 Learning Python & Full Stack Development

---

<div align="center">

### ⭐ Happy Coding! ⭐

Made with ❤️ by **Vedant Jawake**

</div>


thi is an practic of my interview that short look 
# Python Essentials: Must-Know Concepts

## 1. Variables & Data Types

Variables store data. Python automatically detects the data type.

```python
# Integers
age = 25
count = -10

# Floats (decimals)
height = 5.9
price = 19.99

# Strings (text)
name = "Alice"
message = 'Hello World'
multiline = """This is
a multiline
string"""

# Booleans (True/False)
is_active = True
is_completed = False

# Check data type
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(is_active))  # <class 'bool'>

# Type conversion
num_str = "42"
num_int = int(num_str)  # 42
num_float = float(num_str)  # 42.0
```

---

## 2. If/Else Conditionals

Execute code based on conditions.

```python
age = 20

# Basic if/else
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# if/elif/else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")  # Grade: B

# Comparison operators
print(10 > 5)  # True
print(10 >= 10)  # True
print(10 == 10)  # True
print(10 != 5)  # True

# Logical operators
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 13 or age > 65:
    print("Special category")

if not has_license:
    print("Must get a license")

# Ternary operator (one-liner if/else)
status = "Adult" if age >= 18 else "Minor"
```

---

## 3. Loops: For & While

Repeat code multiple times.

```python
# FOR LOOP
print("=== FOR LOOPS ===")

# Iterate over a range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate from 2 to 5 (stop is exclusive)
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# Iterate with step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")  # 0: apple, 1: banana, 2: cherry

# Nested loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

# WHILE LOOP
print("\n=== WHILE LOOPS ===")

count = 0
while count < 5:
    print(count)
    count += 1  # 0, 1, 2, 3, 4

# break: exit the loop
while True:
    password = input("Enter password: ")
    if password == "1234":
        print("Correct!")
        break
    print("Try again")

# continue: skip to next iteration
for i in range(5):
    if i == 2:
        continue  # Skip when i == 2
    print(i)  # 0, 1, 3, 4
```

---

## 4. Functions

Reusable blocks of code.

```python
# Basic function
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Hello, Alice!

# Multiple parameters
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Default parameters
def greet_formal(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_formal("Alice")  # Hello, Alice!
greet_formal("Bob", "Hi")  # Hi, Bob!

# Keyword arguments
def describe_car(brand, color, year):
    print(f"{year} {brand} in {color}")

describe_car(brand="Toyota", color="red", year=2020)
describe_car("Honda", year=2022, color="blue")

# Variable-length arguments
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4, 5)  # Prints 1-5

# Keyword arguments (dictionary-like)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Return multiple values (as tuple)
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)  # 10, 20

# Docstring (documentation)
def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b
```

---

## 5. Lists, Tuples, Sets, Dictionaries

Different ways to store collections of data.

```python
# LISTS - Mutable (can change)
print("=== LISTS ===")
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # 1 (first element)
print(numbers[-1])  # 5 (last element)

# Slicing
print(numbers[1:4])  # [2, 3, 4] (index 1 to 3)
print(numbers[:3])  # [1, 2, 3] (first 3)
print(numbers[2:])  # [3, 4, 5] (from index 2 onward)

# Modifying lists
numbers.append(6)  # Add to end
numbers.insert(0, 0)  # Insert at index
numbers.remove(3)  # Remove value
popped = numbers.pop()  # Remove & return last item

# TUPLES - Immutable (cannot change)
print("\n=== TUPLES ===")
coordinates = (10, 20)
print(coordinates[0])  # 10
# coordinates[0] = 5  # Error! Can't modify

# Tuple unpacking
x, y = coordinates
print(x, y)  # 10, 20

# SETS - Unique, unordered, no duplicates
print("\n=== SETS ===")
unique_numbers = {1, 2, 2, 3, 3, 3}
print(unique_numbers)  # {1, 2, 3}

fruits = {"apple", "banana", "cherry"}
fruits.add("date")  # Add element
fruits.remove("apple")  # Remove element

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a & set_b)  # {3} - intersection
print(set_a | set_b)  # {1, 2, 3, 4, 5} - union
print(set_a - set_b)  # {1, 2} - difference

# DICTIONARIES - Key-value pairs
print("\n=== DICTIONARIES ===")
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

print(person["name"])  # Alice
print(person.get("age"))  # 25
print(person.get("email", "not found"))  # not found (default)

# Modifying dictionaries
person["age"] = 26  # Update value
person["email"] = "alice@example.com"  # Add new key
del person["city"]  # Delete key

# Iterate through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

for key in person.keys():
    print(key)

for value in person.values():
    print(value)
```

---

## 6. List Comprehension

Create lists concisely using a single line.

```python
# Traditional way
squares_traditional = []
for i in range(5):
    squares_traditional.append(i ** 2)
print(squares_traditional)  # [0, 1, 4, 9, 16]

# List comprehension (shorter)
squares = [i ** 2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

# Transforming strings
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(uppercase)  # ['HELLO', 'WORLD', 'PYTHON']

# Nested list comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(matrix)
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Dictionary comprehension
squares_dict = {i: i ** 2 for i in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}
print(unique_lengths)  # {2, 5}
```

---

## 7. Lambda Functions

Anonymous (unnamed) functions, typically one-liners.

```python
# Traditional function
def add(a, b):
    return a + b

# Lambda equivalent
add_lambda = lambda a, b: a + b
print(add_lambda(5, 3))  # 8

# Lambda with single argument
square = lambda x: x ** 2
print(square(4))  # 16

# Common use: with map(), filter(), sorted()

# MAP - Apply function to each item
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# FILTER - Keep items that return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6, 8]

# SORTED - Sort with custom logic
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]
sorted_by_score = sorted(students, key=lambda s: s["score"])
print(sorted_by_score)
# Sorted by score: Charlie (78), Alice (85), Bob (92)

# Sort in reverse
sorted_descending = sorted(numbers, key=lambda x: -x)
```

---

## 8. Exception Handling

Handle errors gracefully instead of crashing.

```python
# TRY-EXCEPT
print("=== BASIC TRY-EXCEPT ===")

try:
    num = int("abc")  # This will raise an error
except ValueError:
    print("Cannot convert to integer")

# Multiple except blocks
try:
    result = 10 / 0  # ZeroDivisionError
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")

# ELSE - runs if no exception occurs
try:
    num = int("42")
    print(num)
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful")  # This prints

# FINALLY - always runs
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always close file

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return "Valid age"

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")

# Custom exception
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money")
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
```

---

## 9. File Handling

Read and write files.

```python
# READING FILES
print("=== READING FILES ===")

# Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline

# Read all lines as list
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines[0])

# WRITING FILES
print("\n=== WRITING FILES ===")

# Write mode (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line")

# Append mode (adds to existing content)
with open("output.txt", "a") as file:
    file.write("\nThird line")

# Write multiple lines
data = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w") as file:
    file.writelines([line + "\n" for line in data])

# JSON files
import json

# Write JSON
person = {"name": "Alice", "age": 25, "city": "NYC"}
with open("person.json", "w") as file:
    json.dump(person, file)

# Read JSON
with open("person.json", "r") as file:
    loaded_person = json.load(file)
    print(loaded_person)

# CSV files
import csv

# Write CSV
rows = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"]
]
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# File modes
# "r" - read (default)
# "w" - write (overwrites)
# "a" - append
# "x" - create
# "b" - binary (e.g., "rb", "wb")
```

---

## 10. Modules & Packages

Reuse code from libraries and organize your code.

```python
# IMPORTING MODULES
print("=== IMPORTING ===")

# Import entire module
import math
print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.14159...

# Import specific items
from math import sqrt, pi
print(sqrt(25))  # 5.0
print(pi)  # 3.14159...

# Import with alias
import math as m
from math import sqrt as square_root
print(m.sqrt(9))  # 3.0
print(square_root(4))  # 2.0

# Import everything (not recommended)
from math import *
print(cos(0))  # 1.0

# Common built-in modules
import random
print(random.randint(1, 10))  # Random number 1-10
print(random.choice(["a", "b", "c"]))  # Random choice

import datetime
now = datetime.datetime.now()
print(now)  # Current date and time

import os
print(os.getcwd())  # Current directory
print(os.listdir("."))  # Files in current directory

# Create your own module (save as my_utils.py)
# def add(a, b):
#     return a + b
# 
# def multiply(a, b):
#     return a * b

# Then use it:
# from my_utils import add, multiply
# print(add(5, 3))

# Python packages are directories with __init__.py
# Structure:
# my_package/
#   __init__.py
#   module1.py
#   module2.py
#   subpackage/
#     __init__.py
#     module3.py

# Import from package:
# from my_package.module1 import function_name
# from my_package.subpackage.module3 import another_function
```

---

## 11. Object-Oriented Programming (OOP)

Create structured, reusable code using classes.

```python
# CLASS - Blueprint for creating objects
print("=== CLASSES & OBJECTS ===")

class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor - runs when object is created
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age
    
    # Methods
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def get_age(self):
        return self.age
    
    # String representation
    def __str__(self):
        return f"Dog named {self.name}, age {self.age}"

# Create objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Buddy
print(dog1.age)  # 3
dog1.bark()  # Buddy says: Woof!
print(dog1)  # Dog named Buddy, age 3

# INHERITANCE - Child class inherits from parent
print("\n=== INHERITANCE ===")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):  # Cat inherits from Animal
    def make_sound(self):  # Override method
        print(f"{self.name} meows")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} chirps")

cat = Cat("Whiskers")
cat.make_sound()  # Whiskers meows

bird = Bird("Tweety")
bird.make_sound()  # Tweety chirps

# POLYMORPHISM - Same method, different behavior
animals = [cat, bird, Dog("Rex", 2)]
for animal in animals:
    animal.make_sound()

# ENCAPSULATION - Hide internal details
print("\n=== ENCAPSULATION ===")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private (double underscore)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount")
    
    def get_balance(self):  # Getter
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # Error! Private

# CLASS METHODS & STATIC METHODS
print("\n=== SPECIAL METHODS ===")

class Circle:
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    @staticmethod
    def is_circle_valid(radius):
        return radius > 0
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
    def area(self):
        return self.pi * self.radius ** 2

# Using static method
print(Circle.is_circle_valid(5))  # True

# Using class method
circle = Circle.from_diameter(10)
print(circle.radius)  # 5.0
print(circle.area())  # 78.5397...
```

---

## 12. Iterators & Generators

Efficient ways to handle sequences of data.

```python
# ITERATORS - Objects with __iter__ and __next__
print("=== ITERATORS ===")

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)  # Create iterator

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# Using in a loop
for num in numbers:
    print(num)
# This works because lists are iterable (have __iter__)

# Custom iterator
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.max:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

counter = CountUp(3)
for num in counter:
    print(num)  # 1, 2, 3

# GENERATORS - Functions that yield values one at a time
print("\n=== GENERATORS ===")

def count_up(n):
    i = 1
    while i <= n:
        yield i  # Pause and return value
        i += 1

# Generator is lazy - doesn't compute all at once
gen = count_up(5)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# Use in loop
for num in count_up(3):
    print(num)  # 1, 2, 3

# Generator expression (like list comprehension)
squares_gen = (i ** 2 for i in range(5))  # Parentheses, not brackets
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4

# Convert to list when needed
squares_list = list((i ** 2 for i in range(5)))
print(squares_list)  # [0, 1, 4, 9, 16]

# Real-world example: reading large files
def read_large_file(filepath, chunk_size=1024):
    with open(filepath, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# for chunk in read_large_file('bigfile.txt'):
#     process(chunk)  # Process one chunk at a time
```

---

## 13. Decorators

Modify or enhance functions/classes without changing their code.

```python
# BASIC DECORATOR
print("=== DECORATORS ===")

def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

# Using decorator
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before the function
# Hello!
# Something after the function

# Equivalent to: say_hello = my_decorator(say_hello)

# DECORATOR WITH ARGUMENTS
def my_decorator_args(func):
    def wrapper(*args, **kwargs):  # Accept any arguments
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@my_decorator_args
def add(a, b):
    return a + b

print(add(5, 3))  # Returns 8, prints before and after

# DECORATOR WITH PARAMETERS
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def print_message(msg):
    print(msg)

print_message("Hi")
# Prints "Hi" three times

# BUILT-IN DECORATORS
print("\n=== BUILT-IN DECORATORS ===")

# @staticmethod - function doesn't use self
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(5, 3))  # 8

# @classmethod - receives class as first argument
class MyClass:
    count = 0
    
    def __init__(self):
        MyClass.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# @property - access method like a variable
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(0)
print(temp.fahrenheit)  # 32.0 (accessed like variable, not method)

# PRACTICAL DECORATOR EXAMPLE
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

slow_function()  # Prints execution time
```

---

## Quick Reference Cheat Sheet

```python
# Variables
name = "Alice"

# Conditionals
if x > 5:
    pass
elif x == 5:
    pass
else:
    pass

# Loops
for i in range(10):
    pass

while x < 10:
    x += 1

# Functions
def func(a, b=default):
    return a + b

# Data Structures
list_ex = [1, 2, 3]
tuple_ex = (1, 2, 3)
dict_ex = {"key": "value"}
set_ex = {1, 2, 3}

# List Comprehension
result = [x**2 for x in range(10) if x % 2 == 0]

# Lambda
square = lambda x: x**2

# Exception Handling
try:
    pass
except Exception as e:
    pass
finally:
    pass

# File Handling
with open("file.txt", "r") as f:
    content = f.read()

# Classes
class ClassName:
    def __init__(self, param):
        self.param = param
    
    def method(self):
        pass

# Generators
def generator():
    yield value

# Decorators
@decorator
def func():
    pass
```

---

## Practice Exercises

1. **Variables & Loops**: Write a program that prints multiplication tables 1-10
2. **Functions**: Create a function that calculates factorial
3. **Lists**: Find the second largest number in a list
4. **Dictionaries**: Count word frequency in a string
5. **List Comprehension**: Create a list of squares for even numbers 0-20
6. **Exception Handling**: Build a simple calculator with error handling
7. **File Handling**: Read a file and count lines
8. **OOP**: Create a Student class with methods to add grades and calculate GPA
9. **Generators**: Create a Fibonacci generator
10. **Decorators**: Create a decorator that logs function calls

Keep coding and practicing these concepts!
