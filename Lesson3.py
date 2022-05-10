# Урок 3

def is_number(strng):
    try:
        float(strng)
        return True
    except ValueError:
        return False


# Задание 1
def task1():
    string = input('Введите-ка предложение: ')
    # print(string.find(' '))
    while ' ' not in string:
        string = input('Что-то пошло не так, попробуйте еще: ')
    choice = input('Пробелы в минусы, вариант 1 или 2 (1 / 2): ')
    while choice not in ('1', '2'):
        choice = input('Пробелы в минусы, вариант 1 или 2 (1 / 2): ')
    # print(choice)
    if choice == '1':
        print(f"Способ методом Replace: {string.replace(' ','-')}")
    else:
        words = string.split()
        string = '-'.join(words)
        print(f"Способ методами Split/Join: {string}")


# Задание 2
def task2():
    nums = []
    print('Введите три целых числа')
    for i in range(3):
        number = input(f'Введите {i+1} число: ')
        while not number.isdigit():
            number = input(f'Уточните {i+1} число: ')
        nums.append(int(number))
    avrg = round((nums[0] + nums[1] + nums[2])/3, 3)
    print(f'Среднее арифметическое {nums[0]}, {nums[1]} и {nums[2]} равняется {avrg}')


# Задание 3
def task3():
    name = input('Введите имя: ')
    city = input('Введите название города: ')
    age = input('Введите возраст в годах: ')
    while not age.isdigit():
        age = input('А поточнее: ')
    print("Форматирование через процент. Привет, я %s-летний %s  из города %s." % (age, name, city))
    print()
    print("Форматирование через format(). Привет, я {} из города {}, мне {} лет.".format(name, city, age))
    print()
    print(f"Форматирование через префикс f. Привет, меня зовут {name}, я {age}-летний житель города {city}")


# Задание 4
def task4():
    nums = []
    print('Введите три любых числа')
    for i in range(3):
        nums[i] = input(f'Введите {i+1} число: ')
        while not is_number(nums[i]):
            nums[i] = input(f'Уточните {i+1} число: ')
        # if float(number) > 0:
        #     pos += 1
        # elif float(number) < 0:
        #     neg += 1
    pos = (float(nums[0]) > 0) + (float(nums[1]) > 0) + (float(nums[2]) > 0)
    neg = (float(nums[0]) < 0) + (float(nums[1]) < 0) + (float(nums[2]) < 0)
    print('Положительных чисел: ', pos)
    print('Отрицательных чисел: ', neg)
    print('Нулей: ', 3-pos-neg)


# Основная программа
print('Домашнее задание с занятия №3')
choice = ''  # input('Выберите номер задачи (1-4) или exit: ')
while choice != 'exit':  # not in ('1', '2', '3', '4'):
    choice = input('Выберите номер задачи (1-4) или exit: ')
    match choice:
        case '1':
            task1()
        case '2':
            task2()
        case '3':
            task3()
        case '4':
            task4()
        case _:
            print('Неверный выбор')
