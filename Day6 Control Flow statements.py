
#             PYTHON CONTROL FLOW PRACTICE
#      Conditional Statements → Loops → Jumping Statements


#                 1. CONDITIONAL STATEMENTS



# 1. if statement
number = 10

if number > 5:
    print("Number is greater than 5")

# o/p
# Number is greater than 5


# 2. if-else statement
number = 3

if number > 5:
    print("Number is greater than 5")
else:
    print("Number is not greater than 5")

# o/p
# Number is not greater than 5


# 3. if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# o/p
# Grade B


# 4. Nested if
number = 20

if number > 10:
    if number < 30:
        print("Number is between 10 and 30")

# o/p
# Number is between 10 and 30


# 5. Checking even or odd
number = 8

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# o/p
# Even number


# 6. Checking positive, negative or zero
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# o/p
# Negative


# 7. Checking voting eligibility
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# o/p
# Eligible to vote


# 8. Finding greater number
a = 15
b = 10

if a > b:
    print("a is greater")
else:
    print("b is greater")

# o/p
# a is greater



#                       2. LOOPS



# 9. for loop
for i in range(1, 6):
    print(i)

# o/p
# 1
# 2
# 3
# 4
# 5


# 10. for loop with string
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


# 11. for loop with list
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)

# o/p
# 10
# 20
# 30
# 40


# 12. while loop
number = 1

while number <= 5:
    print(number)
    number = number + 1

# o/p
# 1
# 2
# 3
# 4
# 5


# 13. while loop with countdown
number = 5

while number >= 1:
    print(number)
    number = number - 1

# o/p
# 5
# 4
# 3
# 2
# 1


# 14. Multiplication table using for loop
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# o/p
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50


# 15. Sum of numbers using for loop
total = 0

for i in range(1, 6):
    total = total + i

print("Sum:", total)

# o/p
# Sum: 15


# 16. Nested for loop
for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)

# o/p
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3



#                 3. JUMPING STATEMENTS

# 17. pass statement
for i in range(1, 4):
    if i == 2:
        pass
    print(i)

# o/p
# 1
# 2
# 3


# 18. continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# o/p
# 1
# 2
# 4
# 5


# 19. break statement
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# o/p
# 1
# 2
# 3


# 20. pass with if statement
number = 10

if number > 5:
    pass

print("Program continues")

# o/p
# Program continues


# 21. continue with even numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

# o/p
# 1
# 3
# 5


# 22. break when number is found
for i in range(1, 10):
    if i == 6:
        break
    print(i)

# o/p
# 1
# 2
# 3
# 4
# 5


# 23. continue in while loop
number = 0

while number < 5:
    number = number + 1

    if number == 3:
        continue

    print(number)

# o/p
# 1
# 2
# 4
# 5


# 24. break in while loop
number = 1

while number <= 5:

    if number == 4:
        break

    print(number)
    number = number + 1

# o/p
# 1
# 2
# 3