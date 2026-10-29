# Write a program to find the product of all digits of a number n.

user_input = input("Enter the number: ")

product = 1

if ("A" <= user_input <= "Z") or ("a" <= user_input <= "z"):
    print("Can't find the product of character")
else:
    if user_input == "":
        product = None
        print(f"No value found. Product: {product}")
    else:
        for i in user_input:
            if "0" <= i <= "9":
                product *= int(i)

        print(f"Product: {product}")