"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке
их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

"""

my_list = [1, 0, 2, 3, 4, 5, 21, 54, 6, 3, 4, 13, 0, 12, 13, 1, 54]
new_list = [el for el in my_list if  my_list.count(el) == 1]
print(new_list)
