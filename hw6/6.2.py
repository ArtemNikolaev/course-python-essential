# https://github.com/ArtemNikolaev/gb-hw/issues/39

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, as_mass, as_height):
        return self._length * self._width * as_mass * as_height


road = Road(20, 5000)
print(road.mass(25, 5))
