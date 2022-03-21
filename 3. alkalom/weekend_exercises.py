# 1. feladat:
# adjatok egy tetszőleges kulcs-érték párt a megadott dictionaryhez.

my_dict = {
    "auto": "BWM"
}

############################################################
# 2. feladat:
# a megadott dictionaryben lévő autokhoz 
# adjatok hozzá egy price kulcsot és egy tetszőleges értéket állítsatok be hozzá

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
# 3. feladat
# a megadott litából hozzatok létre egy tuple-t úgy,
# hogy az első elemtől minden 2. elemet tartalmazza

my_list = ["alma", "körte", "banán", "narancs", "dinnye", "barack"]

############################################################
# 4. feladat:
# gyújtsétek ki a pozíció megnevezéseket egy listába
# egy másik listába pedig a fizetéseket
my_dict = {
    "positions": [
        {
            "pos1": {
                "position": "junior developer",
                "salary": 550000
                },
            "pos2": {
                "position": "medior developer",
                "salary": 750000
                },
            "pos3": {
                "position": "senior developer",
                "salary": 1250000
                }
        }
    ]
    
}

############################################################
# 5. feladat:
# Írjatok egy olyan kis scriptet, ami teljesíti a következő feltételt:
# ha szam1 > szam2 akkor eredmeny = szam1 - szam2
# ha eredmeny > szam2 akkor eredmeny = szam2, különben eredmeny = 0

szam1 = 10
szam2 = 5
eredmeny = None

# 5. feladat, b: ha szam1 osztva szam2-vel 0 akkor az eredmény legyen szam2 négyzete: eredmeny = szam2^2


############################################################
# 6. feladat: 
# Írjatok egy olyan scriptet, amely az alább megadott feltételt teljesíti
# ha az age nagyobb mint 17, akkor a licence értéke legyen igaz.

my_dict = {
            "auto": [{"type": "Volvo",
                     "color": "gold"
                    },
                    {"type": "Audi",
                     "color": "red"
                    },
                    {"type": "Reanult",
                     "color": "White"
                    } ],
            "driver": ["Heikki Kovalainen", "Bruno Senna", "Sebastien Buemi"],
            "licence": False,
            "age": 18
        }
############################################################
# 7. Nem szeretjük a francia autót, töröljök a renault az autók közül. A többi érték ne változzon.

my_dict = {
            "auto": [{"type": "Volvo",
                     "color": "gold"
                    },
                    {"type": "Audi",
                     "color": "red"
                    },
                    {"type": "Reanult",
                     "color": "White"
                    } ],
            "driver": ["Heikki Kovalainen", "Bruno Senna", "Sebastien Buemi"],
            "licence": False,
            "age": 18
        }

############################################################
# 8. feladat: módosítsátok a listát úgy, hogy csak a print, a [], és None elemek maradjanak a listában.
# Törekedjetek a lista múveletek használatára

my_list = [1,2,3,47,8,9,5, print, [], None, 5,6,4,3,56]
