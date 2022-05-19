"""
Урок 6
Домашнее задание
"""

# Задание 1.1 Десятичные в двоичные

def dec_to_bin(dec: int) -> str:
    # ret_bin = []
    # while dec > 0:
    #     ret_bin.append(f'{dec % 2}')
    #     dec //= 2
    # return ''.join(ret_bin[::-1]) if len(ret_bin) else '0'
    ret_bin = f'{dec:0b}'                                      # Ну или так )))))))
    return ret_bin

# Задание 1.2 Двоичные в десятичные

def bin_to_dec(my_bin: str) -> int:
    # ret_dec = 0
    # for i in range(len(my_bin)):    # Перебор двоичных цифр
    #     ret_dec += (int(my_bin[i])*2) ** (len(my_bin)-i-1)  # Двоичная цифра * 2 в степени разряда
    # return ret_dec if int(my_bin[-1]) else ret_dec - 1  # Страховка от 0 ** 0 == 1 в младшем разряде
    ret_dec = int(f'0b{my_bin}', base=2)    # Ну или так )))))))
    return ret_dec

# Задание 3. Азбука Морзе

def morze(txt_to_morze: str) -> str:
    azbuka_morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                      'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                      'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                      'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                      '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' ',
                    '.': 'ТЧК', ',': 'ЗПТ'}
    txt_in_morze = [f' {azbuka_morze[txt_to_morze[i].lower()]}' for i in range(len(txt_to_morze))]
    # for i in range(len(txt_to_morze)):
    #     txt_in_morze += f' {azbuka_morze[txt_to_morze[i].lower()]}'
    return ''.join(txt_in_morze).lstrip()

# Задание 4. Скроллинг списка

def scroll_list(in_list: list, shift: int, dir = True) -> list: # True - вправо, False - влево
    out_list = in_list[-shift:] + in_list[0:-shift] if not dir else in_list[shift::] + in_list[0:shift]
    return out_list

# Задание 5. Фильтрация списка

def filter_list(in_list: list) -> list:
    for el in in_list:
        try:
            in_list[in_list.index(el)] = float(el)  # Все числа переводим в float
        except ValueError:
            continue
    # out_list = list(filter(lambda x: type(x) is str, in_list))
    return list(filter(lambda x: type(x) is str, in_list)) #out_list

# Задание 6. Извращение списка))))

def revers_list(in_list: list) -> list:
    for i in range(len(in_list) // 2):
        in_list[i], in_list[-(i + 1)] = in_list[-(i + 1)], in_list[i]
    return in_list

# Задание 7. Случайности не случайны, особенно четные и нечетные))

def odd_even_list(in_list: list) -> list:
    out_list = sorted(in_list)
    return list(filter(lambda x: not (x % 2), out_list)) + list(filter(lambda x: x % 2, out_list))

# Задание 8. Суммы соседних чисел

def  neighb_sum_list(in_list: list) -> list:
    out_list = [in_list[i-1] + in_list[i+1] for i in range(len(in_list)-1)] + [in_list[0] + in_list[-2]]
    return list(zip(in_list, out_list))

# Задание 9. Выбор страны

def get_country(city: str) -> str:
    city_dict = {
        'Беларусь': ('Минск', 'Брест', 'Гродно', 'Гомель', 'Витебск', 'Могилев'),
        'Россия': ('Москва', 'Питер', 'Смоленск', 'Брянск', 'Псков', 'Белгород'),
        'Украина': ('Киев', 'Чернигов', 'Житомир', 'Ровно', 'Харьков', 'Одесса'),
    }
    # country = 'Город не найден'
    for key in city_dict:
        if city in city_dict[key]:
            return key
    return 'Город не найден'

# Задание 10. Словари в словаре

def get_dict() -> dict:
    out_dict = []
    in_dict_keys = ('FName', 'SName', 'Phone', 'Email')
    i = 1
    while True:
        print(f'Введите {i} абонента  (Enter - закончить ввод):')
        small_dict = []
        for key in in_dict_keys:
            val = input(f'Введите {key}:>')
            if val:
                small_dict.append(val)
            else:
                break
        if len(small_dict):
            out_dict.append([i,dict(zip(in_dict_keys, small_dict))])
            i += 1
        else:
            break
    return dict(out_dict) if len(out_dict) else {1: {'FName': 'Никого нет)))'}}

def wout_email(in_dict: dict) -> str:
    out_list = [val['FName'] if not ('Email' in val.keys() and val['Email']) else '' for val in in_dict.values()]
    # out_list = []
    # for val in in_dict.values():
    #     if not ('Email' in val.keys() and val['Email']):
    #         out_list.append(val['FName'])
    return ', '.join(sorted(out_list)).lstrip(', ')

# Выбор задания

choice = ' '
while choice not in 'Ee':
    try:
        choice = input('Выберите номер задания или выход 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / [E]xit:>')
        match choice:
            case '1':
                print(f"В двоичной системе = {dec_to_bin(int(input('Введите целое десятичное число:>')))}")
            case '2':
                print(f"В десятичной системе = {bin_to_dec(input('Введите двоичное число:>'))}")
            case '3':
                print(f"Текст в азбуке Морзе: {morze(input('Введите текст:>'))}")
            case '4':
                print(f"Сдвинутый список: {scroll_list(list(map(int, input('Введите через пробел числа:>').split())), int(input('Введите сдвиг:>')), bool(input('Вправо - True (default), Влево - False:>')))}")
            case '5':
                print(f"Отфильтрованный список: {filter_list(input('Введите через запятую c пробелом элементы списка:>').split(', '))}")
            case '6':
                print(f"Перевернутый список: {revers_list(list(map(int, input('Введите через пробел числа:>').split())))}")
            case '7':
                print(f"Отсортированный список чет/нечет: {odd_even_list(list(map(int, input('Введите через пробел числа:>').split())))}")
            case '8':
                print(f"Cписок с суммами соседних чисел: {neighb_sum_list(list(map(int, input('Введите через пробел числа:>').split())))}")
            case '9':
                print(f"Этот город в стране {get_country(input('Введите название города:>'))}")
            case '10':
                print(f"У следующих людей нет емейла: {wout_email(get_dict())}")
            case 'E' | 'e':
                print('Aufwiederseen!)))')
            case _:
                print('Оператор инвалид, повторите ввод :(')
    except Exception:
            print('Оператор инвалид детектед >:(')
