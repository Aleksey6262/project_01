
# TODO - Функции, параметры
# TODO - Модули и пакеты
# TODO - Сторонние пакеты


# Параметры
# def trapezoid_s(a: int, b: int, h: int) -> float:
#     '''Функция для расчета площади трапеции. 
#     a - нижнее основание, 
#     b - верхнее основание, 
#     h - высота.'''
 
#     return h * (a+b) / 2
 
# S = trapezoid_s(8, 4, 10)
# S = trapezoid_s(8, h=10, b=4)
# S = trapezoid_s(8, b=4)
# print(S)
 
# Как работает функция print?
# print(1, 2, 3, 4,'vcdaf', '4215', [1, 2], sep='\n', end=' ')
 
def print_them_all(*args, **kwargs):
    print('print_them_all')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
 
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)
 
print_them_all(1, 2, 3, 4, ',dcw', 'a', a=124, b=4214)

# def func(a, b=[]):
#     pass

# func(20)

# pandas.read_csv(PATH, index_col=['a'])





    







   

