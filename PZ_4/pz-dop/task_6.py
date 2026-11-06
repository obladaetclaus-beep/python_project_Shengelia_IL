"""
Задание 6:
Ввести N чисел. Посчитать и вывести количество чисел, равных нулю.
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

zero_count = 0

for i in range(1, n + 1):
    while True:
        try:
            val = float(input(f"Введите {i}-е число: "))
            break
        except ValueError:
            print("Ошибка! Введите число.")
    if val == 0:
        zero_count += 1

print(f"Количество чисел, равных нулю: {zero_count}")
