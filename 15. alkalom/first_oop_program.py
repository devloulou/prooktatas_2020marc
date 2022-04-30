# autosalon - autóink, motorjaink
# el tudjuk adni
# bevétel

# @dataclass

class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        # __str__ : egy objektum szöveges reprezentációja - emberileg értelmezhető legyen
        # stringnek kell lennie
        return f"{self.name} - {self.type} object"
    
class Car(Vehicle):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = 'car'


class Motor(Vehicle):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = 'motor'


class Catalogue:
    def __init__(self):
        self.cars = {}
        self.motors = {}

class Salon:
    def __init__(self):
        self.base_money = 3000000
        self.catalogue = Catalogue()

    def upload_catalogue(self, vehicle):
        if vehicle.type == 'car':
           self.catalogue.cars[vehicle.name] = vehicle
        else:
            self.catalogue.motors[vehicle.name] = vehicle        
       

volvo = Car(name="Volvo", price=1250000)
bmw = Car(name="BMW", price=5000000)

print(volvo)

auto_salon = Salon()

auto_salon.upload_catalogue(bmw)

print(auto_salon)
print(auto_salon.__str__())
print(auto_salon.__repr__())

my_num = 5

print(my_num.__str__())
print(my_num.__repr__())

print(type(my_num))