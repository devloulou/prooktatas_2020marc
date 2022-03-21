# lista

my_list = ["Karcsi", "Senna", 'Pityu', "Jozsó", "Béla", "Jolán", "Margit"]

# ciklus változó: bármi lehet a neve, jelen esetben: item
for item in my_list:
    print(item + "_nev")

for item in my_list:
    item = item + "_nev"

print("###################################")
# enumerate függvény: visszaadja egy 
# iterálható objektum index értékét és az elem értékét is
my_tup = (10, 20)

num1, num2 = my_tup

print(num1)
print(num2)
print("###################################")

for idx, item in enumerate(my_list):
    if item == 'Béla':
        my_list[idx] = "Gergely"

print(my_list)


print("###################################")


my_list = [10, 4, 2, 5, 6, 1, 8, 9, 7, 3]

my_list1 = []

# feladat: minden páros elemet rakjuk bele a my_list1-be
for item in my_list:
    if (item % 2) == 0:
        my_list1.append(item)

print(my_list1)