# 1. feladat
# Írjatok egy olyan scriptet, amely
# kiírja a megadott lista index-eit és elemeit

# pl: 0 - 10
# 1 - 20

my_list = [10, 20, 30, 40, 50, 60, 70]

for idx, item in enumerate(my_list):
    print(f"{idx} - {item}")

print("###########################################")
# 2. feladat:
# töröljétek ki azt az elemet, ahol nem szerepel író
# a megoldás során használjatok ciklust és vizsgáljátok meg, hogy létezik e a writer kulcs

my_dict = {
    "books": [
        {
            "writer": "J.K. Rowlings",
            "book": "Harry Potter and the Goblet of the Fire"
        },
        {            
            "book": "Sorstalanság"
        },
        {
            "writer": "Mikszáth Kálmán",
            "book": "Szent Péter esernyője"
        }
        
    ]

}

for elem in my_dict['books']:
    if not elem.get("writer"):
        my_dict['books'].remove(elem)

print(my_dict)
print("###########################################")
# 3. feladat:
# gyűjtsétek ki egy listába a megadott dictionary kulcsait
# használjatok dictionary-hez kapcsolódó művelete / függvényt


my_dict = {
    "foo": "bar",
    "color": "blue",
    "country": "Sweden"
}

my_list = list(my_dict.keys())

my_list = []

for item in my_dict:
    my_list.append(item)

print(my_list)

# 4. feladat:
# töröljétek az összes olyan elemet a listából, amely
# nem osztható maradék nélkül 3-al

my_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

my_list2 = []

for item in my_list:
    print(f"{item} - {(item % 3) != 0}")
    if (item % 3) != 0:
        my_list.remove(item)
print("###########################################")

my_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
my_list2 = []

for item in my_list:
    if (item % 3) == 0:
        my_list2.append(item)

my_list = my_list2

print(my_list)

# 5. feladat:
# írjatok egy olyan programot, amely a 2 listából csinál egy dictionary-t
# pl: {
#   1: "alma",
#   2: "körte"
#   .
#   .
#   5: "dinnye"
# }
print("###########################################")

my_list = [1, 2, 3, 4, 5]
my_list2 = ["alma", "körte", "barack", "banán", "dinnye"]

my_dict = {}

my_dict = {
    my_list[0]: my_list2[0],
    my_list[1]: my_list2[1],
    my_list[2]: my_list2[2],
    my_list[3]: my_list2[3],
    my_list[4]: my_list2[4]
}

print(my_dict)


for idx, item in enumerate(my_list):
    my_dict[item] = my_list2[idx]

    my_dict.update({ item: my_list2[idx]})

print(my_dict)
