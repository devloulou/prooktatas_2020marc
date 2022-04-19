import os
#1. Feladat
#Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt,
# ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza!
# A program tartalmazza a függvény hívását is!

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def osszegzo(lista):
    temp = 0
    for item in lista:
        temp += item

    return temp

#print(osszegzo(my_list))

def osszegzo(lista):
    return sum(lista)

#print(osszegzo(my_list))


def osszegzo(*args):
    return sum(args)

#print(osszegzo(*my_list))



####################################################################
# 2. Feladat
# Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, 
# amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, 
# ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!

my_list = [1, 3, 5, 6, 7, 8, 9]

my_list2 = [11, 13, 15, 17, 19, 21]


def paros_e(lista):
    for item in lista:
        if item % 2 == 0:
            return True
    return False

#print(paros_e(my_list))
#print(paros_e(my_list2))

####################################################################
# 3.1 Feladat
# Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, 
# amely a paraméterként átvett listában megvizsgálja, 
# hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
# A program tartalmazza a függvény hívását is!

my_list2 = [11, 13, 15, 17, 19, 21]

def harommal_oszthatok(lista):
    temp = []
    for item in lista:
        if item % 3 == 0:
            temp.append(item)

    return len(temp)

#print(harommal_oszthatok(my_list2))

def harommal_oszthatok(lista):
    return len([item for item in lista if item % 3 == 0])

#print(harommal_oszthatok(my_list2))

# 3.2 Feladat
# Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában,
# és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)
# input használatával

def my_func():
    temp = []
    temp2 = []

    my_num = 0
    while my_num >= 0:
        my_num = int(input("Kérem add meg a számot! "))
        if my_num >= 0:
            temp.append(my_num)

    print(temp)

    for item in temp:
        if item % 3 == 0:
            temp2.append(item)
    
    return len(temp2)



def my_func():
    temp = []
    temp2 = []

    my_num = 0
    running = True
    while running:
        my_num = int(input("Kérem add meg a számot! "))
        if 0 >= my_num:
            running = False
            break

        temp.append(my_num)

    print(temp)

    for item in temp:
        if item % 3 == 0:
            temp2.append(item)
    
    return len(temp2)

#print(my_func())
####################################################################

# 4. Feladat
# Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír!
# A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények,
# amely a lista legkisebb elemével tér vissza. A program írja ki, hogy melyik volt a megadott legkisebb szám!

def adat_beker():
    temp = []
    my_num = 0
    while my_num >= 0:
        my_num = int(input('Adj meg egy szamot! '))

        if my_num >= 0:
            temp.append(my_num)

    return temp

def legkisebb(lista):    
    return min(lista)


def main():
    lista = adat_beker()
    print(f"legkisebb szám: {legkisebb(lista)}")

##############################################

def adat_beker(*args):
    temp = []

    for item in args:
        if item >= 0:
            temp.append(item)
        else:
            break

    print(f"temp: {temp}")
    return temp

def legkisebb(lista):    
    return min(lista)

def main():
    lista = adat_beker(1, 2, -4, 3, 4, 5, 6, 7, -1)
    print(f"legkisebb szám: {legkisebb(lista)}")

main()