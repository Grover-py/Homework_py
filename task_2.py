class My_division:
    def __init__(self, divider, denominator):
        self.divider = int(divider)
        self.denominator = int(denominator)

    def zero_check(self):
        try:
            return self.divider / self.denominator
        except:
            return 'Делить на ноль нельзя'


x = My_division(10, 5)
y = My_division(10, 0)
print(x.zero_check())
print(y.zero_check())
