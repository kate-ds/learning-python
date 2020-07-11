while True:
    try:
        a = float(input("Result a = "))
        b = float(input("Result b = "))
        if a > 0 and b > 0:
            i = 1
            while a < b:
                a = a + 0.1 * a
                i = i + 1
            print("Day ", i)
        else:
            print("Tne number can't be 0 or negative.")
    except Exception:
        print("Enter the correct number.")
    quit = input("Do you want to continue? (y/n):")
    if str(quit) == "y":
        continue
    else:
        print("Have a nice day!")
        break

