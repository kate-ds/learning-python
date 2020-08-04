"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def calc(self):
        pass


class Coat(Wear):
    def __init__(self, v):
        self.v = v

    @property
    def calc(self):
        return self.v / 6.5 + 0.3


class Suit(Wear):
    def __init__(self, h):
        self.h = h

    @property
    def calc(self):
        return self.h * 2 + 0.3


a = Coat(10)
print(a.calc)

b = Suit(20)
print(b.calc)

print("Общая сумма", a.calc + b.calc)



# -------------------------------------------2 -----------------------------
#
# class Wear:
#     def __init__(self, v, h):
#         self.v = v
#         self.h = h
#
#     def calc_coat(self):
#         return self.v / 6.5 + 0.3
#
#     def calc_suit(self):
#         return self.h * 2 + 0.3
#
#     @property
#     def get_sum(self):
#         return self.v / 6.5 + 0.3 + self.h * 2 + 0.3
#
#
# class Coat(Wear):
#     def __init__(self, v, h):
#         super().__init__(v, h)
#         self.calc_coat = self.v / 6.5 + 0.3
#
#
# class Suit(Wear):
#     def __init__(self, v, h):
#         super().__init__(v, h)
#
#     def calc(self):
#         return self.h * 2 + 0.3
#

# a = Coat(10)
# print(a.calc())
#
# b = Suit(20)
#
# print(b.calc())
