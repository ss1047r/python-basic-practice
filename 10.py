# Write a program to read seconds and convert them into hours, minutes and seconds.

user_input = int(input("Enter the seconds: "))

hour = user_input // 3600
remaining_seconds = user_input % 3600

minute = remaining_seconds // 60
second = remaining_seconds % 60

print(f"Time: {hour}:{minute}:{second}")