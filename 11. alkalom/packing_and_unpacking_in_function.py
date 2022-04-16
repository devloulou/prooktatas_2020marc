# packing és unpacking

my_list = [1,2,3]
my_list2 = [4, 5, 6]

my_list3 = [*my_list, *my_list2]

print(my_list3)

####################

my_tuple = (1, 2, 3)

a, b, c = my_tuple

print(b, a, c)

a, *b = my_tuple

print(b, a)

print("####################################################################")

####################################################################
# függvények és a packing - unpacking
# *args, **kwargs -> key-value arguments

# ha olyan megoldást leprogramozni
# ahol nem tudom előre, hogy hány paraméterem lesz a függvénynek
def my_func(*args): # az args-ba beleteszzük a meghívásnál kapott paramétereket
    print(args)

my_func(1, 2, "Ricsi", None, "Pista", print)


def my_func(**kwargs):
    if kwargs.get("salaray"):
        print("növeld meg az értékét")

my_func(name="Ricsi", salary=500000, color="red")

##########################################################

def my_func(name, email, telefon, *args, **kwargs):
    print(name)
    print(email)
    print(telefon)
    print(args)
    print(kwargs)
# ha kulcs érték párokat adok meg, utána nem adhatok meg más megadással bejövő értéket
# 
my_func("Ricsi", 1, 2, 3, "Pista", "Karcsi", [1, 2, 3], salary=50)

############################################################