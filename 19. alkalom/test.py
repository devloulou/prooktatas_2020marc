#Megoldások:
# 1. feladat        /KÉRDÉS: 0-10,1-20?/

my_list = [10, 20, 30, 40, 50, 60, 70]
for i in enumerate(my_list):
    print(i)

# 2. feladat:

my_dict = {
    "books": [
        {
            "writer": "J.K. Rowlings",
            "book": "Harry Potter and the Goblet of the Fire"
        },
        {            
            "book": "Sorstalanság"      # TÖRLENDŐ. MY_DICT DICTIONARY,'BOOKS' NEVŰ KULCS ÉRTÉKE AMI LISTA, ANNAK AZ  1 INDEXŰ ELEME AMI DICTIONARY.
        },
        {
            "writer": "Mikszáth Kálmán",
            "book": "Szent Péter esernyője"
        }
    ]

}
my_dict['books'].pop(1)
#vagy
# del my_dict['books'][1]


# 3. feladat:
# gyűjtsétek ki egy listába a megadott dictionary kulcsait
# használjatok dictionary-hez kapcsolódó művelete / függvényt
my_list3=[]
my_dict = {
    "foo": "bar",
    "color": "blue",
    "country": "Sweden"
}
for j in my_dict:
    my_list3.append(j)

print(my_list3)    

# 4. feladat:
# töröljétek az összes olyan elemet a listából, amely
# nem osztható maradék nélkül 3-al

my_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]      # Ez lenne az új lista tartalma: 3,9,15,21,25

for x in my_list:
    if  x % 3 != 0: 
        my_list.remove(x)
# PROBLÉMA: MIUTÁN LEFUT AZ 53. SOR  A FOR CIKLUS SZERETNÉ MEGVIZSGÁLNI A LISTÁM KÖVETKEZŐ ELEMÉT DE                       
# MIVEL TÖRLŐDÖTT AZ ELEM EZÉRT A LISTA SORON KÖVETKEZŐ INDEXŰ ELEME MÁR NEM AZ AZ ELEM. :(         
print(my_list)        


# 5. feladat:
# írjatok egy olyan programot, amely a 2 listából csinál egy dictionary-t
my_list = [1, 2, 3, 4, 5]
my_list2 = ["alma", "körte", "barack", "banán", "dinnye"]

my_dict = {}

for my_key in my_list:
    for my_value in my_list2:
        my_dict[my_key] = my_value

print(my_dict)