"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
при вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим
образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо
выводить только первые n чисел, начиная с 1! и до n!.
"""


def fact(n):
    res = 1
    for e in range(1, n + 1):
        res = e * res
        yield res

for el in fact(5):
    print(el)
