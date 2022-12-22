# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


num = input('Enter: ')
res_dict = {}

if num.isdigit():
    num = int(num)
    sum = 0
    for n in range(1, num+1):
        res = round((1+1/n)**n, 2)
        res_dict |= {n: res}
        sum += res
    print(f'For number {num} sequence created {res_dict} with sum of elements {sum}')
else:
    print('String entered try again')


