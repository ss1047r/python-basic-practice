# Write a program to display all natural numbers from 1 to n in reverse order

user_input = int(input("Enter the number: "))

if user_input < 0:
    print("Negative numbers are not included in the natural numbers")
elif user_input == 0:
    print("There are no natural numbers from 1 to 0.")
else:
    for i in range(user_input, 0, -1):
        print(i)
