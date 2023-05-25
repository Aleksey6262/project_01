
# Наследование

class User:
    '''Модель пользователя'''
    gid = 1000
    active = True
    __token = 'very_secret_key'

    def __init__(self, name=None):
       self.name = name
    
    def inspect(self):
       print(self.__class__.__name__, self.name) # ссылка на класс объекта и далее на имя класса
       print('id({self.gid})')
       print('Active' if self.active else 'Dead')
       print(self.__dict__) # словарь атрибутов класса

class Guest(User):
    '''Гость'''
    
    def check_permissions(self):
       print('Права:','Чтение')

class Admin(User):
    '''Администратор'''
    
    def check_permissions(self):
       print('Права:', 'Чтение', 'Редактирование')

class Root(User):
    '''Суперпользователь'''
    gid = 0
    active = False
 
    def check_permissions(self):
        print('Права:', 'Чтение', 'Редактирование', 'Записþ')

    def get_token(self):
        print(self.__token)


# acc1 = Guest("Радж")
# acc1.inspect() # Метод базового класса
# acc1.check_permissions() # Метод текуûего класса
# print(acc1.__class__)

acc0 = Root()
acc0.get_token()


# print("Сем")
# acc2 = Admin()
# acc2.inspect() # Метод базового класса
# acc2.check_permissions()





