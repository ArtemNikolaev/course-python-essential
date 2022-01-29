# https://github.com/ArtemNikolaev/course-python-essential/issues/45
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def consumption(self):
        return 2 * self.size + 0.3


print(Coat(3.25).consumption())
print(Costume(0.35).consumption())
