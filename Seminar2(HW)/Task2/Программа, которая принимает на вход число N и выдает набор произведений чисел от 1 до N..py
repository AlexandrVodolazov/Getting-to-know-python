# Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


num = int(input('Enter number: '))

f = 1
for i in range(num):
    i = i + 1
    f = i * f

print(f, end=" ")

