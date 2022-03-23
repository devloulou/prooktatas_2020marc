# 1. feladat
# Írjatok egy olyan scriptet, amely
# kiírja a megadott lista index-eit és elemeit

# pl: 0 - 10
# 1 - 20

my_list = [10, 20, 30, 40, 50, 60, 70]

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

# 3. feladat:
# gyűjtsétek ki egy listába a megadott dictionary kulcsait
# használjatok dictionary-hez kapcsolódó művelete / függvényt


my_dict = {
    "foo": "bar",
    "color": "blue",
    "country": "Sweden"
}

# 4. feladat:
# töröljétek az összes olyan elemet a listából, amely
# nem osztható maradék nélkül 3-al

my_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]


# 5. feladat:
# írjatok egy olyan programot, amely a 2 listából csinál egy dictionary-t
# pl: {
#   1: "alma",
#   2: "körte"
#   .
#   .
#   5: "dinnye"
# }

my_list = [1, 2, 3, 4, 5]
my_list2 = ["alma", "körte", "barack", "banán", "dinnye"]

my_dict = {}