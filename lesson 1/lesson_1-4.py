while True:
    a = input("Enter a positive integer number:")
    if not a.isdecimal():
        print("It's not a number (or negative number)")
    else:
        a = int(a)
        max_num = 0
        while a > 0:
            i = a % 10
            a = a // 10
            if i > max_num:
                max_num = i
        print("The maximum digit in the number: ", max_num)
        quit = input("Do you want to continue? (y/n):")
        if str(quit) == "y":
            continue
        else:
            print("Have a nice day!")
            break

