# Write a program to read three numbers and find the largest among them.

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))

if (num1 > num2) and (num1 > num3):
    print(f"{num1} is the largest")
elif (num2 > num1) and (num2 > num3):
    print(f"{num2} is largest")
else:
    print(f"{num3} is the largest")