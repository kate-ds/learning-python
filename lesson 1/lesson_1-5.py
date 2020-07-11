while True:
    try:
        proceeds = float(input("Enter the amount of proceeds: "))
        costs = float(input("Enter the amount of costs: "))
        profit = proceeds - costs
        if not profit > 0:
            print("The company doesn't make a profit.")
        else:
            print("The company makes a profit.")
            profitability = profit / proceeds
            print(f"The profitability is {profitability:2.2%}.")
            num_pers = input("Enter a number of person: ")
            if not num_pers.isdecimal() or num_pers == "0":
                print("Enter the correct number:")
            else:
                num_pers = int(num_pers)
                profit_pers = profit / num_pers
                print(f"The profit per person: {profit_pers:.2f} ")
    except Exception:
        print("Enter the correct amount.")


    quit = input("Do you want to continue? (y/n):")
    if str(quit) == "y":
        continue
    else:
        print("Have a nice day!")
        break
