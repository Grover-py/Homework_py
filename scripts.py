import itertools

def gen_natural_num(start):
    my_list = (el for el in range(start, 11))
    return my_list
'''
Решение с помощью "itertools.count". но мне оно кажется хуже

def gen_natural_num(start):
    my_list = []
    for el in itertools.count(start, 1):
        if el > 10:
            break
        my_list.append(el)
    return iter(my_list)
'''

def gen_list_replay(x):
    my_list = []
    for el in itertools.cycle(x):
        if list.count(my_list, el) == 3:
            break
        else:
            my_list.append(el)
    return iter(my_list)
