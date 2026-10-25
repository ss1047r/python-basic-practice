# Write a program to swap two numbers without using a third variable.

num1 = 5
num2 = 10

print(f"Before swap num1: {num1} and num2: {num2}")

num1 = num2 + num1
num2 = num1 - num2
num1 = num1 - num2

print(f"After swap num1: {num1} and num2: {num2}")
