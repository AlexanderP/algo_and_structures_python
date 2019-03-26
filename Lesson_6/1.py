"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile

"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


@profile
def func_while(n):
    s = ''
    while True:
        s += str(n % 10)
        n //= 10
        if n == 0:
            return s


@profile
def func_reversed(n):
    return ''.join(reversed(str(n)))


@profile
def func_collection(n):
    return str(n)[::-1]


i = 12 ** 222222

# func_while(i)
"""
Line #    Mem usage    Increment   Line Contents
================================================
    24     13.5 MiB     13.5 MiB   @profile
    25                             def func_while(n):
    26     13.5 MiB      0.0 MiB       s = ''
    27     13.5 MiB      0.0 MiB       while True:
    28     14.1 MiB      0.1 MiB           s += str(n % 10)
    29     14.1 MiB      0.3 MiB           n //= 10
    30     14.1 MiB      0.0 MiB           if n == 0:
    31     13.9 MiB      0.0 MiB               return s
"""
# func_collection(i)
"""
Line #    Mem usage    Increment   Line Contents
================================================
    37     13.7 MiB     13.7 MiB   @profile
    38                             def func_collection(n):
    39     13.8 MiB      0.2 MiB       return str(n)[::-1]
"""
# func_reversed(i)
"""
Line #    Mem usage    Increment   Line Contents
================================================
    33     13.6 MiB     13.6 MiB   @profile
    34                             def func_reversed(n):
    35     13.7 MiB      0.2 MiB       return ''.join(reversed(str(n)))
"""

"""
Вывод:
При работе большими числами оптимальный алгоритм по расходыванию памяти является 
преобразование в строку и обратный вывод с помощью [::-1]. Одинаковый объем
памяти показала функция reversed. Самый ресурсоемкий метод, это математический
с использованием цикла.
"""

"""
--------------------------------------------------------------------------------------
"""

"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


@profile
def func_while2(n):
    number = 1
    sum = 1
    for i in range(n):
        number = number * - 0.5
        sum += number
    return sum


@profile
def func_generator(n):
    return 1 + sum([(- 0.5) ** i for i in range(1, n)])


# func_generator(10000)
"""
Line #    Mem usage    Increment   Line Contents
================================================
    43     13.2 MiB     13.2 MiB   @profile
    44                             def func_generator(n):
    45     13.6 MiB      0.4 MiB       return 1 + sum([(- 0.5) ** i for i in range(1,n)])
"""

# func_while2(10000)
"""
Line #    Mem usage    Increment   Line Contents
================================================
    35     13.6 MiB     13.6 MiB   @profile
    36                             def func_while2(n):
    37     13.6 MiB      0.0 MiB       number = 1
    38     13.6 MiB      0.0 MiB       sum = 1
    39     13.6 MiB      0.0 MiB       for i in range(n):
    40     13.6 MiB      0.0 MiB           number = number * - 0.5
    41     13.6 MiB      0.0 MiB           sum += number
    42     13.6 MiB      0.0 MiB       return sum
"""
"""Вывод:
При расчете суммы 10000 элементов последовательности, оптимальный алгоритм по
расходыванию памяти является использования цикла относительно варианта с
генератором.
"""
