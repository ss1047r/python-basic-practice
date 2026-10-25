# Write a program to swap two numbers using a third variable.


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print(f"Before swap, num1: {num1}, num2: {num2}")

temp = num1
num1 = num2
num2 = temp

print(f"After swap num1: {num1}, num2: {num2}")