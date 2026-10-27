# Write a program to find the sum of all even numbers from 1 to n.

user_input = int(input("Enter the number: "))

total = 0
if user_input < 0:
    print("Negative numbers are not allowed")
else:
    for i in range(1, user_input):
        if i % 2 == 0:
            total += i

print(f"Total: {total}")