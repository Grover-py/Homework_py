
def gen_factorial(x):
    finish_num = 1
    for i in range(1, x + 1):
        finish_num *= i
        yield finish_num


n = int(input("Введите число: "))
for el in gen_factorial(n):
    print(el)