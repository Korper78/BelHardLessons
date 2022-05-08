# Урок 3

# Задание 1 способ 1
def task1():
    string = input('Введите-ка предложение: ')
    # print(string.find(' '))
    while string.find(' ') < 0:
        string = input('Что-то пошло не так, попробуйте еще: ')
    choice = input('Пробелы в минусы, вариант 1 или 2 (1 / 2): ')
    while choice not in ['1', '2']:
        choice = input('Пробелы в минусы, вариант 1 или 2 (1 / 2): ')
    # print(choice)
    if choice == '1':
        print(f"Способ методом Replace: {string.replace(' ','-')}")
    else:
        words = string.split()
        string = '-'.join(words)
        print(f"Способ методами Split/Join: {string}")


# Основная программа
task1()
