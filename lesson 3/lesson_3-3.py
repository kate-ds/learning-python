def my_func (num1, num2, num3):
    return num1 + num2 + num3 - min(num1, num2, num3)

while True:
    try:
        num1 = float(input("num1 = "))
        num2 = float(input("num2 = "))
        num3 = float(input("num3 = "))
        print(my_func(num1, num2, num3))
    except ValueError:
        print("Incorrect value!")
    res = input("Press 'y' to continue.")
    if res != "y":
        break