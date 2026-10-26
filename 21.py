# Write a program to display all the natural numbers from 1 to n. (n is user input)

user_input = int(input("Enter the number: "))

if user_input < 0:
    print("Negative numbers are not included in the natural numbers")
elif user_input == 0:
    print("There are no natural numbers from 1 to 0.")
else:
    for i in range(1, user_input+1):
        print(i)