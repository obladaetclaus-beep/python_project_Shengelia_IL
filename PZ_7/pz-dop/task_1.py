"""
Дополнительное задание:
Дан список размера N, состоящий из символов. Привести символы букв
из верхнего регистра в нижний. Определить количество букв.
"""

import random

while True:
    try:
        n = int(input("Введите размер массива символов N: "))
        if n <= 0:
            print("Размер должен быть больше 0!")
            continue
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

# Заполняем список случайными символами (латиница, цифры, знаки)
symbols = []
for _ in range(n):
    # ASCII коды от 45 до 100 включают цифры, знаки и заглавные/строчные буквы
    symbols.append(chr(random.randint(45, 100)))

print(f"Исходный список символов: {symbols}")

# Подсчет количества букв
letter_count = 0
for ch in symbols:
    if ch.isalpha():
        letter_count += 1

print(f"Количество букв в списке: {letter_count}")

# Объединяем список в строку и переводим в нижний регистр
original_string = "".join(symbols)
lower_string = original_string.lower()

print(f"Исходная строка:          '{original_string}'")
print(f"Строка в нижнем регистре: '{lower_string}'")
