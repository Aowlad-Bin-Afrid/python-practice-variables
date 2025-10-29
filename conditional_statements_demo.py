# Conditional Statements Example
# Created by Afrid
# Date: 2025-10-29
# Description: Examples of Python Conditional Statements with Arithmetic Operators


# ------------------------------------------------------------
# Question 1:
# Take user's age as input and print:
# "You are an adult." if age >= 18
# "You are a teenager." if 13 <= age < 18
# Otherwise print "You are a child."
# ------------------------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


# ------------------------------------------------------------
# Question 2:
# Take two numbers from the user.
# If their sum is 100 or more → print "Sum is greater than 100"
# Otherwise → print "Sum is within limit"
# ------------------------------------------------------------

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
sum_result = num_1 + num_2

if sum_result >= 100:
    print("Sum is greater than 100")
else:
    print("Sum is within limit")


# ------------------------------------------------------------
# Question 3:
# Take a number from the user.
# Check if it is even or odd using the modulo (%) operator.
# ------------------------------------------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ------------------------------------------------------------
# Question 4:
# Take two numbers and print which one is bigger.
# If both are equal → print "Both numbers are equal"
# ------------------------------------------------------------

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if num_1 > num_2:
    print(f"Number one is bigger: {num_1}")
elif num_2 > num_1:
    print(f"Number two is bigger: {num_2}")
else:
    print("Both numbers are equal")


# ------------------------------------------------------------
# Question 5:
# Take marks (0–100) as input and show grade using conditional statements:
# 80 or above → Grade A
# 60–79 → Grade B
# 40–59 → Grade C
# Below 40 → Fail
# ------------------------------------------------------------

num1 = int(input("Enter your marks (0-100): "))
marks = not num1 <= 100

if marks:
    print("Please enter a valid mark between 0–100.")
elif num1 >= 80:
    print("Grade: A")
elif num1 >= 60:
    print("Grade: B")
elif num1 >= 40:
    print("Grade: C")
else:
    print("Sorry, you failed.")


# ------------------------------------------------------------
#  Question 6:
# Take a number and check:
# Positive → "Positive number"
# Negative → "Negative number"
# Zero → "Zero"
# ------------------------------------------------------------

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# ------------------------------------------------------------
#  Question 7 (Bonus):
# Take three numbers as input and print the biggest one.
# If all three are equal → print "All numbers are equal"
# ------------------------------------------------------------

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2 and num1 > num3:
    print(f"The biggest number is {num1} (num1)")
elif num2 > num1 and num2 > num3:
    print(f"The biggest number is {num2} (num2)")
elif num1 == num2 == num3:
    print("All numbers are equal")
else:
    print(f"The biggest number is {num3} (num3)")
