from sys import argv

skript_name, name, work_h, many_h, prize = argv
try:
    bounty = int(work_h) * float(many_h) + int(prize)
    print(f'{name} заработал: {int(bounty)}')
except:
    print('Ошибка')
