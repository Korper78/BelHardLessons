# Добавляем
InString = input('А введи-ка целое число: ')
Digits = len(InString)
#print(Digits)
if not InString.isdigit():
    OutString = 'Ты меня за дурака держишь? >:((('
else:
    if Digits % 10 == 1 and Digits != 11:
        OutString = 'В этом числе {Digits} цифра'
    elif Digits % 10 in [2, 3, 4] and Digits not in [12, 13, 14]:
        OutString = f'В этом числе {Digits} цифры'
    else:
        OutString = f'В этом числе {Digits} цифр'
print(OutString)
