# Императивном стиле - написание инструкций для интерпретатора
# Объектно-ориентированное програмирование -концепция, 
# в которой программист создает объекты и задает правила их взаимодействия.

# как создать класс?
# НАЗВАНИЯ КЛАССОВ
# переменные - Shop_list, cost_function
# функция - get_value()
# классы - Person, MyFavoritePage

# Этап создания класса

class Cell:
    '''ячейка таблицы'''
    # атрибуты
    content_type = int()
    content = 1

    # Методы
    # связанный метод (bound method)- это метод с указанием параметра self (указание на имя экз.)
    def set_value(self, val):
        self.content = val
        self.content_type = type(val)
        

# Этап Создания экземпляра класса
a1 = Cell()
print(a1.content)
a1.set_value(100)
print(a1.content)


# ДЗ. 3.1

# m1 = Matrix(5, 10)

# 1 2 3 4
# 1 2 3 
# None None
# None None

# class Matrix:
#     np.array()


# Магические (специальные) методы класса?
# __init__, __eq__, __hash__



