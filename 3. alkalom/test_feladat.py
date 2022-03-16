# 1. feladat:
# a megadott lista elemeihez adjátok hozzá a 4, és "Józsi" értéket
my_list = [[1, 2, 3], ["Ricsi"]]

my_list[0].append(4)
my_list[1].append("Józsi")


my_list[0].insert(0, 4)
my_list[1].insert(0, "Józsi")

#print(my_list)

####################################################
# elvárt eredmény: [[1, 2, 3, 4], ["Ricsi", "Józsi"]]

# 2. feladat:
# a két listát egyesítétek
my_list = [10, 20, 30, 40, 50]
my_list2 = [60, 70, 80, 90, 100]

my_list3 = [*my_list, *my_list2]

my_list4 = my_list + my_list2

my_list.extend(my_list2)

#print(my_list)


# 3. feladat:
# Írassátok ki a 4, 5, 6 elemet slice művelettel
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

print(my_list[3:6])

# 4. feladat:
# string formázással írassátok ki a következő mondatot:

# Ádám fejlesztőként dolgozik és a kezdő fizetése 600000 Ft bruttó

name = "Ádám"
position = "fejlesztő"
salary = 600000 

my_str = f"{name} {position}ként dolgozik és a kezdő fizetése {salary} Ft bruttó"

print(my_str)

# 5. feladat:
# Töröljétek az utolsó 2 elemet a listából
my_list = ["Kata", "Péter", "Tamás", "Zoltán", "Mariann"]

# my_list.pop(-1)
# my_list.pop(-1)

my_list = my_list[0:-2]

print(my_list)
