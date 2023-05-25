
# Наследование

class User:
    '''Модель пользователя'''
    gid = 1000
    active = True
    
    def inspect(self):
      print('id({self.gid})')
      print('Active' if self.active else 'Dead')

class Guest(User):
    '''Гость'''
    
    def check_permissions(self):
       print('Права:','Чтение')

class Admin(User):
    '''Администратор'''
    
    def check_permissions(self):
       print('Права:', 'Чтение', 'Редактирование')

print("Радж")
acc1 = Guest()
acc1.inspect() # Метод базового класса
acc1.check_permissions() # Метод текуûего класса

print("Сем")
acc2 = Admin()
acc2.inspect() # Метод базового класса
acc2.check_permissions()



# acc0 = Root()
# acc0.check_permissions()
# print(acc0.gid)




