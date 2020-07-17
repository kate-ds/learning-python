def sum_list(*args):
    res = 0
    for i in args[0]:
        try:
            i = float(i)
            res = res + i
        except ValueError:
            if i == "n":
                return res
            continue
    return res


res = 0
while True:
    list_num = input("Enter the line of numbers: ").split()
    res += sum_list(list_num)
    if "n" in list_num:
        break
    print("sum=", res)
print("sum=", res)
