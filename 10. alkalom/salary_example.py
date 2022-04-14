print("#############################################")

# írjatok egy olyan programot, ami bekéri a dolgozó fizetését
# és egy random éréket generálva megemeli annyi százalékkal a fizetését, amennyi a generált érték eredménye

# az így kapott fizetést vonjuk le az éves budge-ből

# 5 dolgozó esetében végezzük el ezt a feladatot: találjunk ki 5 eltérő fizetést
# a végén írassuk ki, hogy mennyi maradt a budge: ha negatív, akkor írjuk ki, hogy nem hajható végre az 
# emelés és hajtsuk végre az egész generálást úgy, hogy felezzük meg a százalék megállapításátnál
# megadott random értéket a felére

my_list = [40000, 65000,  76000, 12000, 100000]
budget = 7000

# generáljon egy random értéket a megadott intervallumon belül
def get_random_percent(a, b):
    import random
    return random.randint(a, b)

# végig kell iterálnom a fizetéseken - ami egy lista - 
# minden fizetéshez generálni kell egy random értéket
# az így kapott értéket pl: 5% esetén, a fizetésnek az 5%-át ki kell vonni a budget-ből

def decrease_budget_global(a, b):
    for salary in my_list:
        percent = get_random_percent(a, b)/100
        percent_value = salary * percent  

        global budget

        budget -= percent_value

        print(f"{salary} - {percent} - {percent_value}")

    print(budget)


#decrease_budget_global()

def decrease_budget(budget, a, b):
    for salary in my_list:
        # hard kódolva van a 2 és 5 értéke:  EZT MINDEN ESETBEN ÉRDEMES ELKERÜLNI
        percent = get_random_percent(a, b)/100
        percent_value = salary * percent

        budget -= percent_value

    return budget

# megvizsgálni, hogy a budget az negatív vagy pozitív, ha negatív, 
# a random százalékhoz használt értékek helyett csökkentet értékeket kell megadnom:
# pl első futás: 2 - 5 százalék között, ha a budget negatív,
# újra kellene a kalkulációt futtatni más százalék paraméterekkel


def analyze_budget(kp, num_from, num_to):
    budget_origin = kp
    budget = decrease_budget(kp, num_from, num_to)
    print(budget)
    if budget > 0:
        print("A fizetés emelés végrehajtható a 2 - 5 százalék rátával")
    else:
        # amikor a függvény önmagát meghívja, azt nevezzük rekurziónak
        # rekurzív függvény hívás
        # fibonacchi sorozat x-edik elemét irassátok ki

        analyze_budget(budget_origin, num_from - 2, num_to - 2)

analyze_budget(budget, 2, 5)


# 2. feladat:
# Írjatok egy olyan programot, amely
# a 4 matematikai alapműveletet elvégzi
# a programot úgy írjátok meg, hogy 3 paramétere legyen: 2 szám és egy matematikai jel
# írhattok olyan változatot is, ami output-ról kéri be a matematikai műveletet


def outer_func():

    def inner_func():
        pass

    inner_func()