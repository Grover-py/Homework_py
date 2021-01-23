'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
'''

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))


def my_func(n_1, n_2, n_3):
    my_list = sorted([n_1, n_2, n_3])
    big_sum = my_list[2] + my_list[1]
    return big_sum


print(my_func(num_1, num_2, num_3))
