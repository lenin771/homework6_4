# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)

import random
import sympy
x = sympy.Symbol('x')
k = int(input('Введите число '))
a = 0
pol = 0
for i in range(k, -1, -1):
    a = random.randint(1,100)
    pol = pol + a*x**i
print(pol)
print(type(pol))


