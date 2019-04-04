"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def func(n, i=1, summ=1.0, number=1.0):
    if i == n:
        return summ
    else:
        next_number = number * - 0.5
        return func(n, i + 1, summ + next_number, next_number)


n = int(input("Введите число: "))
print(func(n))
