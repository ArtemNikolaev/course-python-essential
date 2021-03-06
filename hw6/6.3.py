# https://github.com/ArtemNikolaev/gb-hw/issues/40

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


ivan = Position('Ivan', 'Petrov', 'top-hue', {"wage": 1, 'bonus': 2})
print(ivan.get_full_name(), ivan.get_total_income())
