# Вариант 27
# Задание 3
# Дано множество A из N точек (N > 2, точки заданы своими координатами x, y).
# Найти наибольший периметр треугольника, вершины которого принадлежат
# различным точкам множества A, и сами эти точки (в исходном порядке).
# Использовать по два списка: для абсцисс и для ординат.

import math
import random

# Ввод количества точек N
while True:
    try:
        n = int(input("Введите количество точек N (N >= 3): "))
        if n < 3:
            print("Для построения треугольника нужно минимум 3 точки!")
            continue
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

# Списки для координат X и Y
x_coords = []
y_coords = []

for _ in range(n):
    x_coords.append(random.randint(-15, 15))
    y_coords.append(random.randint(-15, 15))

print("Исходные точки множества A:")
for i in range(n):
    print(f"  Точка {i + 1}: ({x_coords[i]}, {y_coords[i]})")


# Функция вычисления расстояния между двумя точками по формуле из задания
def get_distance(i, j):
    dx = x_coords[j] - x_coords[i]
    dy = y_coords[j] - y_coords[i]
    return math.sqrt(dx ** 2 + dy ** 2)


max_perimeter = 0.0
best_indices = (0, 1, 2)

# Перебираем все возможные комбинации из трех разных точек
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            side1 = get_distance(i, j)
            side2 = get_distance(j, k)
            side3 = get_distance(k, i)
            perimeter = side1 + side2 + side3

            if perimeter > max_perimeter:
                max_perimeter = perimeter
                best_indices = (i, j, k)

idx1, idx2, idx3 = best_indices

# Вывод результатов
print("\n--- Результаты ---")
print(f"Наибольший периметр треугольника: {max_perimeter:.4f}")
print("Вершины треугольника в порядке их перечисления при задании множества A:")
print(f"1) Точка {idx1 + 1}: ({x_coords[idx1]}, {y_coords[idx1]})")
print(f"2) Точка {idx2 + 1}: ({x_coords[idx2]}, {y_coords[idx2]})")
print(f"3) Точка {idx3 + 1}: ({x_coords[idx3]}, {y_coords[idx3]})")
