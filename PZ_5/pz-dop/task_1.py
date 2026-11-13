"""
Задание 1:
Даны три целых числа. Определить, у какого числа больше сумма цифр.
Вывод результата предусмотреть в основной программе.
Расчет суммы цифр оформить в функции.
"""


def sum_of_digits(n):
    """Считает сумму цифр числа."""
    # Берем модуль числа на случай отрицательных значений
    n = abs(n)
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


# Ввод трех чисел с обработкой ошибок
numbers = []
for i in range(1, 4):
    while True:
        try:
            val = int(input(f"Введите {i}-е целое число: "))
            numbers.append(val)
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

# Считаем сумму цифр для каждого числа
sums = [sum_of_digits(num) for num in numbers]

for i in range(3):
    print(f"Число: {numbers[i]}, сумма цифр: {sums[i]}")

# Поиск числа с наибольшей суммой цифр
max_sum = max(sums)
best_index = sums.index(max_sum)

print(f"\nНаибольшую сумму цифр ({max_sum}) имеет число: {numbers[best_index]}")
