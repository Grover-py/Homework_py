from abc import ABC, abstractmethod

class Clothes():
    t = 0

    @abstractmethod
    def __init__(self, i):
        self.i = i

    def total():
        return f'Для пошива всей одежды понадобится: {round(Clothes.t, 2)} кв.м. ткани.'


class Coat(Clothes):
    def __init__(self, i):
        self.v = i
    def fabric(self):
        self.s = self.v / 6.5 + 0.5
        Clothes.t += self.s
        return f'Для пошива пальто понадобится: {round(self.s, 2)} кв.м. ткани.'

class Suit(Clothes):
    def __init__(self, i):
        self.h = i
    def fabric(self):
        self.s = self.h * 2 + 0.3
        Clothes.t += self.s
        return f'Для пошива костюма понадобится: {round(self.s, 2)} кв.м. ткани.'

coat_1 = Coat(5)
coat_2 = Coat(4)
suit_1 = Suit(0.89)

print(coat_1.fabric())
print(coat_2.fabric())
print(suit_1.fabric())
print(Clothes.total())