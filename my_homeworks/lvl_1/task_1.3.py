# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

# Решение
user_input = input("Введите, номер месяца: ")
month = int(user_input)
total_month = [[1, 'январь'], 
               [2, 'февраль'], 
               [3, 'март'], 
               [4, 'апрель'], 
               [5, 'май'], 
               [6, 'июнь'], 
               [7, 'июль'],
               [8, 'август'], 
               [9, 'сентябрь'], 
               [10, 'октябрь'], 
               [11, 'ноябрь'], 
               [12, 'декабрь']]

for i, m in total_month:
    if month == i:
        print(f'Вы ввели {i} - это месяц {m}')

if 0 < month < 13:
    if month in (1, 3, 5, 7, 8, 10, 12):
        print('в этом месяце', 31, 'день')
    elif month in (4, 6, 9, 11):
        print('в этом месяце', 30, 'дней')
    elif month == 2:
        print('в этом месяце', 28, 'дней')
else:
    print('Такого месяца нет! Введите число от 1 до 12.')

