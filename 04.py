# Write a program to read the radius of a circle and print its area and circumference.

radius = float(input("Enter the radius of the circle: "))

pi = 3.14

area = pi * (radius * radius)
print(f"Area of circle: {area}")

circumference = round(pi * (2 * radius), 2)
print(f"Circumference of circle: {circumference}")