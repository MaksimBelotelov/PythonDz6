# Задача 30 : Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с
# клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

difference = int(input('Введите разность арифметической прогрессии: '))
amount = int(input('Введите количество элементов арифметической прогрессии: '))
first = int(input('Введите первый элемент арифметической прогрессии: '))

arr1 = [member for member in range(
    first, first + amount * difference, difference)]

print(arr1)
