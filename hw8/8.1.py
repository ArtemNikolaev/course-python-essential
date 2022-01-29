# https://github.com/ArtemNikolaev/course-python-essential/issues/47
class Date:
    def __init__(self, date):
        self.__date = self.extraction(date)

    @property
    def date(self):
        return self.__date

    @classmethod
    def extraction(cls, date):
        result = [int(val) for val in date.split('-')]
        if not cls.validate(result):
            raise NameError('Unnapropriate date')

        return result

    @staticmethod
    def validate(value):
        if value[0] < 1 or value[0] > 31 \
                or value[1] < 1 or value[1] > 12 \
                or value[2] < 0 or value[2] > 2022:
            return False

        return True

    def __str__(self):
        return str(self.__date)


print(Date('29-01-2022'))
