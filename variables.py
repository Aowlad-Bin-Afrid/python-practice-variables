# Basic variable examples
# Created by Afrid
# Date: 2025-10-27
# Description: Basic examples of Python variables

# simple variable
name = "Afrid"
print(name)

# multiple variables
x = "age"
y = 18
print(x, y)

# variables with f-string
name = "Afrid"
age = 18
city = "Dhaka"
print(f"Hi, my name is {name}. I'm {age} years old. I live in {city} city.")

# updating variable value
name = "Afrid"
age = 18
print(f"My name is {name}. I'm {age} years old.")
age = age + 1   # update variable
print(f"Next year I will be {age} years old.")

# taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
age += 1   # update with +1
print(f"{name}, next year you will be {age} years old.")
