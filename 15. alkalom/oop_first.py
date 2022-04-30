
class MyFistClass:
    pass

my_object = MyFistClass
my_object = MyFistClass()

# print(type(my_object))

#########################################################################
########################### 4 principle #################################

# 1. principle
# abstraction - absztrakció: class definícióban rejtsük el a valódi logikát, 
# a definíción kívül minket nem érdekel, hogy hogyan van megvalósítva, csak működjön
def my_func(a, b):
    return a + b

## __file__ ; __name__ == __main__
class Human:
    # konstruktor - constructor
    # __ aláhúzásos függvények neve: double underscore - dunderscore
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        print(f"Hello {self.name}")

ember = Human(name="Karcsi", age=30)

#ember.welcome()

############################################################################

# 2. inheritance - öröklődés:
# olyan mechanizmus, amellyek "gyekmek" objektumot tudunk létrehozni őgy, hogy 
# egy másik osztály definícióból származtatjuk le
# a származtatott osztály minden attribútumát és tulajdonságát örökölve

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def welcome(self):
        print(f"Hello {self.name}")


class Woman(Human):
    def __init__(self, name, age, sex, work):
        super().__init__(name,  age, sex)
        self.work = work


first_woman = Woman(name="Rita", age="30", sex="woman", work="teacher")

#first_woman.welcome()
first_woman.name

################################################################################

class EmlosAllat:
    def __init__(self, name):
        self.name = name
        self.animal_type = "emlősállat"

    def eat(self):
        print("evett a jószág")

class Predator(EmlosAllat):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type


class Vegetarian(EmlosAllat):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

####################################################################
 # 3. encapsulation - egységbezárás: tarts minden attrib€tumot privateként, hacsak nem akarjuk
 # nyílvánossá tenni

 # public, private, protected -> pythonban szinte minden publikus, nincs valódi private láthatóság

my_list = [1,2, 3]

def my_func():
    my_list2 = [4, 5, 6]

##################################################


class Fish:
    def __init__(self):
        self.type = "ponty"
        # változók és függvények elejére __ -> "privát" lesz a láthatósága
        self.__size = "big"
        self.__calculate_salary_raise()

    def getter_size(self):
        return self.__size

    def setter_size(self, size):
        self.__size = size

    def __calculate_salary_raise(self):
        print(2 + 3)


test = Fish()

#print(test._Fish__size)

test._Fish__size = "csak érdekesség"
#print(test.getter_size())



#print(test.type)

test.type = "harcsa"

#print(test.type)
#print(test.getter_size())

test.setter_size("little")

#print(test.getter_size())

#print(test.__calculate_salary_raise())
    
###############################################################################
# Polymorphism - polimorfizmus - többalakúság
# ugyan a függvényt használjuk különboző típusokon, lehet hogy, különböző outputokat fogunk kapni

# len()
print("##############################")
print(len("almafa"))

print(len([1, 2, 3, 4]))

class Sweden:
    def capital(self):
        print("Stockholm is the capital")

    def language(self):
        print("Swedish, but almost everybody speak English")

    def type(self):
        print("It's a developed country")

class Hungary:
    def capital(self):
        print("Budapest is the capital")

    def language(self):
        print("Magyar")

    def type(self):
        print("It's a developing country")


sweden = Sweden()
hungary = Hungary()

for country in (sweden, hungary):
    country.capital()
    country.language()
    country.type()

################################

# 4.1 method overriding


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Háp háp")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Vau Vau")


kacsa = Duck(name="Dagobert")
kutya = Dog(name="Lessie")

kacsa.make_sound()
kutya.make_sound()

#######################################################






