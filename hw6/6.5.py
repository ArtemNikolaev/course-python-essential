# https://github.com/ArtemNikolaev/gb-hw/issues/42
class Stationery:
    title = 'Канцелярская херня'

    def draw(self):
        print(self.title + ' чот рисует')


class Pen:
    title = 'Pen'

    def draw(self):
        print(self.title + ' penning')


class Pencil:
    title = 'Pencil'

    def draw(self):
        print(self.title + ' pencilling')


class Handle:
    title = 'Handle'

    def draw(self):
        print(self.title + ' handling')


Pen().draw()
Pencil().draw()
Handle().draw()
