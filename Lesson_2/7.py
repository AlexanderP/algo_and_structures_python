"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def func(n):
    return n * (n + 1) / 2


def func2(n):
    if n == 0:
        return 0
    else:
        return n + func2(n - 1)


def func3(n):
    if n == 1:
        return "1"
    else:
        return str(func3(n - 1)) + ' + ' + str(n)


n = int(input("Введите число: "))

print("Проверить что:")
print(f'{func3(n)} = {n} * ({n} + 1) / 2')
print("\nПроверка:")
result = func2(n)
print(f'{result} = {n} * {n + 1} / 2')
print(f'{result} = {n * (n + 1)} / 2')
print(f'{result} = {int(n * (n + 1) / 2)}')
