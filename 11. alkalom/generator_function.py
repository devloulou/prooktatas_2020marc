import sys

my_list = [item for item in range(0, 1000000)]

my_gen = (item for item in range(0, 1000000))

print(sys.getsizeof(my_list))
print(sys.getsizeof(my_gen))

# lazy evaluation - laza kiértékelés

for item in range(100):
    print(next(my_gen))


# függvények - return , a return utasítás megállítja a program futását
# és a futás nem folytatható
print("##############################")

def my_func(a, b):
    print("fut a program")
    return a + b
    print()

print(my_func(1, 2))

##############################################
print("##############################")

def my_normal_func(num):
    sum_nums = 0
    for item in range(1, num):
        sum_nums += item

    return sum_nums


eredmeny = my_normal_func(4)
print(eredmeny)

#######################################################
# a generátor függvény nem return-öl, hanem yield-el

print("##############################")
def my_gen_func():
    print("történik e valami")
    yield 1

next(my_gen_func())

print("##############################")

def my_gen_func(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

func = my_gen_func(10)

# for item in func:
#     print(item)

# a generátor függvények olyanok, amelyeket meg lehet állítani,
# és vissza lehet térni a futáshoz menet közben.

# Emiatt a viselkedés miatt memória hatékonyabb mint a normál függvények
# emiatt lassabbak is


print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))


