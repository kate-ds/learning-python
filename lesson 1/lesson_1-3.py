while True:
    n = input("Enter a number:")
    if not n.isdecimal():
        print("It's not a number (or negative number)")
    else:
        result = int(n) + int(n + n) + int(n + n + n)
        print(result)
    quit = input("Do you want to continue? (y/n):")
    if str(quit) == "y":
        continue
    else:
        print("Have a nice day!")
        break