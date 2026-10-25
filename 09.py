#  Write a program to read the marks of 5 subjects and print the total and average.

# subject1 = float(input("Enter the marks of 1st subject: "))
# subject2 = float(input("Enter the marks of 2nd subject: "))
# subject3 = float(input("Enter the marks of 3rd subject: "))
# subject4 = float(input("Enter the marks of 4th subject: "))
# subject5 = float(input("Enter the marks of 5th subject: "))

# total = subject1 + subject2 + subject3 + subject4 + subject5

# average = total/5

# print(f"Total marks: {total}, and Average marks: {average}")

subject_marks = []

user_input = int(input("Enter the number of subject marks you want to enter: "))

total = 0
if user_input < 0:
    print("Entered subject number is negative ")
else:
    for i in range(user_input):
        mark = float(input("Enter the marks: "))
        while(mark < 0):
            print("Negative number is not allowed")
            mark = float(input("Enter the marks: "))
        subject_marks.append(mark)
        total += mark

average = None
if user_input == 0:
    print("Input is 0, no subject is entered.")
else:
    average = round(total/len(subject_marks), 2)
    
print(f"Total marks: {total}, and Average marks: {average}")