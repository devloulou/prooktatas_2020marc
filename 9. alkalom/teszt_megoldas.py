# 1. feladat:
# A Fibonacci sorozatra igaz, hogy minden elem az azt megelőző 2 elem
# összegével egyenlő.
# Írjatok egy olyan függvényt, amely paraméterben kap egy számot.
# A megadott szám a Fibonacci sorozat új elemeinek számát jelenti.

# A függvény szúrja be az új elemeket a lenn megadott listába
# példa függvényhívásra: my_fib(2) -> elvárt eredmény:  [0,1,1,2,3,5,8,13]

from re import M


my_list = [0,1,1,2,3,5]

# clean code elv
def my_func(my_num):
    # docstring
    """"""
    # a lista utolsó elemét adjam hozzá az utolsó előttihez
    for i in range(0, my_num):
        my_list.append(my_list[-1] + my_list[-2])

#my_func(5)

#############################################

# Miért kell nekünk 
print("#############################################")
r = 5
pi = 3.14

# az r és pi értéke más láthatóségi szinten szerepel, mint a függvényem belseje
def my_func():
    return r + pi

# bejövő paramétereket kap és azok értékeit használja fel a máveletéhez
def my_func2(a, b):
    return a + b

def my_func3(a, b):
    eredmeny = a + b
    return eredmeny

eredmeny = my_func()

eredmeny2 = my_func2(1023, 54345)

print(eredmeny2)
##########################################################################################
