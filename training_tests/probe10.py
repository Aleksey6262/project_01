

# TODO - Модули и пакеты
# TODO - Сторонние пакеты

import funcation as fnc  # модуль

import my_package.subpackage as ms  # __init__.py из subpackage

from my_package.module_1 import foo_1, var_1   # ввод имен модуля в пакете



# Стандартная библиотека Python
import os
print(os.getcwd())

from random import sample
print(sample(range(10000), k=3))  # [7366, 7953, 6808]


ms.foo_3()
foo_1()
var_1

# Перекрытие имен
# list().append(100)
# numpy.array().append(100)

# 
