# Write a program to count the number of digits in a number n

user_input = input("Enter the number: ")

count = 0
for i in user_input:
    if "0" <= i <= "9":
        count += 1

print(count)