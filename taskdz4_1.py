# Вычислить число Пи c заданной точностью d

import math
d = float(input('Введите число '))
num = str(d).split('.')

if len(num[1]) < 2:
    print(f'Число π = {round(math.pi, 2)}')  # стандартное значение π = 3.14
else:
    print(f'Вывод числа π с точностью {d}, π = {round(math.pi, len(num[1]))}')