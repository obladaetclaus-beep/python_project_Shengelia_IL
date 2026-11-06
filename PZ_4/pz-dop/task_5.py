"""
Задание 5:
Ввести N чисел. Найти и вывести их среднее арифметическое.
"""

while True:
    try:
        n = int(input("Введите количество чисел N: "))
        if n <= 0:
            print("Количество должно быть больше 0!")
            continue
        break
    except ValueError:
        print("Ошибка! Введите целое положительное число.")

total_sum = 0

for i in range(1, n + 1):
    while True:
        try:
            val = float(input(f"Введите {i}-е число: "))
            break
        except ValueError:
            print("Ошибка! Введите число.")
    total_sum += val

avg = total_sum / n
print(f"Среднее арифметическое {n} введенных чисел: {avg:.2f}")
