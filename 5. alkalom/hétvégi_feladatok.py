# 1. feladat
# Írjatok egy olyan scriptet, amely
# a megadott lista elemeit elosztja 10-el
# és egy listába letárolja az így kapott értéket

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

my_list1 = []
for item in my_list:
    my_list1.append(int(item/10))

print(my_list1)

my_list2 = [int(item/10) for item in my_list]

print(my_list2)

print("##############################################")

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

for key, value in my_dict.items():
    value['arcade'][0] = {'title': value['arcade'][0]['name']}

print(my_dict)

#my_dict['game']['arcade'][0] = {"title": "Need for Speed"}
my_dict2 = {}

print(my_dict.keys())
# for key, value in my_dict.items():
#     if key == 'name':
#         my_dict2['title'] = value
#     else:
#         #  if type(value) == dict:
#         #      print(value.keys())
#         if isinstance(value, dict): # isinstance -> True vagy False értéket ad vissza
#             if 'name' in value.keys():
#                 my_dict2[key] = value
#                 my_dict2[key]['title'] = value['name']
#                 my_dict2[key].pop('name')
#             else:
#                 for k, v in value:
#                     if isinstance(v, dict): # type(v) == dict
#                         if 'name' in v.keys():
#                             my_dict2[key][k] = v
#                             my_dict2[key][k]['title'] = v['name']
#                     elif isinstance(v, list):
#                         for item in v:
#                             pass

#print(my_dict2)
print("##############################################")

#print(my_dict)




# 3. feladat:
# gyűjtsétek ki egy listába a megadott dictionary kulcsait, egy másik listába az ártékeket
# használjatok dictionary-hez kapcsolódó művelete / függvényt


my_dict = {
    "foo": "bar",
    "color": "blue",
    "country": "Sweden"
}

my_list = list(my_dict.keys())
my_list1 = list(my_dict.values())

print(type(my_list))
print("##############################################")


# 4. feladat:
# töröljétek az összes olyan elemet a listából, amely
# nem osztható maradék nélkül 5-al

my_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
# 12 eleme van , max_index = 11 -> elemszám - 1 -> max index

my_list1 = []

for item in my_list:
    if (item%5) == 0:
        my_list1.append(item)

my_list = my_list1

print(my_list)
print("##############################################")

# 5. feladat:
# írjatok egy olyan programot, amely a 2 listából csinál egy dictionary-t
# pl: {
#   1: "alma",
#   2: "körte"
#   .
#   .
#   5: "dinnye"
# }

my_list = [1, 2, 3, 4, 5, 6]
my_list2 = ["alma", "körte", "barack", "banán", "dinnye"]

my_dict = {}

print(len(my_list2))

for idx, item in enumerate(my_list):    
    if len(my_list2) - 1 >= idx:
        my_dict[item] = my_list2[idx]

print(my_dict)
print("##############################################")

# 6. feladat:
# írjatok egy olyan scriptet, amely a lista elemeiből
# csak az utolsó 3 karaktert hagyja meg

# elvárt output:
# ["rna", "lma", "ata", "ack", "émi"]

my_list = ['Barna', "alma", "Kata", "barack", "Noémi"]

my_list2 = []

for item in my_list:
    my_list2.append(item[-3:])

print(my_list2)

my_list3 = [item[-3:] for item in my_list]
print(my_list3)
print("##############################################")

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

for item in my_dict['auto']:
    item.pop('color')
    if item['type'] == 'diesel':
        item['type'] = 'hybrid'

print(my_dict)


############################################################
# 8. feladat
# a listát töltsétek fel  30 random számmal
# csak azok a számok kerüljenek a listába, amelyek oszthatóak 3-al
# a random generálásnál 1 - 100 közötti értékeket generáljatok

import random

my_list = []

for i in range(0, 30):
    num = random.randint(1, 100)    
    if (num%3) == 0:
        my_list.append(num)


print(my_list)

my_list = []
while 30 > len(my_list):
    num = random.randint(1, 100)    
    if (num%3) == 0:
        my_list.append(num)

print(my_list)
print(len(my_list))


###################################
import random
my_list = [random.sample(range(1, 100), 30)]

print (my_list)

my_list2 = []

for item in my_list:
    if (item % 3) == 0:
        my_list2.append(item)

my_list = my_list2

print(my_list)