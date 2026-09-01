
# PYTHON DATA TYPES 


# 1. Integer
age = 52
print("Integer:", age)
print("Type:", type(age))

o/p  Integer: 52
     Type: <class 'int'>

# 2. Float
height = 5.8
print("\nFloat:", height)
print("Type:", type(height))

o/p  Float: 5.8
     Type: <class 'float'>


# 3. String
name = "Max"
print("\nString:", name)
print("Type:", type(name))

o/p  String: Max
     Type: <class 'str'>

# 4. Boolean
is_student = True
print("\nBoolean:", is_student)
print("Type:", type(is_student))

o/p  Boolean: True
     Type: <class 'bool'>

# 5. List
skills = ["Python", "AI", "Git"]
print("\nList:", skills)
print("Type:", type(skills))

o/p  List: ['Python', 'AI', 'Git']
     Type: <class 'list'>

# 6. Tuple
coordinates = (10, 20)
print("\nTuple:", coordinates)
print("Type:", type(coordinates))

o/p   Tuple: (10, 20)
      Type: <class 'tuple'>

# 7. Set
numbers = {1, 2, 3, 4}
print("\nSet:", numbers)
print("Type:", type(numbers))

o/p  Set: {1, 2, 3, 4}
     Type: <class 'set'>

# 8. Dictionary
student = {
    "name": "Max",
    "age": 30,
    "course": "CSE"
}
print("\nDictionary:", student)
print("Type:", type(student))


Dictionary: {'name': 'Max', 'age': 30, 'course': 'CSE'}
Type: <class 'dict'>



# TYPE CONVERSIONS


# 1. String to Integer
value1 = "100"
value1 = int(value1)
print("\nString to Integer:", value1)
print("Type:", type(value1))

o/p   String to Integer: 100
      Type: <class 'int'>


# 2. Integer to String
value2 = 200
value2 = str(value2)
print("\nInteger to String:", value2)
print("Type:", type(value2))

o/p    Integer to String: 200
       Type: <class 'str'>


# 3. Integer to Float
value3 = 50
value3 = float(value3)
print("\nInteger to Float:", value3)
print("Type:", type(value3))

o/p  Integer to Float: 50.0
     Type: <class 'float'>

# 4. Float to Integer
value4 = 25.75
value4 = int(value4)
print("\nFloat to Integer:", value4)
print("Type:", type(value4))

o/p   Float to Integer: 25
      Type: <class 'int'>

# 5. String to Float
value5 = "99.99"
value5 = float(value5)
print("\nString to Float:", value5)
print("Type:", type(value5))

o/p   String to Float: 99.99
      Type: <class 'float'>

# 6. Integer to Boolean
value6 = 1
value6 = bool(value6)
print("\nInteger to Boolean:", value6)
print("Type:", type(value6))

o/p   Integer to Boolean: True
      Type: <class 'bool'>

# 7. Boolean to Integer
value7 = True
value7 = int(value7)
print("\nBoolean to Integer:", value7)
print("Type:", type(value7))

o/p   Boolean to Integer: 1
      Type: <class 'int'>

# 8. String to List
value8 = "Python"
value8 = list(value8)
print("\nString to List:", value8)
print("Type:", type(value8))

o/p   String to List: ['P', 'y', 't', 'h', 'o', 'n']
      Type: <class 'list'>

# 9. List to Tuple
value9 = [1, 2, 3]
value9 = tuple(value9)
print("\nList to Tuple:", value9)
print("Type:", type(value9))

o/p   List to Tuple: (1, 2, 3)
      Type: <class 'tuple'>




