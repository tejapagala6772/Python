# CONDITIONAL STATEMENTS IN PYTHON

# Topics:
# if condition
# else
# elif
# nested if


# 1. If Condition

age = 20

if age >= 18:
    print("You are an adult")

# o/p:
# You are an adult


# 2. If Condition with False Condition

age = 15

if age >= 18:
    print("You are an adult")

# o/p:
# Nothing is printed because the condition is false


# 3. Else

number = 10

if number > 0:
    print("Positive number")
else:
    print("Negative number")

# o/p:
# Positive number


# 4. If -> Else

number = -5

if number > 0:
    print("Positive number")
else:
    print("Negative number")

# o/p:
# Negative number


# 5. Elif

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# o/p:
# Grade B


# 6. Multiple Elif

marks = 45

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade D")

# o/p:
# Grade D


# 7. Nested If

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

# o/p:
# Entry allowed


# 8. Nested If -> Else

age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID is required")

# o/p:
# ID is required


# 9. Simple Real-Life Example

temperature = 30

if temperature > 35:
    print("Very hot")
elif temperature > 25:
    print("Warm")
else:
    print("Cool")

# o/p:
# Warm


# 10. Check Even or Odd

number = 8

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# o/p:
# Even number


# 11. Check Voting Eligibility

age = 21

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# o/p:
# Eligible to vote


# 12. Check Login

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# o/p:
# Login successful

# 13. If - Check Discount Eligibility

purchase_amount = 2500

if purchase_amount >= 2000:
    discount = purchase_amount * 0.10
    print("Discount:", discount)

# o/p:
# Discount: 250.0


# 14. If - Check Password Length

password = "python123"

if len(password) >= 8:
    print("Password is strong enough")

# o/p:
# Password is strong enough


# 15. Elif - Calculate Grade

marks = 82

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# o/p:
# Grade: A


# 16. Elif - Select a Traffic Signal Action

signal = "yellow"

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")

# o/p:
# Get ready


# 17. Else - Check Number Range

number = 45

if number >= 1 and number <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is outside the range")

# o/p:
# Number is between 1 and 100


# 18. Else - Check Shopping Minimum Amount

cart_total = 850

if cart_total >= 1000:
    print("Free delivery")
else:
    print("Delivery charges apply")

# o/p:
# Delivery charges apply


# 19. Nested If - Login and Account Status

username = "admin"
password = "admin123"
account_active = True

if username == "admin":
    if password == "admin123":
        if account_active:
            print("Login successful")
        else:
            print("Account is inactive")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")

# o/p:
# Login successful


# 20. Nested If - Check Exam Eligibility

attendance = 85
fees_paid = True

if attendance >= 75:
    if fees_paid:
        print("Student is eligible for the exam")
    else:
        print("Please complete the fee payment")
else:
    print("Attendance is too low")

# o/p:
# Student is eligible for the exam