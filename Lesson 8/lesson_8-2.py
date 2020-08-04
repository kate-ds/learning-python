"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivision(Exception):
    def __init__(self, txt="Zero division error!"):
        self.txt = txt
        super().__init__(self.txt)


num1 = input("1st number ")
num2 = input("2nd number ")

try:
    if int(num2) == 0:
        raise MyZeroDivision()
    division = int(num1) / int(num2)
except (ValueError, MyZeroDivision) as my_error:
    print(my_error)

else:
    print(division)
