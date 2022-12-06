# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности

list1 = [10, 22, 12, 11, 10, 25, 15, 12]
list2 = []
print(f'исходный список {list1}')
for i in range(len(list1)):
    for j in range(i):
        if list1[i] == list1[j]:
            list2.append(list1[j])
for i in range(len(list2)):
    list1.remove(list2[i])
print(f'список неповторяющихся элементов {list1}')
