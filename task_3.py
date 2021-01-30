my_file = open('txt_for_task_3.txt', mode = 'r',encoding = 'ANSI')
content = my_file.readlines()

small_salary = []
total_salary = 0
for el in content:
    name = el.split()
    total_salary += int(name[1])
    if int(name[1]) < 20000:
        small_salary.append(name[0])

print(f'Сотрудники с окладом менее 20000: {small_salary}')
print(f'Сумма окладов всех сотрудников: {total_salary}')

my_file.close()