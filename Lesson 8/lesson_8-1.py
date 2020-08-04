"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert_to_number(cls, date):
        try:
            res = int("".join([e for e in date.split("-")]))
        except ValueError:
            print("Date should contain only numbers and dashes")
            return None
        print(res, type(res))
        return cls(date)

    @staticmethod
    def validate(date):
        try:
            date = [int(e) for e in date.split("-")]
            if 32 > date[0] > 0 and 13 > date[1] > 0 and 2100 > date[2] > 0:
                return True, date
            else:
                return False
        except ValueError:
            print("The date is incorrect!")
            return False


my_date1 = "15-05-1990"
Date.convert_to_number(my_date1)
print("validate:", Date.validate(my_date1))
print()

my_date2 = "45-05-3500"
Date.convert_to_number(my_date2)
print("validate:", Date.validate(my_date2))
