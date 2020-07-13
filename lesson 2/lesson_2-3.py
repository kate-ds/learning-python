while True:
    month = int(input("Enter the number (0: 12): "))
    year = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
    if month in year[0]:
        print("Winter")
    elif month in year[1]:
        print("Spring")
    elif month in year[2]:
        print("Summer")
    elif month in year[3]:
        print("autumn")
    else:
        print("Enter the correct number from 1 to 12")
    quit = input("Do you want to continue? (y/n):")
    if str(quit) == "y":
        continue
    else:
        print("Have a nice day!")
        break