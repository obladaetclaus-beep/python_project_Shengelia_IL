"""
Задание 4:
Найти и вывести на экран S = 1! + 2! + 3! + 4! + … + n! (n > 1).
"""

while True:
    try:
        n = int(input("Введите число n (> 1): "))
        if n <= 1:
            print("Число должно быть строго больше 1!")
            continue
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

total_sum = 0
factorial = 1

# На каждом шаге домножаем факториал и добавляем в общую сумму
for i in range(1, n + 1):
    factorial *= i
    total_sum += factorial

print(f"Сумма факториалов S = {total_sum}")
