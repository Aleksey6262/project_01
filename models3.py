
# Наследование

class User:
    '''Модель пользователя'''
    active = True
    __token = 'very_secret_key'

    def __init__(self, name=None):
       self.name = name
       self.gid = 1000
       self.get_permissions('700')

    def __str__(self):
       return '{}, id({}), status({})'.format(self.__class__.__name__, self.gid, 'Active' if self.active else 'Dead')

    def get_permissions(self, args):
       self.u, self.g, self.o = args
       return self.u, self.g, self.o
    
    def check_permissions(self):
        print(f'Права: {self.u} {self.g} {self.o}')

class Guest(User):
    '''Гость'''
    
    def check_permissions(self):
       print('Права:','Чтение')

class Admin(User):
    '''Администратор'''
    def __init__(self, name):
       super().__init__(name=name)
       self.get_permissions('764')
    
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
# acc0.get_token()


# print("Сем")
acc2 = Admin(name="Сем")
print(acc2)
acc2.check_permissions()





