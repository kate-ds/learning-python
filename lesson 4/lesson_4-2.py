"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""
my_list = [68, 2, 5, 1, 7, 23, 45, 23, 43, 54, 65, 24, 78, 190, 2, 153]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(my_list)

print(new_list)


