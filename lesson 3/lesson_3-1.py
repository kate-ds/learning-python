def my_func(num1, num2):
    return num1 / num2


while True:
    try:
        num1 = float(input("num1: "))
        num2 = float(input("num2: "))
        print(my_func(num1, num2))
    except ValueError:
        print("Incorrect value!")
    except ZeroDivisionError:
        print("Zero division error!")
    res = input("Press 'y' to continue.")
    if res != "y":
        break


