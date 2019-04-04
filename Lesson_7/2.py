"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random
import timeit
from memory_profiler import profile

lst = [random.randint(0, 50) for _ in range(30)]

# lst = [3, 12, 7, 47, 3, 22, 36, 16, 29, 0, 13, 38, 23, 22, 41, 6, 25, 2, 4, 33,
#        22, 32, 10, 20, 16, 35, 29, 12, 47, 36, 2, 11, 21, 33, 35, 40, 15, 3, 39,
#        10, 12, 24, 25, 17, 12, 19, 43, 19, 25, 45, 18, 16, 10, 6, 21, 1, 22, 1,
#        17, 35, 20, 35, 47, 29, 25, 21, 17, 43, 21, 50, 48, 33, 7, 18, 28, 39,
#        16, 5, 25, 9, 13, 46, 8, 33, 35, 19, 14, 1, 7, 2, 5, 45, 45, 27, 40, 1,
#        24, 42, 6, 6, 37, 13, 23, 20, 4, 3, 15, 31, 0, 43, 15, 17, 1, 25, 15, 6,
#        28, 44, 28, 37, 2, 30, 12, 2, 23, 39, 48, 46, 41, 39, 26, 34, 3, 5, 16,
#        34, 5, 34, 22, 37, 20, 1, 23, 8, 45, 8, 2, 18, 29, 2, 7, 46, 24, 3, 48,
#        22, 46, 5, 18, 30, 24, 47, 10, 2, 13, 34, 25, 8, 44, 10, 4, 35, 30, 11,
#        44, 20, 45, 26, 34, 0, 27, 50, 28, 18, 36, 37, 23, 40, 37, 6, 7, 28, 30,
#        48, 47, 21, 32, 37, 8, 16, 9, 16, 4, 25, 9, 24, 5, 28, 35, 1, 43, 7, 4,
#        28, 9, 13, 13, 14, 5, 14, 49, 37, 15, 42, 22, 6, 25, 38, 48, 33, 24, 21,
#        22, 30, 21, 10, 16, 39, 24, 0, 34, 1, 39, 3, 10, 49, 18, 18, 21, 4, 45,
#        39, 27, 17, 1, 43, 24, 7, 7, 21, 21, 13, 4, 12, 8, 28, 2, 12, 47, 23, 7,
#        31, 28, 41, 18, 42, 32, 25, 50, 15, 4, 43, 31, 11, 37, 21, 40, 13, 50,
#        17, 26, 31, 10, 35, 42, 46, 2, 15, 9, 3, 17, 25, 27, 47, 11, 3, 7, 9, 37,
#        38, 21, 20, 23, 34, 42, 22, 1, 8, 15, 1, 47, 44, 18, 37, 15, 24, 40, 5,
#        4, 7, 45, 49, 27, 25, 11, 40, 40, 50, 7, 31, 49, 16, 39, 41, 45, 29, 35,
#        30, 28, 29, 24, 41, 19, 50, 27, 0, 34, 50, 7, 0, 37, 17, 41, 41, 23, 27,
#        1, 7, 0, 36, 13, 21, 23, 18, 42, 33, 15, 2, 50, 27, 17, 10, 8, 43, 26,
#        40, 45, 38, 17, 49, 27, 13, 19, 33, 44, 40, 8, 44, 24, 12, 32, 47, 19,
#        37, 16, 13, 41, 3, 10, 22, 7, 45, 46, 22, 31, 38, 24, 17, 44, 11, 17, 6,
#        5, 24, 8, 31, 29, 34, 38, 15, 30, 49, 13, 25, 28, 20, 46, 39, 41, 12, 4,
#        33, 30, 46, 6, 31, 46, 30, 7, 10, 22, 31, 25, 11, 23, 13, 46, 28, 36, 28,
#        19, 25, 14, 23, 13, 9, 21, 11, 23, 5, 33, 50, 19, 39, 13, 32, 33, 34, 44,
#        27, 21, 40, 11, 39, 19, 12, 16, 21, 3, 29, 12, 35, 13, 22, 18, 26, 50,
#        40, 37, 17]


print(lst)


