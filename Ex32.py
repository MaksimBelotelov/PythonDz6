# Задача 32: Определить индексы элементов массива (списка), значения
# которых принадлежат заданному диапазону (т.е. не меньше заданного
# минимума и не больше заданного максимума).

from random import randint

size = int(input('Введите размерность массива: '))
arr1 = [randint(1, 10) for i in range(size)]

minValue = int(input('Введите нижнюю границу диапазона: '))
maxValue = int(input('Введите верхнюю границу диапазона: '))

print(arr1)

print(f'Элементы, лежащие в диапазоне [{minValue}, {maxValue}]: ')
for i in range(size):
    if (minValue <= arr1[i] <= maxValue):
        print(f'Индекс {i} : array[{i}] = {arr1[i]}')
