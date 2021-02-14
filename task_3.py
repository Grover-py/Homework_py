class List_of_numbers:
    my_list = []
    i = None
    while True:
        i = input('Введите число (для выхода введите "Q"): ')
        if i == 'Q' or i == 'q':
            break
        try:
            my_list.append(int(i))
        except:
            print('Программа принимает только числа')

    print(my_list)


x = List_of_numbers