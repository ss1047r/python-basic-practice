# Write a program to read the age of a person and check whether they are eligible to vote.

user_input = int(input("Enter your age: "))

if(user_input < 0):
    print("Age can't be negative")
else:
    if(user_input >= 18):
        print("Eligible for vote")
    else:
        print("Not eligible for vote")