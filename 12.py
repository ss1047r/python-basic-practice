# Write a program to read a number and check whether it is positive, negative or zero.


user_input = int(input("Enter the number: "))

if user_input == 0:
    print("Number is 0")
elif user_input > 0:
    print("Number is positive")
else:
    print("Number is negative")