"""
Задание 1:
Ввести 4 числа. Найти и вывести на экран сумму и количество отрицательных чисел.
"""

neg_sum = 0
neg_count = 0

# Вводим 4 числа по очереди
for i in range(1, 5):
    while True:
        try:
            num = float(input(f"Введите {i}-е число: "))
            break
        except ValueError:
            print("Ошибка! Введите число.")

    # Если число меньше нуля, учитываем его
    if num < 0:
        neg_sum += num
        neg_count += 1

print(f"Количество отрицательных чисел: {neg_count}")
print(f"Сумма отрицательных чисел: {neg_sum}")
