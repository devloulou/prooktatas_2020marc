# tuple

# tulajdonságai: immutable - megváltoztathatlan
# költséghatékonyabb adattípus

my_tuple = (1, 2, 3, 4, print, "Ricsi", 1, 1, 2, 2)

my_tuple2 = tuple(1,2,3,4,5)

# my_list = [1,2,3,4]

# my_tuple3 = tuple(my_list)

print(id(my_tuple))

my_tuple = my_tuple[0:-4]

print(id(my_tuple))

print(my_tuple.index(2))

print(my_tuple.count(2))

###########################################################
