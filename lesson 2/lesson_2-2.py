my_list = input("New list: ")
my_list = my_list.split()
for i in range(0, len(my_list) - 1):
    if i % 2 == 0:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
print(my_list)

# ---------------------------------------------------------------

for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
    print(i, my_list[i])
print(my_list)