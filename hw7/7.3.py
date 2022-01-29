# https://github.com/ArtemNikolaev/course-python-essential/issues/46
class Cell:
    def __init__(self, cells):
        self.__cells = cells

    @property
    def cells(self):
        return self.__cells

    def __add__(self, other):
        return Cell(self.__cells + other.cells)

    def __sub__(self, other):
        diff = self.__cells - other.cells
        if diff < 0:
            print('Операция вычитания недопустима')
        else:
            return Cell(diff)

    def __mul__(self, other):
        return Cell(self.__cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.__cells // other.cells)

    def __str__(self):
        return str(self.__cells)

    @staticmethod
    def make_order(cell_instance, order):
        cells = cell_instance.cells

        while cells > 0:
            if cells < order:
                amount = cells
                cells = 0
            else:
                amount = order
                cells -= order

            print('*' * amount)


cell1 = Cell(10)
cell2 = Cell(6)


print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)

print('cell1 make_order')
Cell.make_order(cell1, 4)

print('cell2 make_order')
Cell.make_order(cell2, 2)
