class Data:
    def __init__(self, to_data):
        self.to_data = str(to_data)


    @classmethod
    def data_meaning(cls, to_data):
        x = to_data.split(':')
        return int(x[0]), int(x[1]), int(x[2])

    @staticmethod
    def valid(d, m, y):
        if 0 < d < 32:
            if 0 < m < 13:
                if 0 <= y < 2022:
                    return 'Такая дата существует'
                else:
                    return 'Неверный год'
            else:
                return 'Неверный месяц'
        else:
            return 'Неверный день'


my_data = Data.data_meaning('10:11:2015')
print(my_data)
print(Data.valid(10, 12, 2015))
print(Data.valid(32, 12, 2015))
print(Data.valid(10, 13, 2015))
print(Data.valid(10, 12, 2035))