"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    thickness = 5
    mass_per_one = 25

    def __init__(self, width, lenght):
        self._width = width
        self._lenght = lenght

    def calculate(self):
        mass_asphalt = self._width * self._lenght * Road.thickness * Road.mass_per_one
        print(mass_asphalt / 1000, "tons")


boulevard_periferique = Road(20, 5000)
boulevard_periferique.calculate()
