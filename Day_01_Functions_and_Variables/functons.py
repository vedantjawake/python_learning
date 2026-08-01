# functions.py

# Simple function
def say_hello():
    print("Hello, Vedant!")


# Function with parameters
def greet(name):
    print(f"Hello, {name}!")


# Function with return value
def add(a, b):
    return a + b


# Function with default parameter
def introduce(name, city="Amravati"):
    return f"My name is {name} and I live in {city}."


# Main program
def main():
    say_hello()
    greet("Vedant")

    result = add(10, 20)
    print("Sum:", result)

    print(introduce("Vedant"))
    print(introduce("Rahul", "Pune"))


if __name__ == "__main__":
    main()
        





