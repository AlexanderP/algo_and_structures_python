"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

import random

array = [random.randint(1, 100) for _ in range(40)]
if array[0] <= array[1]:
    minimum = array[0]
    oldminimum = array[1]
else:
    minimum = array[1]
    oldminimum = array[0]

for i in array[2:]:
    if minimum >= i:
        oldminimum = minimum
        minimum = i
    elif oldminimum >= i:
        oldminimum = i

print(f"В массиве\n{array}\n{minimum} и {oldminimum} являются"
      f"самыми минимальными элементами")
