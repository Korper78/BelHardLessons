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


print(decode_bits("000000011100000"))
