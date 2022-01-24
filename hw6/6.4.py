# https://github.com/ArtemNikolaev/gb-hw/issues/41

class Car:
    _speed = 0
    is_police = False
    _speed_limit = float('inf')

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self):
        self._speed += 20
        if self._speed > self._speed_limit:
            self._speed = self._speed_limit

    def stop(self):
        self._speed = 0

    def turn(self, direction):
        print(self.name + ' повернула ' + direction)

    def show_speed(self):
        print(self.name + ' скорость: ' + str(self._speed))


class TownCar(Car):
    _speed_limit = 60


class SportCar(Car):
    _speed_limit = 120


class WorkCar(Car):
    _speed_limit = 40


class PoliceCar(Car):
    is_police = True


town_car = TownCar('black', 'Ruhla')
town_car.go()
town_car.show_speed()
town_car.go()
town_car.show_speed()
town_car.go()
town_car.show_speed()
town_car.go()
town_car.show_speed()
town_car.turn('left')




