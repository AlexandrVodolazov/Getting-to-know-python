# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


num = input('Enter number N: ')
if num.isdigit():
    num = int(num)
    res_list =  list(range(-num, num+1))
    print(f'List for number {num} equals {res_list}')
    multiply = 1
    multiply_list = []
    file_obj = open("file.txt")
    file_lines = file_obj.readlines()
    for line in file_lines:
        line = line.rstrip('\n')
        if line.isdigit():
            temp = int(line)
            multiply_list.append(temp)
            if temp < len(res_list):
                multiply *= res_list[temp-1]
    file_obj.close()
    print(f'Product of list elements under numbers {multiply_list} равно {multiply}, where 1 corresponds to the null element')
else:
    print('Try again')

