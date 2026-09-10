
# FUNCTIONS IN PYTHON - PRACTICE



# 1. Simple Function
print("1. Simple Function")

def greet():
    print("Hello, Python!")

greet()

# o/p
# Hello, Python!


# 2. Function with Parameter
print("\n2. Function with Parameter")

def greet_user(name):
    print("Hello", name)

greet_user("Alex")

# o/p
# Hello Alex


# 3. Function with Two Parameters
print("\n3. Function with Two Parameters")

def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(10, 20)

# o/p
# Sum: 30


# 4. Function with Return
print("\n4. Function with Return")

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Result:", result)

# o/p
# Result: 20


# 5. Function with Default Parameter
print("\n5. Function with Default Parameter")

def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Alex")

# o/p
# Welcome Guest
# Welcome Alex


# 6. Function with Multiple Parameters
print("\n6. Function with Multiple Parameters")

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info("Alex", 21, "Python")

# o/p
# Name: Alex
# Age: 21
# Course: Python


# 7. Function to Check Even or Odd
print("\n7. Function to Check Even or Odd")

def check_number(number):
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

check_number(12)

# o/p
# Even Number


# 8. Function to Find Square
print("\n8. Function to Find Square")

def square(number):
    return number * number

print("Square:", square(6))

# o/p
# Square: 36


# 9. Function to Find Largest Number
print("\n9. Function to Find Largest Number")

def largest(a, b):
    if a > b:
        return a
    else:
        return b

print("Largest:", largest(25, 18))

# o/p
# Largest: 25


# 10. Function with List
print("\n10. Function with List")

def show_items(items):
    for item in items:
        print(item)

numbers = [10, 20, 30, 40]
show_items(numbers)

# o/p
# 10
# 20
# 30
# 40


# 11. Function to Calculate Average
print("\n11. Function to Calculate Average")

def average(a, b, c):
    return (a + b + c) / 3

print("Average:", average(10, 20, 30))

# o/p
# Average: 20.0


# 12. Function Calling Another Function
print("\n12. Function Calling Another Function")

def add(a, b):
    return a + b

def calculate():
    result = add(10, 15)
    print("Result:", result)

calculate()

# o/p
# Result: 25


# 13. Function with Keyword Arguments
print("\n13. Function with Keyword Arguments")

def details(name, age):
    print("Name:", name)
    print("Age:", age)

details(age=22, name="Alex")

# o/p
# Name: Alex
# Age: 22


# 14. Function with *args
print("\n14. Function with *args")

def total(*numbers):
    print("Total:", sum(numbers))

total(10, 20, 30, 40)

# o/p
# Total: 100


# 15. Function with **kwargs
print("\n15. Function with **kwargs")

def information(**details):
    for key, value in details.items():
        print(key, ":", value)

information(name="Alex", age=22, course="Python")

# o/p
# name : Alex
# age : 22
# course : Python


# 16. Recursive Function
print("\n16. Recursive Function")

def countdown(number):
    if number > 0:
        print(number)
        countdown(number - 1)

countdown(5)

# o/p
# 5
# 4
# 3
# 2
# 1