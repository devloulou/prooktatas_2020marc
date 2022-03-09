my_list = [1, 2, 3, ["Ricsi", 'Janó']]
num = 100
name = 'Tamás'

# referencia hivatkozás
b = my_list

my_list.pop(0)

my_list[2].pop(0)

print(b)
print(my_list)


print('############################################')
# a referencia első szintjének megszűntetése
my_list = [1, 2, 3, ["Ricsi", 'Janó']]
b = []
b.extend(my_list)

my_list.pop(0)

print(b)
print(my_list)

print('############################################')

# a belső referencia továbbra is fenn áll
my_list = [1, 2, 3, ["Ricsi", 'Janó']]
b = []
b.extend(my_list)

print(id(b[3]))
print(id(my_list[3]))
print()
print(id(b))
print(id(my_list))

print("###################")

my_list.pop(0)

my_list[2].pop(0)

print(b)
print(my_list)