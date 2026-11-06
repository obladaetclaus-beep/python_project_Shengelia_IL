"""
Задание 8:
Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
включительно (использовать оператор цикла).
"""

while True:
    try:
        a = int(input("Введите число A: "))
        b = int(input("Введите число B (B > A): "))
        if a >= b:
            print("Ошибка! Число A должно быть меньше B.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите целые числа.")

total_sum = 0
current = a

while current <= b:
    total_sum += current
    current += 1

print(f"Сумма всех чисел от {a} до {b} включительно: {total_sum}")
