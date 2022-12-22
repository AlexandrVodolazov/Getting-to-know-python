# Реализуйте алгоритм перемешивания списка.


import random

start_list = [9,22,13,84,55]
print (f'the program shuffles the list {start_list}')
end_list = start_list
random.shuffle(end_list)
print (f'Final result {end_list}')


