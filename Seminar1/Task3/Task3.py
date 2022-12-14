# Программа, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3


num_x = int(input("Enter number coordinates x: "))
num_y = int(input("Enter number coordinates y: "))

if num_x > 0 and num_y > 0:
    print("Сoordinate № 1")

if num_x < 0 and num_y > 0:
    print("Сoordinate № 2")

if num_x < 0 and num_y < 0:
    print("Сoordinate № 3")

if num_x > 0 and num_y < 0:
    print("Сoordinate № 4")

if num_x == 0 or num_y == 0:
    print("Сoordinate cannot = 0! Try again!")


