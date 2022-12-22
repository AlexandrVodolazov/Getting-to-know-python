# Программа, которая принимает на вход вещественное число и показывает сумму его цифр.



num = int(input('Enter number N: '))
sum_num = 0
while num != int(num):
    num *= 10

while num > 0:
    sum_num += num % 10
    num //= 10
print(sum_num)



# num = input('Enter number N: ')
# sum = 0
# for ch in num:
#     if ch.isdigit():
#         sum += int(ch)
# print(f'Сумма цифр в числе {num} составляет {sum}')


