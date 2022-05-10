# Урок 4

# Задание 1. Список из степеней 2

grade = input('Введите краюнюю степень:>')
while not grade.isdigit():
    grade = input('Уточните:>')
grade_list = [2**i for i in range(1, int(grade)+1)]
print(f'Список степеней числа 2 до {grade}:\n{grade_list}\n')

# Задание 2. Словарь вхождений букв в тексте

sentence = input('Введите любой текст:>')
# sentence_list = list(sentence)
# sentence_set = set(sentence)
# sentence_dict = {k: sentence_list.count(k) for k in sentence_set}
sentence_dict = {k: sentence.count(k) for k in set(sentence)}
print(f'{sentence_dict}\n')

# Задание 3*

length = input('Введите длину словаря:>')
while not length.isdigit():
    length = input('Уточните:>')
dbl_dict = {n: {'name': input('Введите имя:>'), 'email': input('Введите email:>')} for n in range(int(length))}
print(dbl_dict)
