# Write a program to read a character and check whether it is a vowel or a consonant.

vowels = ["a","e","i","o","u"]

user_input = input("Enter the character: ")

if user_input.lower() in vowels:
    print(f"{user_input} is a Vowel")
else:
    print(f"{user_input} is a consonant")