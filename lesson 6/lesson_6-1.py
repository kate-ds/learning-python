"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
 порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep
import os


class TrafficLight:
    def __init__(self):
        self.__color = [{"color": "\x1b[6;37;41m  red   \x1b[0m", "duration": 7},
                        {"color": "\x1b[6;37;43m yellow \x1b[0m", "duration": 2},
                        {"color": "\x1b[6;37;42m green  \x1b[0m", "duration": 7}]

    def running(self):
        for e in self.__color:
            print(e["color"])
            sleep(e["duration"])

    def running2(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for e in self.__color:
            print(e["color"])
            sleep(e["duration"])
            os.system('cls' if os.name == 'nt' else 'clear')


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running2()
