"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

maximum = ''
max_sum = 0

while True:
    n = input("Введите число (Для выхода оставьте поле пустым): ")
    if n == "":
        if maximum == '':
            break
        else:
            print(f"Максимальное число по сумме цифр: {maximum}\n"
                  f"Сумма чисел равна: {max_sum}")
            break
    n = int(n)
    i = n
    tmp_sum = 0
    while True:
        if i == 0:
            break
        tmp_sum += i % 10
        i //= 10
    if tmp_sum > max_sum:
        max_sum = tmp_sum
        maximum = n
