def dirReduc(arr):
    nul_dir = ('NORTHSOUTH', 'SOUTHNORTH', 'WESTEAST', 'EASTWEST')
    i = 0
    while i < len(arr):
        for j in range(i, len(arr)):
            # i = arr.index(cur_dir)
            if ''.join(arr[j:j + 2]) in nul_dir:
                del arr[j:j + 2]
                i = -1
                break
        i += 1
    return arr


print(dirReduc(["NORTH", "SOUTH", "EAST", "WEST"]))


def move_zeros(array):
    # zeros = array.count(0)
    # array = [num for num in array if num] + [0]*zeros
    return [num for num in array if num] + [0] * array.count(0)


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))


def valid_solution(board):
    cntrl_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    row_check = all([set(row) == cntrl_set for row in board])
    print(row_check)
    col_chek = all([{row[i] for row in board} == cntrl_set for i in range(9)])
    print(col_chek)
    blck_chek = all(
        [{row[j] for j in range(i, i + 3) for row in board[k:k + 3]} == cntrl_set for i in (0, 3, 6) for k in
         (0, 3, 6)])
    print(blck_chek)
    return all([row_check, col_chek, blck_chek])


print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 6, 8, 1, 7, 9]
]))


def decode_bits(bits):
    bits_2_morse = {
        1: '.',
        3: '-',
        -1: '',
        -3: ' ',
        -7: '   '
    }
    bit_list = []
    i1, i0 = 0, 0
    bits.strip('0')
    for char in bits:
        match char:
            case '1':
                if i0:
                    bit_list.append(-i0)
                    i1, i0 = 1, 0
                else:
                    i1 += 1
            case '0':
                if i1:
                    bit_list.append(i1)
                    i1, i0 = 0, 1
                else:
                    i0 += 1
    bit_list.append(i1 - i0)
    if bit_list[0] < 0:
        del bit_list[0]
    if bit_list[-1] < 0:
        del bit_list[-1]
    print(bit_list)
    tu = min([abs(x) for x in bit_list])
    print(tu)
    # tu0 = min([-x for x in bit_list if x <0])
    morse = ''
    for i in bit_list:
        morse += bits_2_morse[i / tu]
    # bits = bits.replace('111111', '-')
    # bits = bits.replace('11', '.')
    # bits = bits.replace('0000', ' ')
    # bits = bits.replace('00', '')
    return morse.strip()


print(decode_bits("0000001011100000"))


from collections import Counter
from itertools import groupby, product
def mix(s1, s2):
    str1 = Counter([char for char in s1 if char.isalpha() and char.islower() and (s1.count(char) > 1)])
    str2 = Counter([char for char in s2 if char.isalpha() and char.islower() and (s2.count(char) > 1)])
    str3 = str2 | str1
    res_str = sorted([f'{"=" if str1[k] == str2[k] else "1" if str1[k] > str2[k] else "2"}:' + ''.join(list(g)) for k, g in groupby(sorted(str3.elements()))], key=lambda x: x[0])
    return '/'.join(sorted(res_str, key=lambda x: len(x), reverse=True))

print(mix("mmmmm m nnnnn y&friend&Paul has heavy hats! &", "my frie n d Joh n has ma n y ma n y frie n ds n&"))


def get_pins(observed: str) -> list[str]:
    keypad2 = ('08', '124', '2153', '326', '4157', '52684', '6359', '748', '85907', '968')
    return [''.join(combo) for combo in product(*[keypad2[int(char)] for char in observed])]

print(sorted(get_pins('8')))


from math import gcd

def solution(a: list[int]) -> int:
    # a.sort()
    # if len(set(a)) > 1:
    #     a[a.index(max(a))] -= a[a.index(min(a))]
    #     return solution(a)
    # else:
    #     return sum(a)

    # return sum(a) if a == a[::-1] else solution(a)

    # set_a = set(a)
    # while len(set_a) > 1:
    # while len(set(a)) > 1:
        # a.append(max(a) - min(a))
        # a.remove(max(a))
        # while not all(a[0] == aa for aa in a):
        # a.sort()
        # a[a.index(max(a))] -= a[a.index(min(a))]
        # a.insert(-2, a.pop(-1) - a[-1])

        # a.append(a.pop(a.index(max(a))) - max(a))

        # a.sort()
        # a = list(accumulate(a, lambda x, y: y if x == y else y - x))

        # a = list(map(lambda x, y: abs(x-y) if x-y else x, a, a[-1:]+a[:-1]))

        # a.append(max(a) - a.remove(max(a))[0])
        # m = max(set_a)
        # set_a.remove(m)
        # set_a.add(max(set_a) - min(set_a))
        # set_a.remove(max(set_a))
    # return len(a) * max(set_a)
    return len(a) * gcd(*a)

print(solution([1, 21, 55]))

def sum_for_list(lst: list[int]) -> list[list[int]]:
    """
    Поиск простых делителей и вычисление сумм элементов списка, кратных имю
    :param lst: входящий список положительных и отрицательных целых
    :return: вложенный список простых делителей и сумм
    """
    # p = 2
    # # norm_lst = sorted([abs(x) for x in lst])
    # res_lst = []
    # while p <= max([abs(x) for x in lst]) // 2 + 1:
    #     for pp in range(2, int(p ** 0.5 + 1)):
    #         if p % pp == 0:
    #             break
    #     else:
    #         # comp_list = [x for x in lst if not (x % p)]
    #         if comp_lst := [x for x in lst if not (x % p)]:
    #             # res_lst.append([p, sum(comp_lst)])
    #             res_lst.append([p, comp_lst])
    #     p += 1 if p == 2 else 2
    # res_lst += [[abs(p), [p]] for p in set(lst) - {y for x in res_lst for y in x[1]}]
    # # for x in res_lst:
    # #     print(f'{x[0]} : {x[1]}')
    # return [[x[0], sum(x[1])] for x in res_lst]

    """
    Вариант 2. В множестве накапливаем уникальные простые делители всех элементов списка,
    включая элементы - простые числа
    """
    set_lst = set()
    for el in lst:
        p = 2
        while p * p <= abs(el):
            if el % p:
                p += 1 if p == 2 else 2
            else:
                el //= p
                set_lst.add(p)
        if abs(el) > 1:
            set_lst.add(abs(el))
    print(set_lst, lst)
    return sorted([[p, sum([x for x in lst if not (x % p)])] for p in set_lst], key=lambda x: x[0])

print(sum_for_list([15, 30, -127, 51]))
