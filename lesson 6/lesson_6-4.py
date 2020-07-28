"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} speed is {self.speed} km/h")
        if self.is_police:
            print('{blue}POLICE !!!{endcolor}'.format(blue='\033[91m', endcolor='\033[0m'))

    def stop(self):
        print(f"{self.name} stopped")

    def turn(self, direction):
        print(f"{self.name} turn {direction}")

    def show_speed(self):
        print(f"{self.name} speed is {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"You exceeded the speed limit of 60 km/h. Your speed is {self.speed} km/h")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"You exceeded the speed limit of 40 km/h. Your speed is {self.speed} km/h")


class PoliceCar(Car):
    def arrest(self, name):
        print(f"{name} arrested")


renault = TownCar(90, "blue", "Renault 2CV", False)
renault.go()
renault.show_speed()
renault.turn("right")
renault.stop()


pol = Car(70, "white-blue", "ВАЗ", True)
pol.go()
pol.show_speed()


lobzikov = PoliceCar("33", "white-blue", "Камаз", True)
lobzikov.go()
lobzikov.arrest("suzuki")
