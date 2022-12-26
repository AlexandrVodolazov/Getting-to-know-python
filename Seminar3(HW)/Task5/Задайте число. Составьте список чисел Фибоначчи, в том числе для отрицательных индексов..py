# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# n = int(input('Введите размер числа Фибоначчи '))
# if n < 0: n = n*-1
# f1 = f2 = 1
# list1 = [f1, f2]
# for i in range(2, n):
#     f1,f2 = f2, f1 + f2
#     list1.append(f2)
# print(list1)
# f1=f2=1
# for i in range(-n, 1):
#     f1,f2 = f2, f1 - f2
#     list1.insert(0, f2)
# print(list1)


#РАБОТАЕЕЕЕТ!!!

fib = int(input('5# введите число for fib = '))
res_5 = []
for i in range(fib+1):
    if i==0:
        res_5.append(i)
    elif i==1:
        res_5.append(i)
        res_5.insert(0, i)
    else:
        res_5.append(res_5[len(res_5)-1]+res_5[len(res_5)-2])
        res_5.insert(0, (-1)**(i-1)*res_5[len(res_5)-1])
print(res_5)