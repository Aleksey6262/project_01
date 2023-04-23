
# TODO - лаконичная запись
# TODO - словари
# Список списков
# population = [
#     ['Москва', 58321512],
#     ['Новгород', 891242],
#     ['Владимир', 124853],
# ]

# Словарь - набор комбинаций "ключ" - "значение"
# Словарь это изменяемый объект
# lst = []
# tpl = ()
# dct = {}

# capitals = {
#     'Россия': 'Москва',
#     'Италия': 'Рим'
#     }

# capitals['Франция'] = 'Париж'
# print(capitals)


# Пример применения словарей
# pd.DataFrame({'a': [1, 2, 3, 4,]})

# Задача
population = {
    'Москва': 58321512,
    'Новгород': 891242,
    'Владимир': 124853,
}

total_population = sum((population[city] for city in population))
print(total_population)

for city, people in population.items():
    print(city, people)

# population.keys()
# population.values()
# population.items()
