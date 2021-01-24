from functools import reduce

my_generator = (el for el in range(100, 1001, 2))
sum_all = reduce(lambda x, y: x * y, my_generator)
print(sum_all)
