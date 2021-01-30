my_file = open('txt_for_task_5.txt', mode = 'w', encoding = 'ANSI')

num = ''

while num != 'Q':
    num = input('Введите число, для выхода введите "Q": ')
    try:
        num = int(num)
        data_write = str(num) + ' '
        my_file.write(data_write)
        my_file.close()
        my_file = open('txt_for_task_5.txt', mode='r+', encoding='ANSI')
        content = my_file.read()
        x = 0
        for el in content.split():
            x += int(el)
        print(f'Сумма чисел в файле: {x}')
    except:
        print('Вы ввели не число, попробуйте ещё раз.')

my_file.close()