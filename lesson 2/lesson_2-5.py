# if list of numbers is input:
# inp_list = input("Write a set of numbers: ").split()
# new_list = [int(number) for number in inp_list]
# ----------------------------------------------------------------------
new_list = [3, 6, 7, 2, 7, 3, 6]
while True:
    print(sorted(new_list, reverse=True))
    new_num = input("Enter new number: ")
    if not new_num.isdecimal():
        print ("Enter the correct number.")
    else:
        new_num = int(new_num)
        new_list.append(new_num)
        print(sorted(new_list, reverse=True))
    res = input("repeat? y/n")
    if res == "n":
        print("Have a nice day!")
        break
