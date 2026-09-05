
# JUMPING STATEMENTS


#Pass
#Continue 
#Break




# 1. PASS


print("1. Pass Example")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

# o/p:
# 1
# 2
# 3
# 4
# 5



# 2. PASS

print("\n2. Pass Example")

number = 10

if number > 5:
    pass

print("Number is:", number)

# o/p:
# Number is: 10



# 3. PASS

print("\n3. Pass Example")

for i in range(1, 4):
    if i == 2:
        pass
    print("Value:", i)

# o/p:
# Value: 1
# Value: 2
# Value: 3



# 4. PASS


print("\n4. Pass Example")

for i in range(1, 6):
    if i == 4:
        pass
    else:
        print("Number:", i)

# o/p:
# Number: 1
# Number: 2
# Number: 3
# Number: 5



# 5. CONTINUE


print("\n5. Continue Example")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# o/p:
# 1
# 2
# 4
# 5



# 6. CONTINUE


print("\n6. Continue Example")

for i in range(1, 6):
    if i == 2:
        continue
    print("Number:", i)

# o/p:
# Number: 1
# Number: 3
# Number: 4
# Number: 5



# 7. CONTINUE


print("\n7. Continue Example")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# o/p:
# 1
# 3
# 5
# 7
# 9



# 8. CONTINUE


print("\n8. Continue Example")

for i in range(1, 6):
    if i == 4:
        continue
    print("Hello", i)

# o/p:
# Hello 1
# Hello 2
# Hello 3
# Hello 5



# 9. CONTINUE


print("\n9. Continue Example")

for i in range(1, 6):
    if i < 3:
        continue
    print(i)

# o/p:
# 3
# 4
# 5



# 10. BREAK


print("\n10. Break Example")

for i in range(1, 6):
    if i == 3:
        break
    print(i)

# o/p:
# 1
# 2



# 11. BREAK


print("\n11. Break Example")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# o/p:
# 1
# 2
# 3
# 4



# 12. BREAK


print("\n12. Break Example")

for i in range(1, 6):
    print(i)
    if i == 4:
        break

# o/p:
# 1
# 2
# 3
# 4



# 13. BREAK


print("\n13. Break Example")

for i in range(1, 11):
    if i > 5:
        break
    print(i)

# o/p:
# 1
# 2
# 3
# 4
# 5



# 14. BREAK


print("\n14. Break Example")

number = 1

while number <= 5:
    if number == 4:
        break
    print(number)
    number = number + 1

# o/p:
# 1
# 2
# 3



# 15. BREAK


print("\n15. Break Example")

for i in range(1, 6):
    if i == 2:
        break
    print("Value:", i)

# o/p:
# Value: 1


# 16. COMBINATION OF CONTINUE AND BREAK


print("\n16. Continue and Break Example")

for i in range(1, 11):

    if i == 3:
        continue

    if i == 7:
        break

    print(i)

# o/p:
# 1
# 2
# 4
# 5
# 6