# 1. feladat:
# adjatok egy tetszőleges kulcs-érték párt a megadott dictionaryhez.

my_dict = {
    "auto": "BWM"
}

my_dict['kulcs'] = "érték"

my_dict.update({"ez_egy_kulcs": "ez_egy_ertek"})

#print(my_dict)

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

my_dict['auto'][0]["price"] = 1
my_dict['auto'][1]["price"] = 2
my_dict['auto'][2]["price"] = 3

my_dict['auto'][0].update({'price': 5})
my_dict['auto'][1].update({'price': 6})
my_dict['auto'][2].update({'price': 7})

#print(my_dict)

############################################################
# 3. feladat
# a megadott litából hozzatok létre egy tuple-t úgy,
# hogy az első elemtől minden 2. elemet tartalmazza

my_list = ["alma", "körte", "banán", "narancs", "dinnye", "barack"]

my_tupl = tuple(my_list[::2])
my_tupl = tuple(my_list[0::2])
my_tupl = tuple(my_list[0:-1:2]) # ez nem a legszebb

#print(my_tupl)

############################################################
# 4. feladat:
# gyújtsétek ki a pozíció megnevezéseket egy listába
# egy másik listába pedig a fizetéseket
my_dict = {
    "position": [
                    {
                        "pos1": {
                            "position": "junior developer",
                            "salary": 550000
                            }   ,
                        "pos2": {
                            "position": "medior developer",
                            "salary": 750000
                            },
                        "pos3": {
                            "position": "senior developer",
                            "salary": 1250000
                            }
                    }
                ],
        
    "jobs": [

        ]
    
        }

my_list1 = [my_dict['position'][0]['pos1']['position'],
            my_dict['position'][0]['pos2']['position'],
            my_dict['position'][0]['pos3']['position']
            ]

my_list2 = [my_dict['position'][0]['pos1']['salary'],
            my_dict['position'][0]['pos2']['salary'],
            my_dict['position'][0]['pos3']['salary']
            ]

# print(my_list1)
# print(my_list2)

############################################################
# 5. feladat:
# Írjatok egy olyan kis scriptet, ami teljesíti a következő feltételt:
# ha szam1 > szam2 akkor eredmeny = szam1 - szam2
# ha eredmeny > szam2 akkor eredmeny = szam2, különben eredmeny = 0

szam1 = 10
szam2 = 5
eredmeny = None

if szam1 > szam2:
    eredmeny = szam1 - szam2

if eredmeny > szam2:
    eredmeny = szam2
else:
    eredmeny = 0


#print(eredmeny)


# 5. feladat, b: ha szam1 osztva szam2-vel 0 akkor az eredmény legyen szam2 négyzete: eredmeny = szam2^2
#print((szam1/szam2)==0)

if (szam1/szam2)==0:
    eredmeny = szam2**2


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

if my_dict["age"] > 17:
    my_dict['licence'] = True

my_dict['licence'] = True if my_dict["age"] > 17 else False

if szam1 - 2 > 4:
    pass
elif szam1 - 5 > 2:
    pass
elif szam1 - 4 > 3: 
    pass


#print(my_dict)

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

#del my_dict['auto'][2]

my_dict['auto'].pop(2)

#print(my_dict)

############################################################
# 8. feladat: módosítsátok a listát úgy, hogy csak a print, a [], és None elemek maradjanak a listában.
# Törekedjetek a lista múveletek használatára

my_list = [1, 2, 3, 47, 8, 9, 5, print, [], None, 5, 6, 4, 3, 56]

my_list = my_list[7:10]

# my_list.pop(0)
# my_list.pop(0)
# my_list.pop(0)
# my_list.pop(0)
# my_list.pop(0)
# my_list.pop(0)
# my_list.pop(0)
# my_list.pop(-1)
# my_list.pop(-1)
# my_list.pop(-1)
# my_list.pop(-1)
# my_list.pop(-1)

#print(my_list)