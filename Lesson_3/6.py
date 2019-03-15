"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

array = [random.randint(1, 100) for _ in range(40)]
maximum = array[0]
nmax = 0
nmin = 0
minimum = array[0]

for i, j in enumerate(array[1:], 1):
    if maximum < j:
        maximum = j
        nmax = i
    if minimum > j:
        minimum = j
        nmin = i

if nmax < nmin:
    array2 = array[nmax + 1:nmin]
else:
    array2 = array[nmin + 1:nmax]

print(f"Сумму элементов, находящихся "
      f"между минимальным[{nmin}] и максимальным[{nmax}] элементами массива\n"
      f"{array}\nравна {sum(array2)}")
