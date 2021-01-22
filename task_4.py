'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
'''

x = int(input('Введите число x: '))
y = int(input('Введите степень y: '))


def my_func(x, y):
    sum = x
    n = 1
    if y > 0:
        while n != y:
            sum = sum * x
            n += 1
    elif y < 0:
        n = -1
        while n != y:
            sum = sum * x
            n -= 1
        sum = 1 / sum
    else:
        sum = 1

    return sum

print(my_func(x, y))
print(x**y)
