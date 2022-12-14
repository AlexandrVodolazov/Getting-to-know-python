# Программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

day = int(input("Enter day of the week: "))

if day in range(1, 6):
    print("it's a work day")

if day in range(6, 8):
    print("it's a holiday")

if day < 1 or day > 7:
    print("Try again!!!")

    


    