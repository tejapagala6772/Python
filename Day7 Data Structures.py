
# DATA STRUCTURES IN PYTHON



# 1. List
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

# o/p
# List: [10, 20, 30, 40, 50]


# 2. Accessing List Elements
numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Third element:", numbers[2])

# o/p
# First element: 10
# Third element: 30


# 3. Adding Element to List
numbers = [10, 20, 30]

numbers.append(40)

print("List:", numbers)

# o/p
# List: [10, 20, 30, 40]


# 4. Removing Element from List
numbers = [10, 20, 30, 40]

numbers.remove(30)

print("List:", numbers)

# o/p
# List: [10, 20, 40]


# 5. Updating List Element
numbers = [10, 20, 30]

numbers[1] = 25

print("List:", numbers)

# o/p
# List: [10, 25, 30]


# 6. List Length
numbers = [10, 20, 30, 40]

print("Length:", len(numbers))

# o/p
# Length: 4


# 7. Tuple
numbers = (10, 20, 30, 40)

print("Tuple:", numbers)

# o/p
# Tuple: (10, 20, 30, 40)


# 8. Accessing Tuple Elements
numbers = (10, 20, 30, 40)

print("First element:", numbers[0])
print("Second element:", numbers[1])

# o/p
# First element: 10
# Second element: 20


# 9. Tuple Length
numbers = (10, 20, 30, 40, 50)

print("Length:", len(numbers))

# o/p
# Length: 5


# 10. Set
numbers = {10, 20, 30, 40}

print("Set:", numbers)

# o/p
# Set: {10, 20, 30, 40}


# 11. Adding Element to Set
numbers = {10, 20, 30}

numbers.add(40)

print("Set:", numbers)

# o/p
# Set: {10, 20, 30, 40}


# 12. Removing Element from Set
numbers = {10, 20, 30, 40}

numbers.remove(20)

print("Set:", numbers)

# o/p
# Set: {10, 30, 40}


# 13. Set Removes Duplicates
numbers = {10, 20, 20, 30, 30}

print("Set:", numbers)

# o/p
# Set: {10, 20, 30}


# 14. Dictionary
student = {
    "name": "Alex",
    "age": 20,
    "course": "Python"
}

print("Dictionary:", student)

# o/p
# Dictionary: {'name': 'Alex', 'age': 20, 'course': 'Python'}


# 15. Accessing Dictionary Values
student = {
    "name": "Alex",
    "age": 20
}

print("Name:", student["name"])
print("Age:", student["age"])

# o/p
# Name: Alex
# Age: 20


# 16. Adding Dictionary Item
student = {
    "name": "Alex",
    "age": 20
}

student["course"] = "Python"

print("Dictionary:", student)

# o/p
# Dictionary: {'name': 'Alex', 'age': 20, 'course': 'Python'}


# 17. Updating Dictionary Value
student = {
    "name": "Alex",
    "age": 20
}

student["age"] = 21

print("Dictionary:", student)

# o/p
# Dictionary: {'name': 'Alex', 'age': 21}


# 18. Removing Dictionary Item
student = {
    "name": "Alex",
    "age": 20,
    "course": "Python"
}

del student["age"]

print("Dictionary:", student)

# o/p
# Dictionary: {'name': 'Alex', 'course': 'Python'}


# 19. Dictionary Keys
student = {
    "name": "Alex",
    "age": 20,
    "course": "Python"
}

print("Keys:", student.keys())

# o/p
# Keys: dict_keys(['name', 'age', 'course'])


# 20. Dictionary Values
student = {
    "name": "Alex",
    "age": 20,
    "course": "Python"
}

print("Values:", student.values())

# o/p
# Values: dict_values(['Alex', 20, 'Python'])



#  List of Dictionaries
students = [
    {"name": "Alex", "marks": 85},
    {"name": "Sam", "marks": 92},
    {"name": "John", "marks": 78}
]

for student in students:
    print(student["name"], ":", student["marks"])

# o/p
# Alex : 85
# Sam : 92
# John : 78


#  Dictionary with List
student = {
    "name": "Alex",
    "subjects": ["Python", "SQL", "AI"],
    "marks": [85, 90, 88]
}

print("Name:", student["name"])
print("Subjects:", student["subjects"])
print("Marks:", student["marks"])

# o/p
# Name: Alex
# Subjects: ['Python', 'SQL', 'AI']
# Marks: [85, 90, 88]


#  Set Operations
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# o/p
# Union: {10, 20, 30, 40, 50, 60}
# Intersection: {30, 40}
# Difference: {10, 20}


# Nested Dictionary
students = {
    "student1": {
        "name": "Alex",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Sam",
        "age": 21,
        "marks": 92
    }
}

print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Marks:", students["student2"]["marks"])

# o/p
# Student 1 Name: Alex
# Student 2 Marks: 92