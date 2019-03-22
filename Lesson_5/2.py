"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections

index = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d",
         "e", "f"]


def mul_hex(a, b, verbose=False):
    if len(a) < len(b):
        a, b = b, a
    original_a = a
    original_b = b
    a = [int(f'0x{i}', 16) for i in a]
    b = [int(f'0x{i}', 16) for i in b]
    lst = []
    num_b2 = 0
    for num_b, hex_b in enumerate(b[::-1]):
        if hex_b != 0:
            lst.append(collections.deque())
            for i in range(num_b):
                lst[num_b2].appendleft(" ")
            for hex_a in a[::-1]:
                lst[num_b2].appendleft(hex_a * hex_b)
            num_b2 += 1
    for i in lst:
        tmp = 0
        for j in reversed(range(-len(i), 0)):
            if i[j] != " ":
                i[j] += tmp
                tmp, i[j] = i[j] // 16, i[j] % 16
        if tmp != 0:
            i.appendleft(tmp)
    len_max = len(max(lst, key=len))
    for i in lst:
        if len(i) < len_max:
            i.extendleft([" " for j in range(len_max - len(i))])
    result = collections.deque()
    for i in range(len_max):
        sums = 0
        for j in range(len(lst)):
            if lst[j][i] != " ":
                sums += lst[j][i]
        result.append(sums)
    tmp = 0
    for j in reversed(range(-len(result), 0)):
        result[j] += tmp
        tmp, result[j] = result[j] // 16, result[j] % 16
    if tmp != 0:
        result.appendleft(tmp)
    result = [index[i] for i in result]
    if verbose is True:
        for j in lst:
            for n, i in enumerate(j):
                if j[n] != " ":
                    j[n] = index[i]
        print("Умножение:")
        if len(original_a) < len_max:
            print(" " * (len_max - len(original_a)), end="")
        print("".join(original_a))
        if len(original_b) < len_max:
            print(" " * (len_max - len(original_b)), end="")
        print("".join(original_b))
        print(len_max * "-")
        for i in lst:
            print("".join(i))
        print(len_max * "-")
        print("".join(result))
    return result


def sum_hex(a, b, verbose=False):
    if len(a) < len(b):
        a, b = b, a
    lst = []
    lst.append(collections.deque([int(f'0x{i}', 16) for i in a]))
    lst.append(collections.deque([int(f'0x{i}', 16) for i in b]))
    len_max = len(max(lst, key=len))
    for i in lst:
        if len(i) < len_max:
            i.extendleft([" " for j in range(len_max - len(i))])
    result = collections.deque()
    for i in range(len_max):
        sums = 0
        for j in range(len(lst)):
            if lst[j][i] != " ":
                sums += lst[j][i]
        result.append(sums)
    tmp = 0
    for j in reversed(range(-len(result), 0)):
        result[j] += tmp
        tmp, result[j] = result[j] // 16, result[j] % 16
    if tmp != 0:
        result.appendleft(tmp)
    result = [index[i] for i in result]
    if verbose is True:
        print("Сложение:")
        if len(a) < len_max:
            print(" " * (len_max - len(a)), end="")
        print("".join(a))
        if len(b) < len_max:
            print(" " * (len_max - len(b)), end="")
        print("".join(b))
        print(len_max * "-")
        print("".join(result))
    return result


a = ["a", "2"]
b = ["c", "4", "f"]

print(f"Умножение '{''.join(a)}' на '{''.join(b)}' равно "
      f"'{''.join(mul_hex(a, b))}'")
print(f"Сложение '{''.join(a)}' на '{''.join(b)} равно "
      f"'{''.join(sum_hex(a, b))}'")

print("-" * 60)
a = ["a", "2", "4", "6", "d", "5", "f"]
b = ["c", "4", "f", "0", "0", "8"]
mul_hex(a, b, True)
print()
print("-" * 60)
sum_hex(a, b, True)
