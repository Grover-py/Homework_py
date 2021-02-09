class Cell:
    def __init__(self, cl):
        self.cl = int(cl)
    def __add__(self, other):
        return f'Соединение двух клеток в одну большую. Размер новой клетки: {self.cl + other.cl}'

    def __sub__(self, other):
        s = self.cl - other.cl
        return f'От клетки откусили кусочек, теперь она: {s}' if s > 0 else 'Клетка была съедина полностью'

    def __mul__(self, other):
        return f'Клетка поглотила {other.cl} клеток себе подобных, теперь она: {self.cl * other.cl}'

    def __truediv__(self, other):
        return f'Клетка распалась (как СССР) на {other.cl} равных клеток, теперь её размер {self.cl / other.cl}'

    def make_order(self, n):
        data = ''
        x = self.cl
        while True:
            if x > n:
                data = data + '*' * n + '\n'
                x -= n
            elif x == n:
                data = data + '*' * n
                break
            else:
                data = data + '*' * x
                break
        return data


cell = Cell(12)
cell_2 = Cell(2)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(5))