# 1. Function without parameters
def hello():
    print("Hello World")

# 2. Function with parameters
def greet(name):
    print(f"Hello, {name}")

# 3. Function with multiple parameters
def add(a, b):
    return a + b

# 4. Function with default parameter
def country(name, place="India"):
    print(name, "is from", place)

# 5. Function with keyword arguments
def student(name, age):
    print(name, age)

# 6. Function with arbitrary arguments (*args)
def total(*numbers):
    print(sum(numbers))

# 7. Function with keyword arbitrary arguments (**kwargs)
def info(**details):
    for key, value in details.items():
        print(key, ":", value)

# 8. Lambda function
square = lambda x: x * x

# 9. Recursive function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# 10. Nested function
def outer():
    def inner():
        print("Inner Function")
    inner()

# 11. Anonymous function example
cube = lambda x: x ** 3

# ===============================
# Main Function
# ===============================

def main():
    hello()
    greet("Vedant")
    print(add(10, 20))
    country("Vedant")
    student(age=23, name="Vedant")
    total(10, 20, 30, 40)
    info(name="Vedant", city="Amravati", course="MCA")
    print(square(5))
    print(cube(3))
    print(factorial(5))
    outer()

    

if __name__ == "__main__":
    main()