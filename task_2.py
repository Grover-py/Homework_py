class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 0.025
        self.height = 5

    def calc(self):
        finish_sum = self._length * self._width * self.weight * self.height
        print(f'Потребуется {int(finish_sum)} тонн асфальта')

x = Road(5000, 20)
x.calc()
