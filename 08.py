# Write a program to read a temperature in Celsius and convert it to Fahrenheit.

temperature = float(input("Enter the temperature: "))

fahrenheit = temperature * (9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")


celsius = (temperature - 32) * (5/9)
print(f"Temperature in Celsius: {celsius}")