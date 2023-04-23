# TODO - if-elif-else
# TODO - while
# TODO - for
# TODO - лаконичная запись


# условный оператор if
# Задача 2
# Создайте список списков населения перечисленных городов

population = [
    ['Москва', 58321512],
    ['Новгород', 891242],
    ['Владимир', 124853],
]

# # print(population[0][0])

# if population[0][0] == 'Москва' and 0:
#     print(f'Найдено население города {population[0][0]}')

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек


# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Цикл for - работает с элементами списка

# Вариант 1
# tolal_population = 0

# for i in population:
#     # tolal_population = tolal_population + i
#     tolal_population += i[1]

# print(f'Итого размер населения - {tolal_population} человек')

# Вариант 2
# tolal_population = 0
# for city, people in population:
#     # print(f'Население города {city} - {people} человек')
#     tolal_population += people

# print(f'Итого размер населения - {tolal_population} человек')

# Вариант 3 - списковое включение
# Что такое однострочник?
for i in [1, 2, 3, 4,]:
    print(i ** 2)

print(
    [i ** 2 for i in [1, 2, 3, 4,]]
    )
# вариант 1 в одну строчку:
# print(f'Итого размер населения - {sum([i[1] for i in population])} человек')


# Итого размер населения - ХХ человек

# lst = [1, 2, 3, 4, 5]
# for i in lst:
#     i = i * 2
#     print(i)





