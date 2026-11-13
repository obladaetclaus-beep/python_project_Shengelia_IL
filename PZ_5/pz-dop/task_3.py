"""
Задание 3:
Написать программу, подсчитывающую количество цифр числа,
используя для этого функцию.
"""


def count_digits(n):
    """Подсчитывает количество цифр в целом числе."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


# Ввод числа
while True:
    try:
        num = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

# Вызов функции и вывод результата
result = count_digits(num)
print(f"В числе {num} содержится цифр: {result}")
