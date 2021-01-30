from translate import Translator
translator = Translator(to_lang="ru")

my_file_in = open('txt_for_task_4.txt', mode = 'r', encoding = 'ANSI')
my_file_out = open('txt_for_task_4_1.txt', mode = 'w', encoding = 'ANSI')

for el in my_file_in.readlines():
    data_el = el.split()
    write_el = f'{str(translator.translate(data_el[0]))} {str(data_el[1])} {str(data_el[2])} \n'
    my_file_out.write(write_el)

my_file_out.close()
my_file_in.close()
