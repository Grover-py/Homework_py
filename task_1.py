my_file = open('txt_for_task_1.txt', 'w')
inp = input('Введи чё нить: ')

while True:
    if inp == '\n' or inp == '':
        break
    else:
        my_file.write(inp)
        inp = '\n' + input('Введи чё нить: ')

my_file.close()
