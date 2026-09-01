```python
# What is Python & Why Use It
print("Hello, World!")

# Variables and Data Types
name = "Alex"
age = 22
height = 5.9
is_student = True
skills = ["Python", "Flask", "MySQL"]
info = {"course": "AI", "year": "final"}

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(skills))
print(type(info))

# Type Conversion
a = 5
b = 2.5
c = a + b
print(c)
print(type(c))

num_str = "100"
num_int = int(num_str)
print(num_int, type(num_int))

x = 10
y = float(x)
print(y, type(y))

age_str = str(age)
print(age_str, type(age_str))

price = float("99.99")
print(price, type(price))

# Input & Output
print("Hello there!")
print("Age:", 22)
print("Sum =", 5 + 3)
print(f"My name is {name} and I am {age} years old.")

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print(f"Hello {user_name}, you are {user_age} years old.")

user_age = int(input("Enter your age: "))
next_year = user_age + 1
print(f"Next year, you'll be {next_year} years old.")
```


Python Basics: Data Types & I/O
Data Types
int – whole number → age = 25
float – decimal number → price = 99.99
string – text → city = "Delhi"
bool – True/False → is_active = True

Check any type with type(variable).

Input & Output

print() → displays output

python
print("Hello, World!")

input() → takes user input (always returns a string)

python
name = input("Enter your name: ")
print("Hello,", name)

Converting input to numbers:

python
age = int(input("Enter your age: "))
print("Next year:", age + 1)
