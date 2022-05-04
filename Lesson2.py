# Добавляем
InString = input('А введи-ка целое число: ')
Digits = len(InString)
#print(Digits)
if not InString.isdigit():
    OutString = 'Ты меня за дурака держишь? >:((('
else:
    if Digits % 10 == 1 and Digits != 11:
        OutString = 'В этом числе '+str(Digits)+' цифра'
    elif Digits % 10 in [2, 3, 4] and Digits not in [12, 13, 14]:
        OutString = 'В этом числе ' + str(Digits) + ' цифры'
    else:
        OutString = 'В этом числе ' + str(Digits) + ' цифр'
print(OutString)
