# Write a program to display all multiples of a number m up to n terms

m = int(input("Enter the number whose multiples you want: "))
n = int(input("Enter the number of terms: "))

for i in range(1, n + 1):
    print(m * i)
