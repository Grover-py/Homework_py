class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a} {self.b + other.b}'

    def __mul__(self, other):
        return f'{self.a * other.a} {self.b * other.b}'


n_1 = ComplexNumber(1, -2)
n_2 = ComplexNumber(3, 4)
print(n_1 + n_2)
print(n_1 * n_2)