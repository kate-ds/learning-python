"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(self.title)


class Pen(Stationery):
    def draw(self):
        print(f'\033[94m{self.title}\033[0m')


class Pencil(Stationery):
    def draw(self):
        print(f'\033[1m{self.title}\033[0m')


class Handle(Stationery):
    def draw(self):
        print(f'\x1b[6;30;42m{self.title}\x1b[0m')


unknown = Stationery("This text should be white.")
unknown.draw()
pen = Pen("This text is written with pen")
pen.draw()
pencil = Pencil("This text is written with pencil")
pencil.draw()
handle = Handle("This text is marked with handle")
handle.draw()
