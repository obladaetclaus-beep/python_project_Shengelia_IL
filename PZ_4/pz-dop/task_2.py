"""
Задание 2:
Ввести 4 числа. Найти и вывести на экран количество четных чисел.
"""

even_count = 0

for i in range(1, 5):
    while True:
        try:
            num = int(input(f"Введите {i}-е целое число: "))
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    # Проверяем на четность
    if num % 2 == 0:
        even_count += 1

print(f"Количество четных чисел: {even_count}")
