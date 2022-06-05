from itertools import groupby

digs = [5,4,3,2,1,5,4,3,2,10,10]
print(*filter(lambda x: digs.count(x) % 2, set(digs)))

iterable = [1,2,2,3,3]
print([k for k, g in groupby(iterable)])

def tribonacci(signature, n):
    # if n < 4:
    #     return signature[0:n]
    # else:
    while len(signature) <n:
        signature.append(sum(signature[-3:]))
    # trib = {
    #     0: [],
    #     1: signature[0:0],
    #     2: signature[0:1],
    #     3: signature[:],
    #     4: [    *signature, sum([-3: -1]) for i in range(3, n+1)]
    # }[4 if n > 3 else n]
    return signature[0:n]

print(tribonacci([1, 2, 3], 10))


def find_nb(m):
    n = 0
    while m > 0:
        n += 1
        m -= n**3
    return -1 if m else n

print(find_nb(91716553919377))


def is_prime(num):
    # if num < 2:
    #     return f'{num} is not prime'
    # elif num is any(2, 3, 5, 7):
    #     return f'{num} is prime'
    # elif
    if num < 2: return False
    i = int(num ** (0.5))
    while num % i:
        i -= 1
    # return f'{num} is not prime' if (i - 1) else f'{num} is prime'
    return not bool(i - 1)

print(is_prime(39))


def duplicate_encode(word):
    return ''.join([')' if word.lower().count(c) - 1 else '(' for c in word.lower()])

print(duplicate_encode('))(()())())'))


def wave(people):
    return [people[:i] + people[i:].capitalize() for i in range(len(people)) if people[i] != ' ']

print(wave('two words'))


def pick_peaks(arr):
    out = {'pos':[], 'peaks':[]}
    for i in range(1, len(arr)):
        # if arr[i] > arr[i-1]:
        #     j = i
        # if arr[i] > arr[i+1]:
        #     out['pos'].append(j)
        #     out['peaks'].append(arr[j])
        for j in arr[i:]:
            if j > arr[i]:
                break
            elif j < arr[i] and arr[i-1] < arr[i]:
                out['pos'].append(i)
                out['peaks'].append(arr[i])
                break
    return out

print((pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])))


ar = [[1,4], [11, 12], [3, 5], [6, 11], [2, 6]]
print(sorted(ar))

def sum_of_intervals(intervals):
    sort_int = [list(inter) for inter in sorted(intervals)]
    ovrlap_int = []
    # print(sort_int)
    for int1 in sort_int:
        indx_inter = sort_int.index(int1)+1
        for int2 in sort_int[indx_inter:]:
            if int1[1] >= int2[0]:
                int1[1] = max(int1[1], int2[1])
                sort_int.remove(int2)
    # print(sort_int)
    return sum([inter[1] - inter[0] for inter in sort_int])

print(sum_of_intervals([(1,4), (11, 12), (3, 5), (6, 11), (2, 6)]))
