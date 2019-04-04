# 4.	Определить, какое число в массиве встречается чаще всего.

import random

array = [random.randint(1, 20) for _ in range(50)]

n = 0
a = ''

for i in array:
    j = len(list(filter(lambda x: x == i, array)))
    if j > n:
        a = i
        n = j

print(f"В массиве:\n{array}\nЧаще всего встречается число {a} - {n} раз")
