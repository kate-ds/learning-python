"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
 порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = [{"color": "red", "duration": 7},
                        {"color": "yellow", "duration": 2},
                        {"color": "green", "duration": 7}]

    def running(self):
        for e in self.__color:
            print(f"Running {e['color']}")
            sleep(e["duration"])


traffic_light = TrafficLight()
traffic_light.running()
