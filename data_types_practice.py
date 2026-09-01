# ==========================================
# PYTHON DATA TYPES AND TYPE CONVERSIONS
# ==========================================

print("===== PYTHON DATA TYPES =====")

# 1. Integer
age = 52
print("Integer:", age)
print("Type:", type(age))

# 2. Float
height = 5.8
print("\nFloat:", height)
print("Type:", type(height))

# 3. String
name = "Max"
print("\nString:", name)
print("Type:", type(name))

# 4. Boolean
is_student = True
print("\nBoolean:", is_student)
print("Type:", type(is_student))

# 5. List
skills = ["Python", "AI", "Git"]
print("\nList:", skills)
print("Type:", type(skills))

# 6. Tuple
coordinates = (10, 20)
print("\nTuple:", coordinates)
print("Type:", type(coordinates))

# 7. Set
numbers = {1, 2, 3, 4}
print("\nSet:", numbers)
print("Type:", type(numbers))

# 8. Dictionary
student = {
    "name": "Teja",
    "age": 22,
    "course": "CSE"
}
print("\nDictionary:", student)
print("Type:", type(student))


# ==========================================
# TYPE CONVERSIONS
# ==========================================

print("\n===== TYPE CONVERSIONS =====")

# 1. String to Integer
value1 = "100"
value1 = int(value1)
print("\nString to Integer:", value1)
print("Type:", type(value1))

# 2. Integer to String
value2 = 200
value2 = str(value2)
print("\nInteger to String:", value2)
print("Type:", type(value2))

# 3. Integer to Float
value3 = 50
value3 = float(value3)
print("\nInteger to Float:", value3)
print("Type:", type(value3))

# 4. Float to Integer
value4 = 25.75
value4 = int(value4)
print("\nFloat to Integer:", value4)
print("Type:", type(value4))

# 5. String to Float
value5 = "99.99"
value5 = float(value5)
print("\nString to Float:", value5)
print("Type:", type(value5))

# 6. Integer to Boolean
value6 = 1
value6 = bool(value6)
print("\nInteger to Boolean:", value6)
print("Type:", type(value6))

# 7. Boolean to Integer
value7 = True
value7 = int(value7)
print("\nBoolean to Integer:", value7)
print("Type:", type(value7))

# 8. String to List
value8 = "Python"
value8 = list(value8)
print("\nString to List:", value8)
print("Type:", type(value8))

# 9. List to Tuple
value9 = [1, 2, 3]
value9 = tuple(value9)
print("\nList to Tuple:", value9)
print("Type:", type(value9))

# 10. Tuple to List
value10 = (4, 5, 6)
value10 = list(value10)
print("\nTuple to List:", value10)
print("Type:", type(value10))


print("\n===== PRACTICE COMPLETED =====")