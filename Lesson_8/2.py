"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib

def counter(s):
    length = len(s)
    sub = set()
    for i in range(length):
        for j in range(length+1):
            if i == 0 and j == length:
                continue
            elif i < j:
                sub.add(hashlib.md5(s[i:j].encode('utf-8')).hexdigest())
    return sub

s = input("Введите строку, состоящую только из маленьких латинских букв:")

sub = counter(s)

print(f"Количество подстрок: {len(sub)}")

for i,j in enumerate(sub,1):
    print(f'{i}.\t {j}')

