# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

ax, ay = input("Введите координаты точки А через пробел: ").split()
bx, by = input("Введите координаты точки B через пробел: ").split()

A = int(ay) - int(by)
B = int(bx) - int(ax)
C = int(ax) * int(by) - int(bx) * int(ay)

if ax == bx and ay == by:
    print("Координаты точек равны")
else:
    if B < 0:
        B = f" - {abs(B)}y"
    else:
        B = f" + {abs(B)}y"
    if A < 0:
        A = f" - {abs(A)}x"
    else:
        A = f"{abs(A)}x"
    if C == 0:
        C = ''
    elif C < 0:
        C = f" - {abs(C)}"
    else:
        C = f" + {abs(C)}"
    print(f"Уравнение прямой: {A}{B}{C}")
