# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N

number=int(input("Введите число: "))
factor = []
ind = []
for i in range(2, number+1):
    if(number%i==0):
        factor.append(i)

for i in range(len(factor)-1, 0, -1):
    for j in range(i):
        
        if factor[i] % factor[j] == 0:
            ind.append(factor[i])
            break

for i in range(len(ind)):
    factor.remove(ind[i])
print(f'список простых множителей числа {number} = {factor}')