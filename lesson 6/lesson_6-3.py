"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        print({"Name": name,
               "Surname": surname,
               "Position": position,
               "Wage": wage,
               "Bonus": bonus})


class Position(Worker):
    def get_full_name(self):
        print(self.surname + " " + self.name)

    def get_total_income(self):
        # for i in Worker._income:
        # total = Worker.wage + Worker.bonus
        print("Total: ", self._income["wage"] + self._income["bonus"], "руб")


zemlyanikina = Position("Дарья", "Земляникина", "Инженер", 100000, 50000)
lepeshkina = Position("Полина", "Лепешкина", "Экономист", 200000, 30000)
bulkin = Position("Артем", "Булкин", "Булочник", 33500, 21300)


zemlyanikina.get_full_name()
zemlyanikina.get_total_income()
lepeshkina.get_full_name()
lepeshkina.get_total_income()
bulkin.get_full_name()
bulkin.get_total_income()


