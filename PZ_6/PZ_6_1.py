# Вариант 27
# Задание 1
# Дан список A размера N. Найти минимальный элемент из его элементов с четными номерами: A2, A4, A6, ...

import random

while True:
    try:
        n = int(input("Введите размер списка N (N >= 2): "))
        if n >= 2:
            break
        else:
            print("Размер списка должен быть не менее 2!")
    except ValueError:
        print("Ошибка! Введите целое число.")

a = [random.randint(1, 100) for _ in range(n)]
print(f"Исходный список: {a}")

even_pos_elements = a[1::2]
print(f"Элементы на четных позициях: {even_pos_elements}")

min_val = min(even_pos_elements)
print(f"Минимальный элемент из элементов с четными номерами: {min_val}")
