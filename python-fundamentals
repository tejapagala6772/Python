# Python Fundamentals

## 1. What is Python and Why Use It

Python is a high-level, interpreted, general-purpose programming language known for its simple, readable syntax.

Reasons to use Python:

- Easy to learn and read, with minimal boilerplate
- Versatile, used in web development, AI/ML, automation, and data science
- Large ecosystem of libraries such as NumPy, Pandas, Flask, and TensorFlow
- Interpreted, so code runs line by line without a separate compilation step
- Cross-platform, running on Windows, macOS, and Linux

```python
# A simple Python program
print("Hello, World!")
```

Output:
```
Hello, World!
```

## 2. Variables and Data Types

A variable is a name that refers to a value stored in memory. Python is dynamically typed, meaning the data type is inferred automatically rather than declared explicitly.

### Declaring Variables

```python
name = "Alex"
age = 22
height = 5.9
is_student = True
```

### Common Data Types

- int: whole numbers, e.g. 10
- float: decimal numbers, e.g. 10.5
- str: text, e.g. "Hello"
- bool: boolean values, True or False
- list: ordered, mutable collection, e.g. [1, 2, 3]
- tuple: ordered, immutable collection, e.g. (1, 2, 3)
- dict: key-value pairs, e.g. {"key": "value"}
- set: unordered collection of unique items, e.g. {1, 2, 3}

### Example

```python
name = "Alex"
age = 22
height = 5.9
is_student = True
skills = ["Python", "Flask", "MySQL"]
info = {"course": "AI", "year": "final"}

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(skills))      # <class 'list'>
print(type(info))        # <class 'dict'>
```

## 3. Type Conversion

Type conversion is changing a value from one data type to another. There are two kinds:

- Implicit conversion: Python performs this automatically, for example converting an int to a float during an operation
- Explicit conversion: performed manually using functions such as int(), float(), str(), and bool()

### Implicit Conversion Example

```python
a = 5        # int
b = 2.5      # float
c = a + b    # Python automatically converts 'a' to float

print(c)         # 7.5
print(type(c))   # <class 'float'>
```

### Explicit Conversion Example

```python
# String to Integer
num_str = "100"
num_int = int(num_str)
print(num_int, type(num_int))   # 100 <class 'int'>

# Integer to Float
x = 10
y = float(x)
print(y, type(y))   # 10.0 <class 'float'>

# Integer to String
age = 22
age_str = str(age)
print(age_str, type(age_str))   # "22" <class 'str'>

# String to Float
price = float("99.99")
print(price, type(price))   # 99.99 <class 'float'>
```

Note: int("abc") raises a ValueError, since "abc" is not a valid number.

## 4. Input and Output

### Output: print()

Used to display output on the screen.

```python
print("Hello there!")
print("Age:", 22)
print("Sum =", 5 + 3)

# Formatted output using f-strings
name = "Alex"
age = 22
print(f"My name is {name} and I am {age} years old.")
```

Output:
```
Hello there!
Age: 22
Sum = 8
My name is Alex and I am 22 years old.
```

### Input: input()

Used to take input from the user. The input() function always returns a string, so the value must be converted if a number is needed.

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello {name}, you are {age} years old.")
```

### Input with Type Conversion

```python
age = int(input("Enter your age: "))
next_year = age + 1
print(f"Next year, you'll be {next_year} years old.")
```
