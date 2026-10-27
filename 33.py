# Write a program to display all numbers from 1 to n that are divisible by 3 or 5.

n = int(input("Enter the value: "))

if n < 0:
    print("Negative number are not accepted.")
for i in range(n+1):
    if (i % 3 == 0) or (i % 5 == 0):
        print(i)