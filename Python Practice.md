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


Every value in Python has a type, and the type decides what operations are allowed on it.
You can add two ints directly, but adding an int to a string needs conversion first.
int(), float(), str() are the common conversion functions.
int and float are both numeric, but behave differently — dividing two ints still gives a float (5 / 2 = 2.5).
Strings support + for joining and * for repeating, e.g. "Hi" * 3 → "HiHiHi".
Booleans are a subtype of int — True acts like 1, False acts like 0.
So True + True equals 2.
input() pauses the program and waits for the user to type and press Enter.
Whatever input() returns is always a string, even if it looks like a number.
That's why numeric input usually needs int() or float() before doing math on it.
print() can take multiple values separated by commas.
It automatically adds a space between them and a newline at the end.
Both behaviors can be changed using the sep and end parameters.