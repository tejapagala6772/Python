# Loops Statements

# For Loop  
# #While Loop  
# #Nested Loop



# 1. For Loop
# Example
for i in range(5):
    print(i)

# o/p
# 0
# 1
# 2
# 3
# 4


# 2. For Loop
# Example
for i in range(1, 6):
    print(i)

# o/p
# 1
# 2
# 3
# 4
# 5


# 3. For Loop
# Example
for i in range(1, 6):
    print(i * 2)

# o/p
# 2
# 4
# 6
# 8
# 10


# 4. For Loop
# Example
fruits = ["Apple", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)

# o/p
# Apple
# Mango
# Orange


# 5. For Loop
# Example
word = "Python"

for letter in word:
    print(letter)

# o/p
# P
# y
# t
# h
# o
# n


# 6. For Loop
# Example
for i in range(1, 6):
    print("Hello")

# o/p
# Hello
# Hello
# Hello
# Hello
# Hello


# 7. While Loop
# Example
i = 1

while i <= 5:
    print(i)
    i = i + 1

# o/p
# 1
# 2
# 3
# 4
# 5


# 8. While Loop
# Example
i = 5

while i >= 1:
    print(i)
    i = i - 1

# o/p
# 5
# 4
# 3
# 2
# 1


# 9. While Loop
# Example
i = 2

while i <= 10:
    print(i)
    i = i + 2

# o/p
# 2
# 4
# 6
# 8
# 10


# 10. While Loop
# Example
i = 1

while i <= 5:
    print("Python")
    i = i + 1

# o/p
# Python
# Python
# Python
# Python
# Python


# 11. While Loop
# Example
i = 1
total = 0

while i <= 5:
    total = total + i
    i = i + 1

print(total)

# o/p
# 15


# 12. Nested Loop
# Example
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# o/p
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3


# 13. Nested Loop
# Example
for i in range(1, 4):
    for j in range(1, 3):
        print("*")

# o/p
# *
# *
# *
# *
# *
# *


# 14. Nested Loop
# Example
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

# o/p
# 1 2 3
# 1 2 3
# 1 2 3


# 15. Nested Loop
# Example
for i in range(1, 4):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# o/p
# *
# * *
# * * *


# 16. Nested Loop
# Example
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# o/p
# 1 2 3
# 2 4 6
# 3 6 9

# 17. Nested Loop
# Example
for i in range(3):
    for j in range(2):
        print(i, j)

# o/p
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1                     