import json
average_profit = 0
finish_list = []
profit_firm = {}
general_profit = {}
n = 0

my_file = open('txt_for_task_7.txt', mode = 'r',encoding = 'ANSI')

for el in my_file.readlines():
    name, form, profit, loss = el.split()
    data_profit_firm = int(profit) - int(loss)
    if data_profit_firm > 0:
        average_profit += data_profit_firm
        n += 1
    profit_firm[name] = int(data_profit_firm)

my_file.close()

if average_profit == 0:
    print('Все фирмы работают в убыток')
else:
    general_profit['average_profit'] = int(average_profit)
    finish_list.append(profit_firm)
    finish_list.append((general_profit))
    with open('json_for_task_7.json', 'w') as data_write:
        json.dump(finish_list, data_write)
    with open('json_for_task_7.json', 'r') as data_read:
        print(f'Был создан Json файл. Вот его содержимое: \n{data_read.read()}')
