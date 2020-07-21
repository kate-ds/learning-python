"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале
нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""


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
    list_num = input("Enter the line of numbers (Enter 'n' to finish): ").split()
    res += sum_list(list_num)
    if "n" in list_num:
        break
    print("sum=", res)
print("sum=", res)
