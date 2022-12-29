# Вычислить число c заданной точностью d

# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import *
import math

accuracy_value = input('Введите интересуемую точность для числа π в формате 0.001: ')
getcontext().prec = len(accuracy_value.split('.')[1]) + 1
pi_version = Decimal(math.pi) + Decimal('0.0')
print (pi_version)