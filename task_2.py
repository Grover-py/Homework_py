my_file = open('txt_for_task_2.txt', mode = 'r',encoding = 'ANSI')

content = my_file.read()
content_lowercase = content.split('\n')
print(f'Строк в текстовом файле: {len(content_lowercase)}')

n = 1
for el in content_lowercase:
    number_of_words = len(el.split())
    print(f'Слов в строке № {n}: {number_of_words} ')
    n += 1

my_file.close()