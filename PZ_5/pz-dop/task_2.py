"""
Задание 2:
Рассчитать и вывести периметр и площадь прямоугольника.
Расчеты оформить в функции.
"""


def calc_rectangle(a, b):
    """Вычисляет периметр и площадь прямоугольника."""
    perimeter = 2 * (a + b)
    area = a * b
    return perimeter, area


# Ввод сторон прямоугольника
while True:
    try:
        side_a = float(input("Введите длину стороны a: "))
        side_b = float(input("Введите длину стороны b: "))
        if side_a <= 0 or side_b <= 0:
            print("Стороны прямоугольника должны быть положительными числами!")
            continue
        break
    except ValueError:
        print("Ошибка! Введите числовые значения.")

# Вызов функции
p, s = calc_rectangle(side_a, side_b)

print(f"Периметр прямоугольника: {p}")
print(f"Площадь прямоугольника: {s}")
