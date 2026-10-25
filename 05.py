# Write a program to read the length and breadth of a rectangle and print its area and perimeter.


length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

area = length * breadth
print(f"Area of rectangle: {area}")

perimeter = 2 * (length + breadth)
print(f"Perimeter of rectangle: {perimeter}")