# for ciklus szintaktikája

# egyéb nyelvek
# for (int item; item> 10; item++) {

# }
# python
# for item in iterálható objektum:
#     cikluson belüli műveletek



#unpacking - kicsomagolás

szam1, szam2, szam3 = 1, 2, 3

szam1, szam2, szam3, szam4 = (1, 2, 3, 4)

# print(szam1)
# print(szam2)
# print(szam3)
# print(szam4)


my_list = [1,2,3]
my_list2 = [4, 5, 6]

my_list3 = [*my_list, *my_list2]

#print(my_list3)

my_list = ["Karcsi", "Senna", 'Pityu', "Jozsó", "Béla", "Jolán", "Margit"]

my_list2 = [("Ricsi", "Laci"), ("Margit", "Karolina")]

for item in my_list:
    if item == "Jozsó":
        print(my_list.index(item))
print("########################################")   

    
for idx, item in enumerate(my_list):
    print(f"{idx}-{item}")

print("########################################")   
for idx, item in enumerate(my_list2):
    print(item[3])

print("########################################")