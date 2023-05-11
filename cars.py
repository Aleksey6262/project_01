# Что такое класс и экземпляр?

# Класс - шаблон по которому создаются экземпляры-объекты
# Класс Машины это чертеж по которому с конвеера выходят новые машины
class Car:
    # Атрибуты класса - переменные внутри класса (свойства)
    wheels = 4
    color = 'black'

    # Методы - функции внутри класса (действия)
    def sound():
        print('Beebeeb')

    def move(self, start):
        print('Машина поехала')
        self.engine_status = True
        return self.engine_status
    
# Сами экземпляры класса
# Машины, которые живут собственной жизнью
toyota1 = Car()
toyota2 = Car()
toyota3 = Car()
toyota4 = Car()

# toyota3.move(True)

# __del__ деструктор объекта

class Truck:
    '''Самосвал загружает в ковш и выгружает из него в другом месте'''

    def __init__(self, *args):
        print('Загрузка в ковш:')
        [print(i) for i in args]

    def __del__(self):
        print('содержимое выгружено из ковша!')

van1 = Truck('песок', 'щебень', 'земля')




# int()
# new_lst = list

