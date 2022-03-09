# Python dinamikusosan tipusos nyelv - dynamic typed

# int szam = 10;
# String my_string = 'Ez egy string';


# mi az hogy változó?

my_num = 10 # ez egy változó
my_str = 'ez egy string'
my_str2 = "ez egy másik string"


my_num = 10 # mi történik ilyenkor?

my_num = "ez mégis egy string legyen"


# memóriában létrejön egy objektum,
# aminek van egy memória címe
# lefoglalja az értéket
# és beállít egy típust neki

my_num = 10
my_num2 = 10

# referencia hivatkozás történik az értékre

# print(my_num)
# print(my_num2)

# print(id(my_num))
# print(id(my_num2))

# print(5+3)
# print(5-3)

# # a my_num megegyezik a my_num2-vel: 
# # ez visszaad egy True vagy False értéket
# print(my_num == my_num2)

# #print(help(my_num))

# # alaptípusok:

# my_int = 10 # integer

# my_float = 10.1 # float

# print(type(my_int))
# print(type(my_float))

# print(print)
# print(type(print))


# print(id(print))
# print(help(5+2))


# alaptípusok:
my_complex_num = 2+3j

#print(type(my_complex_num))

my_int = 10 # integer

my_float = 10.0 # float

sum_int_float = my_float + my_int

#print(type(sum_int_float))

#print(type(5/2)) # ez a 2.# pythonban ez nem így van: 2
########################################################################

# string típus

my_string = ''
my_string2 = ""

# mi a string: a string az karakterlánc -> a legkisebb eleme a karakter -> 
# tehát egy string több karakterből áll -> minden egyes karaktert el tudjuk érni pozíciója alapján
# -> a string egy iterálható objektum

my_string = "ez nem egy rövidke string karakterlánc"

# string slicing
# pozíciót indexnek nevezzük, és minden iterálható objektum indexelése
# 0-val kezdődik

print(
    my_string[11:18]
)

print(
    my_string[26:38]
)

# trükkök

# utolsó karakter
print(
    my_string[-1]
)

# az utolsó 4 karaktert add vissza
print(
    my_string[-4:] # -4 >= x > -2
)

print(
    my_string
)

print(
    my_string[:18]
)

print(
    my_string[:]
)


print(
    my_string[:18]
)

print(
    my_string[0:18:6]
)

# string formázás

# összetett típusok
# lista
# tuple
# dictionary
# set