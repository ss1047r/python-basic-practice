# Write a program to find the product of all natural numbers from 1 to n (factorial of n)

user_input = int(input("Enter the number: "))

factorial = 1
if user_input < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(2, user_input + 1):
        factorial *= i

print(f"Factorial of {user_input}: {factorial}")


# while user_input != 0:
#     factorial *= user_input
#     user_input -= 1