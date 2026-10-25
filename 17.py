# Write a program to read a character and check whether it is an alphabet, digit or special symbol.

user_input = input("Enter the character: ")
ch = ord(user_input)

if ( 65 <= ch <= 90) or (97 <= ch <= 122):
    print(f"{user_input} is a alphabet")
elif (48 <= ch <= 57):
    print(f"{user_input} is a digit")
else:
    print(f"{user_input} is a special character")