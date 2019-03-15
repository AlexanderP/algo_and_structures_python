# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[str(random.randint(1, 99)) for j in range(12)] for i in range(8)]

print("Матрица")
for i in matrix:
    for j in i:
        if len(j) == 1:
            print(f' {j}', end=" ")
        else:
            print(j, end=" ")
    print()
print()
minimum = [int(matrix[0][i]) for i in range(len(matrix[1]))]

for i in range(len(matrix[1])):
    for j in range(len(matrix)):
        if minimum[i] > int(matrix[j][i]):
            minimum[i] = int(matrix[j][i])

maximum = minimum[0]

for i in minimum[1:]:
    if maximum < i:
        maximum = i

print(f"Максимальный элемент среди минимальных элементов столбцов матрицы равен"
      f" {maximum}")
