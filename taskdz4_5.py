# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
# В file1.txt : 2*x**2 + 4*x + 5
# В file2.txt: 4*x**2 + 1*x + 4
# Результирующий файл: 6*x**2 + 5*x + 9

import sympy
x = sympy.symbols('x')
with open("file1.txt", "r") as file:
    pol1 = sympy.sympify(file.readline())
with open("file2.txt", "r") as file:
    pol2 = sympy.sympify(file.readline())

print(type(pol1))  # Для контроля
print(type(pol2))  # Для контроля
print(pol1)     # Для контроля
print(pol2)     # Для контроля
print(sympy.simplify(pol1 + pol2))      # Для контроля

with open("file3.txt", "w") as file:
    file.write(str(sympy.simplify(pol1 + pol2)))
    file.close()

