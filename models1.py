
# Наследование

class User:
 '''Моделþ полþзователā'''
    gid = 1000
    active = True
 
    def inspect(self):
        print('id({self.gid})')
        print('Active' if self.active else 'Dead')

class Guest(User):
 '''Гостþ'''
 def check_permissions(self):
 print('Права:','Чтение')



