"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random
import timeit
from memory_profiler import profile

lst = [random.randint(-100, 100) for _ in range(1000)]


# @profile
def cocktail_sort(lst):
    left = 0
    rigt = len(lst) - 1
    while left <= rigt:
        for i in range(left, rigt):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        rigt -= 1
        for i in range(rigt, left, -1):
            if lst[i] > lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        left += 1
    return lst


# @profile
def bubble_sort(lst):
    i = len(lst) - 1
    while i > 0:
        for j in range(i):
            if lst[j] < lst[j + 1]:
                sorted = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        i -= 1
    return lst


# @profile
def bubble_sort_opt(lst):
    i = len(lst) - 1
    while i > 0:
        sorted = True
        for j in range(i):
            if lst[j] < lst[j + 1]:
                sorted = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if sorted is True:
            return lst
        i -= 1
    return lst


print(lst)
print(bubble_sort_opt(lst.copy()))
print(bubble_sort(lst.copy()))
print(cocktail_sort(lst.copy()))

# print(timeit.timeit("bubble_sort(lst.copy())",
#                     setup="from __main__ import bubble_sort, lst",
#                     number=100))
# print(timeit.timeit("bubble_sort_opt(lst.copy())",
#                     setup="from __main__ import bubble_sort_opt, lst",
#                     number=100))
# print(timeit.timeit("cocktail_sort(lst.copy())",
#                     setup="from __main__ import cocktail_sort, lst",
#                     number=100))
"""
Скорость алгоритма:
1.  Сортировка методем пузырька без оптимизации
    bubble_sort() - 10.493 секунды
2.  Сортировка методем пузырька с оптимизацией
    bubble_sort_opt() -  7.288 секунды
3.  Шейкерная сортировка
    cocktail_sort() - 8.292 секунды

Расходование памяти:
1.  Сортировка методем пузырька без оптимизации
    Filename: /home/alex/git-reps/algo_and_structures_python/Lesson_7/1.py
    
    Line #    Mem usage    Increment   Line Contents
    ================================================
        32     16.3 MiB     16.3 MiB   @profile
        33                             def bubble_sort(lst):
        34     16.3 MiB      0.0 MiB       i = len(lst) - 1
        35     16.3 MiB      0.0 MiB       while i > 0:
        36     16.3 MiB      0.0 MiB           for j in range(i):
        37     16.3 MiB      0.0 MiB               if lst[j] < lst[j + 1]:
        38     16.3 MiB      0.0 MiB                   sorted = False
        39     16.3 MiB      0.0 MiB                   lst[j], lst[j + 1] = lst[j + 1], lst[j]
        40     16.3 MiB      0.0 MiB           i -= 1
        41     16.3 MiB      0.0 MiB       return lst

    Использовано 16.3 мб памяти

2.  Сортировка методем пузырька с оптимизацией

    Filename: /home/alex/git-reps/algo_and_structures_python/Lesson_7/1.py
    
    Line #    Mem usage    Increment   Line Contents
    ================================================
        44     16.3 MiB     16.3 MiB   @profile
        45                             def bubble_sort_opt(lst):
        46     16.3 MiB      0.0 MiB       i = len(lst) - 1
        47     16.3 MiB      0.0 MiB       while i > 0:
        48     16.3 MiB      0.0 MiB           sorted = True
        49     16.3 MiB      0.0 MiB           for j in range(i):
        50     16.3 MiB      0.0 MiB               if lst[j] < lst[j + 1]:
        51     16.3 MiB      0.0 MiB                   sorted = False
        52     16.3 MiB      0.0 MiB                   lst[j], lst[j + 1] = lst[j + 1], lst[j]
        53     16.3 MiB      0.0 MiB           if sorted is True:
        54     16.3 MiB      0.0 MiB               return lst
        55     16.3 MiB      0.0 MiB           i -= 1
        56                                 return lst

    Использовано 16.3 мб памяти

3.  Шейкерная сортировка

    Filename: /home/alex/git-reps/algo_and_structures_python/Lesson_7/1.py

    Line #    Mem usage    Increment   Line Contents
    ================================================
        16     16.4 MiB     16.4 MiB   @profile
        17                             def cocktail_sort(lst):
        18     16.4 MiB      0.0 MiB       left = 0
        19     16.4 MiB      0.0 MiB       rigt = len(lst) - 1
        20     16.4 MiB      0.0 MiB       while left <= rigt:
        21     16.4 MiB      0.0 MiB           for i in range(left, rigt):
        22     16.4 MiB      0.0 MiB               if lst[i] > lst[i + 1]:
        23     16.4 MiB      0.0 MiB                   lst[i], lst[i + 1] = lst[i + 1], lst[i]
        24     16.4 MiB      0.0 MiB           rigt -= 1
        25     16.4 MiB      0.0 MiB           for i in range(rigt, left, -1):
        26     16.4 MiB      0.0 MiB               if lst[i] < lst[i - 1]:
        27     16.4 MiB      0.0 MiB                   lst[i], lst[i - 1] = lst[i - 1], lst[i]
        28     16.4 MiB      0.0 MiB           left += 1
        29     16.4 MiB      0.0 MiB       return lst
    
    Использовано 16.4 мб памяти

 
Вывод: 
1. По расходу памяти все реализации показали одинаковый результат(при n = 1000).
2. По времени лучший результат у алгоритма сортировка методем пузырька с
   оптимизацией.

"""