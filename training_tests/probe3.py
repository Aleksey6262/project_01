
# TODO - while
# TODO - лаконичная запись

# Цикл while
i = 0
while i < 10:
    i += 1
    if i ==5:
        continue
    print('i=', i)

# Задачка: даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ
a, b = 1000, 453

i = a
divide = 0
while i > b:

    i -= b
    divide += 1
    # i = i - b
print(f'Целочисленное деление {a} на {b} дает {divide}')

# print(a // b)

