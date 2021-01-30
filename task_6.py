def num_is_str(x):
    data_str = ''
    for el in x:
        try:
            if 0 <= int(el) <= 9:
                data_str = data_str + str(el)
        except:
            el = el
    if data_str == '':
        return 0
    else:
        return int(data_str)

my_dict = {}
with open('txt_for_task_6.txt', mode = 'r',encoding = 'ANSI') as content:
    for el in content.readlines():
        name, h_1, h_2, h_3 = el.split()
        my_dict[name] = num_is_str(h_1) + num_is_str(h_2) + num_is_str(h_3)

print(my_dict)
