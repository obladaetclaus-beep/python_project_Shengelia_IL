# Вариант 27
# Дано множество A из N точек (N > 2, точки заданы своими координатами x, y).Найти наибольший периметр треугольника, вершины которого принадлежат различным точкам множества A, и сами эти точки (в исходном порядке). Использовать по два списка: для абсцисс и для ординат.

import math
import random

n = int(input("Введите количество точек N (N >= 3): "))

x_coords = [random.randint(-15, 15) for _ in range(n)]
y_coords = [random.randint(-15, 15) for _ in range(n)]

print("Исходные точки множества A:")
for i in range(n):
    print(f"Точка {i + 1}: ({x_coords[i]}, {y_coords[i]})")

def get_distance(i, j):
    return math.sqrt((x_coords[j] - x_coords[i])**2 + (y_coords[j] - y_coords[i])**2)

max_perimeter = 0
best = (0, 1, 2)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            p = get_distance(i, j) + get_distance(j, k) + get_distance(k, i)
            if p > max_perimeter:
                max_perimeter = p
                best = (i, j, k)

print(f"\nНаибольший периметр: {max_perimeter:.4f}")
print("Вершины треугольника (в порядке исходного списка):")
print(f"1) Точка {best[0] + 1}: ({x_coords[best[0]]}, {y_coords[best[0]]})")
print(f"2) Точка {best[1] + 1}: ({x_coords[best[1]]}, {y_coords[best[1]]})")
print(f"3) Точка {best[2] + 1}: ({x_coords[best[2]]}, {y_coords[best[2]]})")
