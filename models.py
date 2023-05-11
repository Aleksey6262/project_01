# Наследование - передача атрибутов и методов дочернему классу
 
class Plane(object):
    
    def __init__(self) -> None:
        self.wings = True
        self.cargo_limit = 20
        self.engine = 2
 
    def fly(self):
        self.speed = 500
        return f'Полет со скоросью {self.speed}'
    
 
class CargoPlane(Plane):
    
    def __init__(self):
        super().__init__()
        self.cargo_limit = 100
        self.engine = 4
 
class WarPlane(Plane):
 
    def shoot(self):
        return 'BABAH'
 
# Экземпляры класса
TU214 = CargoPlane()
print(TU214.fly())
 
AN12 = WarPlane()
print(AN12.shoot())
AN12.__str__()