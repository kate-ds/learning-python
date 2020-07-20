"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv
file_name, hours_worked, rate, bonus = argv


try:
    salary = float(hours_worked) * float(rate) + float(bonus)
    if float(hours_worked) >= 0 and float(rate) >= 0 and float(bonus) >= 0:
        print(f"Hours worked: {hours_worked} hours")
        print(f"Rate: {rate} rub/hour")
        print(f"Bonus: {bonus} rub")
        print(f"Your salary: {salary} rub")
    else:
        print("Incorrect values")
except ValueError:
    print("Incorrect values!")


