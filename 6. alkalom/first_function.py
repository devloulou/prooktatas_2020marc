
# prototipizálás
def my_func():
    pass

# minden függvénynek van visszatérési értéke, alapértelmezetten: None
# opcionális, hogy adunk e a függvénynek paramétert

# írjunk egy olyan függvényt, amely összead 2 számot

# 1. lépés
def osszeadas():
    pass

# 2. lépés
# a függvény zárójelek közötti részét használom paraméterek átadására
def osszeadas(szam1, szam2):
    print(szam1+szam2)

osszeadas(10, 6)

my_print = print

my_osszeadas = osszeadas

# egy függvényt hozzá lehet rendelni egy vagy több változóhoz

print("Ezt a print függvénnyel iratom ki")
my_print("Ezt az én my_print változómmal iratom ki")

print(my_osszeadas)

my_osszeadas(1, 2)


print("########################################")
def osszeadas(szam1, szam2):
    print(szam1+szam2)

print(osszeadas(1, 2))

def osszeadas2(szam1, szam2):
    osszeg = szam1 + szam2
    return osszeg

print("########################################")

my_num = osszeadas2(14, 21)

print(my_num)


print("########################################")

# az alább definiált függvényünk paramétereit kötelezően meg kell adni
def osszeadas2(szam1=1, szam2=4):
    osszeg = szam1 + szam2
    print(osszeg)
    return osszeg


osszeadas2(10)
osszeadas2(10, 30)
osszeadas2()
#osszeadas2(10, 12, 13)

##############################################################
print("########################################")

import random

my_list = []

for i in range(0, 30):
    num = random.randint(1, 100)    
    if (num%3) == 0:
        my_list.append(num)

my_list2 = []

def auto_number_loader():
    for i in range(0, 30):
        num = random.randint(1, 100)    
        if (num%3) == 0:
            my_list2.append(num)

auto_number_loader()
auto_number_loader()

print(my_list2)

# modul fogalma
# os modul
# *args, **kwargs - packing unpacking fügvényeknél
# typehinting
# return-nél packing unpacking

# scope, namespace
# decorator
# generator függvények
# file műveletek alapjai - itt sok időt el fogunk tölteni
    # csv, txt, json, excel
    # with contextusmanager
# adatbázis műveletek - SQL, különböző libraryk
# docker
# git-et
# pandas
# OOP - projektmunkát ~ 25 óra
# http műveletek
# fogunk beszélni a lehetőségekről a pythonnal kapcsolatban
# MongoDB - NoSQL adatbázis
# UI