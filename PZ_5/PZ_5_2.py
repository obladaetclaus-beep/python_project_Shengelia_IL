# Вариант 27
# Описать функцию AddRightDigit(D, K), добавляющую к целому положительному числу K. справа цифру D (D — диапазон 0-9, K — параметр целого типа). С помощью этой функции последовательно добавить к числу K цифры D1 и D2,выводя результат каждого добавления.

def add_right_digit(d, k):
    return k * 10 + d
def get_input(text, min_val, max_val):
    while True:
        try:
            val = int(input(text))
            if min_val <= val <= max_val:
                return val
            print(f"Ошибка. Число должно быть от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка. Введи целое число.")
k = get_input("Введи целое положительное число K: ", 1, float('inf'))
d1 = get_input("Введи цифру D1 (от 0 до 9): ", 0, 9)
d2 = get_input("Введи цифру D2 (от 0 до 9): ", 0, 9)
k = add_right_digit(d1, k)
print(f"После добавления цифры {d1} справа: {k}")
k = add_right_digit(d2, k)
print(f"После добавления цифры {d2} справа: {k}")
