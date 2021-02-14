class My_warehouse:
    warehouse = []
    quantity = 0


class Equipment:
    def __init__(self, name, mass):
        try:
            My_warehouse.warehouse.append({'name': str(name), 'mass': int(mass)})
            My_warehouse.quantity += 1
        except:
            print('Не реальные параметры неучтённой техники')


class Printer(Equipment):
    def __init__(self, mass, paper_size):
        try:
            My_warehouse.warehouse.append({'paper_size': str(paper_size), 'mass': int(mass)})
            My_warehouse.quantity += 1
        except:
            print('Не реальные параметры принтера')


class Scanner(Equipment):
    def __init__(self, mass, availability_of_colors):
        try:
            My_warehouse.warehouse.append({'availability_of_colors': bool(availability_of_colors), 'mass': int(mass)})
            My_warehouse.quantity += 1
        except:
            print('Не реальные параметры сканера')


class Copier(Equipment):
    def __init__(self, mass, print_speed):
        try:
            My_warehouse.warehouse.append({'print_speed': int(print_speed), 'mass': int(mass)})
            My_warehouse.quantity += 1
        except:
            print('Не реальные параметры ксерокса')


printer = Printer(50, 'A4')
scanner = Scanner(55, True)
copier = Copier(43, 8)
random_device = Equipment('pen', 1)

print(f'Количество предметов на складе: {My_warehouse.quantity}')
print(f'Список всего на складе: {My_warehouse.warehouse}')
