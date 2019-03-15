"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
matrix = [[] for j in range(5)]

for i in range(5):
    while True:
        a = input("Введите 4 числа через пробел: ").split()
        if len(a) == 4:
            break
        else:
            print("Ошибка попробуйте еще раз.")
    a = list(map(int, a))
    matrix[i] += a
    matrix[i].append(sum(a))
print()
print("Матрица:")
for i in range(5):
    for j in range(4):
        print(matrix[i][j], end='\t')
    print(f"| {matrix[i][4]}")
