def my_func(x, y):
    y = y * (-1)
    res = 1
    for i in range(0, y):
        res = res * 1 / x
    return res


while True:
    try:
        x = int(input("Enter positive X\nX = "))
        y = int(input("Enter negative Y\nY = "))
        if x > 0 > y:
            print(my_func(x, y))
        else:
            print("Incorrect numbers!")
    except ValueError:
        print("Incorrect numbers!")
    res = input("Press 'y' to continue.")
    if res != "y":
        break
