"""
ДЗ после 7 и 8 уроков
Программа семантического анализа
"""
stop_words: tuple = (
    'в', 'без', 'до', 'из', 'к', 'на', 'по', 'о', 'от', 'перед', 'при',
    'через', 'с', 'у', 'за', 'над', 'об', 'под', 'про', 'для',
    'тоже', 'также', 'и', 'да', 'но', 'зато', 'только', 'либо', 'что',
    'когда', 'как', 'пока', 'чтобы', 'так', 'потому', 'хотя', 'если', 'несмотря',
    'ну', 'не', 'ни', 'ли', 'разве', 'неужели', 'будто', 'словно', 'вроде', 'бы',
    'же', 'то', 'пусть', 'ау', 'ах', 'ох', 'эге', 'уф', 'а', 'э', 'увы', 'фу', 'ого',
    'типа'
    )


def main() -> None:
    """
    Основной блок программы
    """
    text, filtr_text, matrix_has_got_you, i, strng = [], [], {}, 1, ' '
    print('Введите исходные предложения текста (Enter - закончить ввод):')
    while strng:
        strng = input(f'Предложение {i}: ').lower()
        if strng:
            for char in strng:
                if not char.isalpha():
                    strng = strng.replace(char, ' ')
            text.append(strng.split())
        i += 1
    print(text)
    for strng in text:
        filtr_text.append(list(filter(lambda x: x not in stop_words, strng)))
    print(filtr_text)
    set_text = set([word for strng in filtr_text for word in strng])
    for word in set_text:
        matrix_has_got_you.update({word: [strng.count(word) for strng in filtr_text]})
    print(matrix_has_got_you)


main()
