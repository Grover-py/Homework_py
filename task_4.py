
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

finish_generator = (el for el in my_list if list.count(my_list, el) == 1)

print(list(finish_generator))
