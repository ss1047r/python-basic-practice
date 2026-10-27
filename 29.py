# Write a program to display the multiplication table of a number n.

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")