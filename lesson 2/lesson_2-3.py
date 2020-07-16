while True:
    month = input("Enter the number [1: 12]: ")
    if not month.isdecimal() or int(month) > 12 or int(month) < 1:
        print("Enter the correct number.")
    else:
        print("ok")
        month = int(month)
        method = input("Enter the method: 1 - list, 2 - dictionary, 3 - dictionary and list: ")
        if not method.isdecimal():
            print("Enter the correct number.")
        else:
            method = int(method)
# -------------------------------------------------------1-list--------------------------------------------------------
            if method == 1:
                year = [[1, 2, 12],
                        [3, 4, 5],
                        [6, 7, 8],
                        [9, 10, 11]]
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
# ------------------------------------------------------2-dictionary---------------------------------------------------
            elif method == 2:
                year = {1: "winter", 2: "winter", 12: "winter",
                        3: "spring", 4: "spring", 5: "spring",
                        6: "summer", 7: "summer", 8: "summer",
                        9: "autumn", 10: "autumn", 11: "autumn"}
                print("Season: ", year[month])
# ------------------------------------------------------3-dict+list----------------------------------------------------
            elif method == 3:
                year = {"winter": [1, 2, 12],
                        "spring": [3, 4, 5],
                        "summer": [6, 7, 8],
                        "autumn": [9, 10, 11]}
                for k in year:
                    if month in year[k]:
                        print(k)
                        break
            else:
                print("Sorry, I didn't write more methods.")
    # -------------------------------------------------------------------------------------------------------------------

    quit = input("Do you want to continue? (y/n):")
    if str(quit) == "y":
        continue
    else:
        print("Have a nice day!")
        break