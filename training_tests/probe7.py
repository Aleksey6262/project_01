
# TODO - Функции, параметры
# TODO - Модули и пакеты
# TODO - Сторонние пакеты
# Функция - блок кода, принимающие некие значения и возвращающий обработанные значения
# Принцип DRY - Dont reapit

# Создание функции
# def greeting(name):
#     return f'Привет, {name}'

# # Вызов функции
# for _ in ['Никита', 'Маша', 'Саша']:
#     print(greeting(_) + 'Как дела?')

# len(lst) -> int
# multi(x, y) -> res
# multi(x, y) -> res

# Задача 1
# Проверьте, содержит ли строка одинаковое количество "x" и "o".
# Строка должна быть нечувствительна к регистру. 
# Строка может содержать любые символы.
 
# Примеры ввода/вывода:
#   XO("ooxx") => true
#   XO("xooxx") => false
#   XO("ooxXm") => true
#   XO("zpzpzpp") => true # когда нет "x" и "o", должно быть возвращено значение true
#   XO("zzoo") => false

# string = "zpzpzpp"


# def check_xo(string):
#     counter_x = 0
#     counter_o = 0
#     for i in string.lower():
#         if i == 'o':
#             counter_o += 1
#         elif i == 'x':
#             counter_x += 1

#     return counter_x == counter_o

# for i in ["ooxx", "xooxx", "ooxXm", "zpzpzpp", "zzoo"]:
#     print(check_xo(i))


# Задача 2
# Посчитайте количество нечетных чисел в заданном числе n
# Задача 2
# Посчитайте количество нечетных чисел в заданном числе n
# 7 [1, 3, 5] -> 3
# 15 [1, 3, 5, 7, 9, 11, 13] -> 7
 
def odd_count(n):
    return n // 2
 
print(odd_count(10000))


# Организация файла
# 1. Глобальные переменные (если ооочень надо)
base_ur1 = 'https:'

# Создание функции
# def greeting(name):
#     return f'Привет, {name}'





    







   