# @profile
def cocktail_sort(lst):
    left = 0
    rigt = len(lst) - 1
    while left <= rigt:
        for i in range(left, rigt):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        rigt -= 1
        for i in range(rigt, left, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        left += 1
    return lst


# @profile
def bubble_sort(lst):
    i = len(lst) - 1
    while i > 0:
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        i -= 1
    return lst


# @profile
def bubble_sort_opt(lst):
    i = len(lst) - 1
    while i > 0:
        sorted = True
        for j in range(i):
            if lst[j] > lst[j + 1]:
                sorted = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if sorted is True:
            return lst
        i -= 1
    return lst


# @profile
def merge(left, right):
    lst = []
    n_left = 0
    n_right = 0
    while n_left < len(left) and n_right < len(right):
        if left[n_left] < right[n_right]:
            lst.append(left[n_left])
            n_left += 1
        else:
            lst.append(right[n_right])
            n_right += 1
    return lst + left[n_left:] + right[n_right:]


# @profile
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        left = lst[:len(lst) // 2]
        right = lst[len(lst) // 2:]
        return merge(merge_sort(left), merge_sort(right))


print(merge_sort(lst.copy()))
# print(cocktail_sort(lst.copy()))
# print(bubble_sort(lst.copy()))
# print(bubble_sort_opt(lst.copy()))

# print(timeit.timeit("merge_sort(lst.copy())",
#                     setup="from __main__ import merge_sort, lst",
#                     number=100))
# print(timeit.timeit("cocktail_sort(lst.copy())",
#                     setup="from __main__ import cocktail_sort, lst",
#                     number=100))
# print(timeit.timeit("bubble_sort(lst.copy())",
#                     setup="from __main__ import bubble_sort, lst",
#                     number=100))
# print(timeit.timeit("bubble_sort_opt(lst.copy())",
#                     setup="from __main__ import bubble_sort_opt, lst",
#                     number=100))

"""
Скорость алгоритма:
1.  Сортировка слиянием:
    merge_sort() - 0.186 секунды

2.  Шейкерная сортировка
    cocktail_sort() - 2.068 секунды

3.  Сортировка методем пузырька без оптимизации
    bubble_sort() - 2.149 секунды

4.  Сортировка методем пузырька c оптимизацией
    bubble_sort_opt() - 1.859 секунды


Расходование памяти:
1.  Сортировка слиянием:
    Line #    Mem usage    Increment   Line Contents
    ================================================
        57     16.2 MiB     16.2 MiB   @profile
        58                             def merge(left, right):
        59     16.2 MiB      0.0 MiB       lst = []
        60     16.2 MiB      0.0 MiB       n_left = 0
        61     16.2 MiB      0.0 MiB       n_right = 0
        62     16.2 MiB      0.0 MiB       while n_left < len(left) and n_right < len(right):
        63     16.2 MiB      0.0 MiB           if left[n_left] < right[n_right]:
        64     16.2 MiB      0.0 MiB               lst.append(left[n_left])
        65     16.2 MiB      0.0 MiB               n_left += 1
        66                                     else:
        67     16.2 MiB      0.0 MiB               lst.append(right[n_right])
        68     16.2 MiB      0.0 MiB               n_right += 1
        69     16.2 MiB      0.0 MiB       return lst + left[n_left:] + right[n_right:]
    
    
    Filename: /home/alex/git-reps/algo_and_structures_python/Lesson_7/2.py
    
    Line #    Mem usage    Increment   Line Contents
    ================================================
        72     16.2 MiB     16.2 MiB   @profile
        73                             def merge_sort(lst):
        74     16.2 MiB      0.0 MiB       if len(lst) <= 1:
        75     16.2 MiB      0.0 MiB           return lst
        76                                 else:
        77     16.2 MiB      0.0 MiB           left = lst[:len(lst) // 2]
        78     16.2 MiB      0.0 MiB           right = lst[len(lst) // 2:]
        79     16.2 MiB      0.0 MiB           return merge(merge_sort(left), merge_sort(right))
        

2.  Шейкерная сортировка
    Filename: /home/alex/git-reps/algo_and_structures_python/Lesson_7/2.py

    Line #    Mem usage    Increment   Line Contents
    ================================================
        44     16.3 MiB     16.3 MiB   @profile
        45                             def cocktail_sort(lst):
        46     16.3 MiB      0.0 MiB       left = 0
        47     16.3 MiB      0.0 MiB       rigt = len(lst) - 1
        48     16.3 MiB      0.0 MiB       while left <= rigt:
        49     16.3 MiB      0.0 MiB           for i in range(left, rigt):
        50     16.3 MiB      0.0 MiB               if lst[i] > lst[i + 1]:
        51     16.3 MiB      0.0 MiB                   lst[i], lst[i + 1] = lst[i + 1], lst[i]
        52     16.3 MiB      0.0 MiB           rigt -= 1
        53     16.3 MiB      0.0 MiB           for i in range(rigt, left, -1):
        54     16.3 MiB      0.0 MiB               if lst[i] < lst[i - 1]:
        55     16.3 MiB      0.0 MiB                   lst[i], lst[i - 1] = lst[i - 1], lst[i]
        56     16.3 MiB      0.0 MiB           left += 1
        57     16.3 MiB      0.0 MiB       return lst
        
3.  Сортировка методем пузырька без оптимизации

    Filename: /home/alex/git-reps/algo_and_structures_python/Lesson_7/2.py

    Line #    Mem usage    Increment   Line Contents
    ================================================
        60     16.3 MiB     16.3 MiB   @profile
        61                             def bubble_sort(lst):
        62     16.3 MiB      0.0 MiB       i = len(lst) - 1
        63     16.3 MiB      0.0 MiB       while i > 0:
        64     16.3 MiB      0.0 MiB           for j in range(i):
        65     16.3 MiB      0.0 MiB               if lst[j] > lst[j + 1]:
        66     16.3 MiB      0.0 MiB                   lst[j], lst[j + 1] = lst[j + 1], lst[j]
        67     16.3 MiB      0.0 MiB           i -= 1
        68     16.3 MiB      0.0 MiB       return lst

4.  Сортировка методем пузырька c оптимизацией

    Filename: /home/alex/git-reps/algo_and_structures_python/Lesson_7/2.py

    Line #    Mem usage    Increment   Line Contents
    ================================================
        71     16.2 MiB     16.2 MiB   @profile
        72                             def bubble_sort_opt(lst):
        73     16.2 MiB      0.0 MiB       i = len(lst) - 1
        74     16.2 MiB      0.0 MiB       while i > 0:
        75     16.2 MiB      0.0 MiB           sorted = True
        76     16.2 MiB      0.0 MiB           for j in range(i):
        77     16.2 MiB      0.0 MiB               if lst[j] > lst[j + 1]:
        78     16.2 MiB      0.0 MiB                   sorted = False
        79     16.2 MiB      0.0 MiB                   lst[j], lst[j + 1] = lst[j + 1], lst[j]
        80     16.2 MiB      0.0 MiB           if sorted is True:
        81     16.2 MiB      0.0 MiB               return lst
        82     16.2 MiB      0.0 MiB           i -= 1
        83                                 return lst

Вывод: 
1.  По расходу памяти все реализации показали одинаковый результат(при n = 500).
2.  По времени лучший результат у алгоритма сортировка методем слияния.

"""