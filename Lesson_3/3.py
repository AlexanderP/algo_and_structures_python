# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

array = [random.randint(1, 100) for _ in range(30)]
maximum = array[0]
nmax = 0
nmin = 0
minimum = array[0]

print(array)
for i, j in enumerate(array[1:], 1):
    if maximum < j:
        maximum = j
        nmax = i
    if minimum > j:
        minimum = j
        nmin = i

array[nmax], array[nmin] = array[nmin], array[nmax]
print(array)
