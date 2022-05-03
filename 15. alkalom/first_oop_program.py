# autosalon - autóink, motorjaink
# el tudjuk adni
# bevétel

# @dataclass

from enum import auto
import json


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

    def __str__(self):
        temp = {
            'cars': [],
            'motors': []
        }

        for key, value in self.cars.items():
            temp['cars'].append({"brand": key, "price": value.price})

        for key, value in self.motors.items():
            temp['motors'].append({"brand": key, "price": value.price})

        return json.dumps(temp, indent=4)

class Salon:
    def __init__(self):
        self.base_money = 3000000
        self.catalogue = Catalogue()

    def upload_catalogue(self, vehicle):
        if vehicle.type == 'car':
           self.catalogue.cars[vehicle.name] = vehicle
        else:
            self.catalogue.motors[vehicle.name] = vehicle

    # törölni az adott autót motort a katalógusból
    # a törölt object értékével növelni a base_money értékét

    def delete_from_catalogue(self, item):
        if item.type == "car":
            self.catalogue.cars.pop(item.name)
        else:
            self.catalogue.motors.pop(item.name)

        return item
    
    def transaction_handling(self, item):
        if item.price > 0:
            self.base_money += item.price
        else:

            if 0 > self.base_money - (item.price*-1):
                raise Exception(f"Nincs elengendő pénzed arra, hogy megvedd az {item.type}")

            self.base_money -= (item.price*-1)
            
            if item.type == "car":
                self.catalogue.cars[item.name].price *= -1
            else:
                self.catalogue.motors[item.name].price *= -1
       

volvo = Car(name="Volvo", price=1250000)
bmw = Car(name="BMW", price=5000000)
harley = Motor(name="Harley Davidson", price=10000000)

royce = Car(name="Royce", price=100000000)

opel = Car(name="Opel", price=450000)

auto_salon = Salon()

auto_salon.upload_catalogue(bmw)
auto_salon.upload_catalogue(volvo)
auto_salon.upload_catalogue(harley)

temp = auto_salon.delete_from_catalogue(volvo)

auto_salon.transaction_handling(temp)

print(auto_salon.base_money)

# vétel: vettünk egy opelt.
auto_salon.upload_catalogue(opel)
opel.price *= -1

auto_salon.transaction_handling(opel)

royce.price *= -1
auto_salon.transaction_handling(royce)

print(auto_salon.base_money)

print(auto_salon.catalogue)

exit()
auto_salon.delete_from_catalogue(harley)

print(auto_salon.catalogue)

