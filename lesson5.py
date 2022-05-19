# Классная работа

# strng = input('Введите текст:>')
# chars = []
# for char in strng:
#     if not (strng.count(char) - 1):
#         chars.append(char)
# print(chars)

# word = input('Введите слово:>').lower().replace(' ', '')
# print('Не непалиндром' if word == word[::-1] else 'Не палиндром, а непалиндром!')

# text = input('Введите слово:>')
# vowels = 'aoeui'
# glas = 0
# soglas = 0
# for char in text:
#     if char.isalpha():
#         if char.lower() in vowels:
#             glas += 1
#         else:
#             soglas += 1
# print(f'{glas} гласных, {soglas} согласных')


# Домашняя работа

# Задание 1
def task5_1():
    while True:
        try:
            n = int(input('Введите N:>'))
            m = int(input('Введите M:>'))
            k = int(input('Введите K:>'))
        except Exception:
            print('Что-то не так, повторите ввод')
        else:
            break

    k += m - (k % m)                               # Приводим К к ближайшему большему кратному М
    n_digs = [i for i in range(k, k + m * n, m)]   # Вариант с генератором
    # n_digs = []                                  # Вариант с циклом
    # k += 1
    # n -= 1
    # while len(n_digs) <= n:
    #     if not k % m:
    #         n_digs.append(k)
    #         k += m
    #     else:
    #         k += 1
    print(n_digs)

# Задание 2
def task5_2():
    while True:
        try:
            num_1 = float(input('Введите первое число:>'))
            action = input('Введите действие:>')
            num_2 = float(input('Введите второе число:>'))
        except Exception:
            print('Калькулятор сломался, повторите ввод :(')
        else:
            if action in ('+-*/'):
                break
            print('Калькулятор сломался, повторите ввод :(')
    match action:
        case '+':
            result = num_1 + num_2
        case '-':
            result = num_1 - num_2
        case '*':
            result = num_1 * num_2
        case '/':
            if num_2 != 0:
                result = num_1 / num_2
            else:
                print('Принято считать, что на ноль делить нельзя! :b')
                result = 'Бесконечности'
    print(f'Результат выражения "{num_1} {action} {num_2}" равен {result}')

# Задание 3*
def task5_3():
    while True:
        try:
            num_n = int(input('Введите предел вывода четных чисел:>'))
        except Exception:
            print('Оператор инвалид, повторите ввод :(')
        else:
            if num_n > 1:
                break
            print('Оператор инвалид, повторите ввод :(')

    evens = [i for i in range(2, num_n+1, 2)]
    while len(evens) > 5:
        print(evens[0:5])
        del evens[0:5]
    print(evens)

# Выбор задания
choice = ' '
# print(choice in 'Ee')
while choice not in 'Ee':
    choice = input('Выберите номер задания или выход 1 / 2 / 3 / [E]xit:>')
    match choice:
        case '1':
            task5_1()
        case '2':
            task5_2()
        case '3':
            task5_3()
        case 'E' | 'e':
            print('Aufwiederseen!)))')
        case _:
            print('Оператор инвалид, повторите ввод :(')

