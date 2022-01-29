# https://github.com/ArtemNikolaev/course-python-essential/issues/44
class Matrix:
    def __init__(self, matrix):
        self.__matrix = matrix

    @property
    def matrix(self):
        return self.__matrix

    def __str__(self):
        return str(self.__matrix)

    def __add__(self, other):
        if not len(self.__matrix) == len(other.matrix) or \
                not len(self.__matrix[0]) == len(other.matrix[0]):
            print('Длина и/или ширина матриц отличается')
            return False

        result = [];
        for i in range(0, len(self.__matrix)):
            result.append([])
            for j in range(0, len(self.__matrix[i])):
                result[i].append(self.__matrix[i][j] + other.matrix[i][j])
        return Matrix(result)


src1 = [
    [31, 32],
    [37, 43],
    [51, 86],
]

src2 = [
    [9, 8],
    [3, 7],
    [9, 4],
]

print(Matrix(src1) + Matrix(src2))
