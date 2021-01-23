'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

numerator = input("Введите числитель: ")
denominator = input("Введите знаменатель: ")
def calc(x, y):
    try:
        amount = int(x) / int(y)
    except ValueError:
        return None
    except ZeroDivisionError:
        return None

    return amount


print(calc(numerator, denominator))
