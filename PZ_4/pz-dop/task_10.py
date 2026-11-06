"""
Задание 10:
Вывести первые N (N >= 3) чисел Фибоначчи и посчитать количество четных чисел.
"""

while True:
    try:
        n = int(input("Введите число N (N >= 3): "))
        if n < 3:
            print("Ошибка! N должно быть не менее 3.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

# Первые два числа Фибоначчи
f1 = 1
f2 = 1
even_count = 0

print("Числа Фибоначчи:", f1, f2, end=" ")

# Если среди первых двух есть четные (в классическом ряду оба нечетные: 1, 1)
if f1 % 2 == 0:
    even_count += 1
if f2 % 2 == 0:
    even_count += 1

# Генерируем оставшиеся числа
for _ in range(3, n + 1):
    f_next = f1 + f2
    print(f_next, end=" ")
    if f_next % 2 == 0:
        even_count += 1
    f1 = f2
    f2 = f_next

print(f"\nКоличество четных чисел Фибоначчи: {even_count}")
