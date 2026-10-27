# Write a program to count how many numbers from 1 to n are divisible by 3

n = int(input("Enter the value: "))

if n == 0:
    print("Zero is not allowed")
else:
    for i in range(1,n+1):
        if i % 3 == 0:
            print(i)