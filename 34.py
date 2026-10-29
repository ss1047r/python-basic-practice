# Write a program to display all the digits of a number n (one per line).

user_input = input("Enter the number: ")

for i in user_input:
    if ("0" <= i <= "9"):
        print(i)