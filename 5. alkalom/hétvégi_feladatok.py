# 1. feladat
# Írjatok egy olyan scriptet, amely
# a megadott lista elemeit elosztja 10-el
# és egy listába letárolja az így kapott értéket

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 2. feladat:
# a megadott dictionary-ben javítsátok a name kulcsot title-re


my_dict = {
    "game": {
        "action": [
            {"title": "Call of Duty"},
            {"title": "Battlefield"}
        ],
        "rpg": [
            {"title": "Oblivion"},
            {"title": "Dark Souls"}
        ],
        "arcade": [
            {"name": "Need for Speed"}
        ]
    }

}

# 3. feladat:
# gyűjtsétek ki egy listába a megadott dictionary kulcsait, egy másik listába az ártékeket
# használjatok dictionary-hez kapcsolódó művelete / függvényt


my_dict = {
    "foo": "bar",
    "color": "blue",
    "country": "Sweden"
}

# 4. feladat:
# töröljétek az összes olyan elemet a listából, amely
# nem osztható maradék nélkül 5-al

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

# 6. feladat:
# írjatok egy olyan scriptet, amely a lista elemeiből
# csak az utolsó 3 karaktert hagyja meg

# elvárt output:
# ["rna", "lma", "ata", "ack", "émi"]

my_list = ['Barna', "alma", "Kata", "barack", "Noémi"]

############################################################
# 7. feladat:
# a megadott dictionary-ből töröljétek a color hoz tartozó értékeket
# illetve ahol a type = diesel ott állítsátok be hybrid -nek az értéket
my_dict = {
    "auto": [
        {
            "brand": "BMW",
            "color": "white",
            "type": "diesel"
        },
        {
            "brand": "Volvo",
            "color": "yellow",
            "type": "benzin"
        },
        {
            "brand": "Tesla",
            "color": "black",
            "type": "electric"
        }
    ]
}
############################################################
# 8. feladat
# a listát töltsétek fel  30 random számmal
# csak azok a számok kerüljenek a listába, amelyek oszthatóak 3-al
# a random generálásnál 1 - 100 közötti értékeket generáljatok

my_list = []

