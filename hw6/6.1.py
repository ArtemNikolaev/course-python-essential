# https://github.com/ArtemNikolaev/gb-hw/issues/38
from itertools import cycle
from time import sleep


class TrafficLight:
    __rules = {
        '🔴': 7,
        '🟡': 2,
        '🟢': 4,
    }
    __lights = ('🔴', '🟡', '🟢')
    __lights_cycle = cycle(__lights)
    __color = next(__lights_cycle)

    def running(self):
        print(self.__color)
        sleep(self.__rules[self.__color])
        self.__color = next(self.__lights_cycle)
        self.running()


light1 = TrafficLight()
light1.running()
