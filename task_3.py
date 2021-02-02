class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']



x = Position('Андрей', 'Алтухов', 'спец', 100, 50)
print(f'Сотрудник: {x.get_full_name()}')
print(f'Заработал: {x.get_total_income()} попугаев')