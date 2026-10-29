# Write a program to find the sum of all digits of a number n.

user_input = input("Enter the number: ")

total = 0
for i in user_input:
    if "0" <= i <= "9":
        total += int(i)

print(total)

