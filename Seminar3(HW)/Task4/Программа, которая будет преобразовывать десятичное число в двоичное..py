# Программа, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def get_binary(int_num):
    result = ''
    while int_num // 2 > 0:
        result += str(int_num % 2)
        int_num = int_num // 2
    result += str(int_num % 2)
    return result[::-1]


num = int(input('Введите целое число: '))
result = get_binary(num)
print(result)