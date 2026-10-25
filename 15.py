# Write a program to read a year and check whether it is a leap year or not.


user_input = int(input("Enter year: "))

if (user_input % 400 == 0) or (user_input % 4 == 0 and user_input % 100 != 0):
    print("It is a leap year")
else:
    print("It is not a leap year")

