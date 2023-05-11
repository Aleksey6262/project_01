

# TODO - Модули и пакеты
# TODO - Сторонние пакеты

# import funcations as fnc  # импортируем имена модуля

import my_package.subpackage as ms  # импорт имен из __init__.py из subpackage

from my_package.module_1 import foo_1, var_1   # вызов имен модуля в пакете

# ms.foo_3()
# foo_1()
# var_1
# Перекрытие имен
# list().append(100)
# numpy.array().append(100)

# Стандартная библиотека Python
import os
# from os import getcwd
# print(os.getcwd())

from random import sample
print(sample(range(10000), k=3))  # [7366, 7953, 6808]





