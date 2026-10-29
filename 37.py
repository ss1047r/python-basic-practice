# Write a program to reverse a number n.

user_input = input("Enter the number: ")

reversed_list = []

sign = None
for i in user_input:
    if user_input[0] == "-":
        sign = "-"

    if "0" <= i <= "9":            
        reversed_list.insert(0, i)

if sign is not None:
    print(sign, end="")

for digit in reversed_list:
    print(digit, end="")