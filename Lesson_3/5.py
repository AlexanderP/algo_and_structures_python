# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
import random

a = None
n = ''

array = [random.randint(-100, 100) for _ in range(40)]

for i, j in enumerate(array):
    if j < 0:
        if a is None:
            n = i
            a = j
        elif a < j:
            n = i
            a = j

if a is None:
    print(f"В массиве:\n{array}\nНет отрицательных элементов")
else:
    print(f"В массиве:\n{array}\nМаксимальный отрицательный элемент {a} - "
          f"Находится на позиции {n}")
