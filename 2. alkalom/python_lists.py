# Összetett adattípusok:
# Lista objektum: mutable adattípus -> 
#                 az  elemei és maga a lista megváltoztatható

my_list = []
my_list = list()


my_lst = [1, "Ricsi", ['234', 1, "Dani"], print]

# indexek mentén el lehet kérni a listából 1 adott elemet
# illetve egy megadott részhalmazát is el lehet kérni a listának
print(my_lst[2])
print(my_lst[-2])
print(my_lst[::-2])

my_lst[1] = "Jocó"

print(my_lst)
my_lst[0:2] = [2, "Józsi"]

print(my_lst)

print(my_lst[2][2])

my_lst[2][2] = "Karcsi"

print(my_lst)


# elem törlése listából

# index mentén törölni: pop()
# érték mentén törölni: remove()

#my_lst.clear()

my_lst.pop(3)



print(my_lst)

my_lst2 = [1, 1, 1, 1, 1, 1, 1, 2, 3, 4, "Ricsi", "Ricsi", "Ricsi", "Ricsi"]

my_lst2.remove(1)
my_lst2.remove(1)
my_lst2.remove(1)
my_lst2.remove(1)
my_lst2.remove(1)
my_lst2.remove("Ricsi")

# my_lst2[0:7] = []

print(my_lst2)

my_list3 = []
# append - 1 elemet ad a lista végéhez
my_list3.append("Józsi")
my_list3.append(10)
my_list3.append("almafa")
#my_list3.append([1, 2, 3, 4, 5])

# insert - egy megadott index elé teszi az adatot

my_list3.insert(3, "ez egy insert")
my_list3.insert(-1, "ez egy insert2")

# extend - több érték egyidejű hozzáadása a lista végéhez
my_list3.extend([1, 2, 3, 4, 5])

print(my_list3)

my_list3.extend([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(my_list3)


# listák egyesítése

my_list = [1, 1, 1]
my_list2 = [1, 1, 1]

my_list3 = []

my_list3.extend(my_list)
my_list3.extend(my_list2)

my_list4 = my_list + my_list2

my_list5 = [*my_list, *my_list2]

# * -> asterix operátor
# print(my_list3)
# print(my_list4)
# print(my_list5)

# [1, 2, 3, 4, 5, 6]



#Összegzés:

# Lista egy iterálható - Iterable object - adattípus
# amely mutable - megváltoztatható
# lehet hozzáadni adatot egyesével, tömegesen
# indexek mentén elérjük az adatokat, akár egyesével
# akár több értékről legyen szó
# törölni tudunk elemeket a listából
# össze tudunk vonni listákat

# REFERENCIA