name = input("Your name? ")
city = input("Where do you live? ")
age = input("How old are you? ")
print(f"Hello! Your name is {name}, you live in {city}, you are {age} years old.\nLet's calculate a bit:")
while True:
    a = float(input("Enter the 1st number. \na="))
    b = float(input("Enter the 2nd number. \nb="))
    operation = input("Enter an operator (+, -, /, *): ")
    if operation == str("+"):
        print("a + b = ", a + b)
    elif operation == str("-"):
        print("a - b = ", a - b)
    elif operation == str("/"):
        if b == 0:
            print("Zero division.")
            b = float(input("Enter other value of b"))
        print("a / b = ", a / b)
    elif operation == str("*"):
        print("a * b = ", a * b)
    else:
        print("Sorry, it is not working yet")
    reply = input("Do you want to count something else? y/n ")
    if reply == "y":
        continue
    break
