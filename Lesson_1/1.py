# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input("Введите трех значное число: "))

number_0 = number // 100
number_2 = number % 10
number_1 = (number - number_2 - number_0 * 100) / 10
number_4 = number_0 * number_1 * number_2
number_5 = number_0 + number_1 + number_2

print(f"Произведение цифр трех значного числа {number} равна: {number_4}")
print(f"Сумма цифр трех значного числа {number} равна: {number_5}")
