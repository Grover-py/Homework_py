class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки "{self.title}" ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки "{self.title}" карандашём'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки "{self.title}" маркером'

pen = Pen('Картина')
print(pen.draw())
pencil = Pencil('Картина')
print(pencil.draw())
handle = Handle('Картина')
print(handle.draw())