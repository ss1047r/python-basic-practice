# Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).

marks = float(input("Enter the marks: "))
if marks < 0 or marks > 100:
    print("Enter a valid number.")
else:
    if marks >= 90:
        print("A Grade")
    elif marks >= 80:
        print("B Grade")
    elif marks >= 70:
        print("C Grade")
    elif marks >= 60:
        print("D Grade")
    else:
        print("F Grade")