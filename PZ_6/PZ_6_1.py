# Вариант 27
# Задание 1
# Дан список A размера N. Найти минимальный элемент из его элементов
# с четными номерами: A2, A4, A6, ...

import random

# Ввод размера списка N
while True:
    try:
        n = int(input("Введите размер списка N (N >= 2): "))
        if n < 2:
            print("Размер списка должен быть не менее 2!")
            continue
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

# Заполнение списка случайными числами
a = []
for _ in range(n):
    a.append(random.randint(1, 100))

print(f"Исходный список: {a}")

# Элементы с четными номерами A2, A4, A6 в Python имеют индексы 1, 3, 5...
even_pos_elements = []
for i in range(1, n, 2):
    even_pos_elements.append(a[i])

print(f"Элементы на четных позициях: {even_pos_elements}")

# Поиск минимального элемента
min_val = even_pos_elements[0]
for item in even_pos_elements:
    if item < min_val:
        min_val = item

print(f"Минимальный элемент из элементов с четными номерами: {min_val}")
