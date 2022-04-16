# hiba kezelés - exception handling
#
#

""" try-catch - try-except
try:
    fusson_a_fuggveny()
    egye_usitasok()
    for i in ciklus:
        pass
except: -> itt lehet megadni specifikus hibákat, többet is adott esetben

    ide kell azokat a hibakezeléssel kapcsolatos kódrészleteket tenni,
    amelyeket szeretnénk:
    hibának a logolása
    újrafuttatás - ha úgy megírva a program
    egyéb folyamat elindítása

finally:
    print("Ez fusson le")
    Ide azokat a programkódokat célszerű megfuttatni
    amelyek sikeres futás esetén is illetve hibás futás esetén is le
    kell hogy fussanak



"""

def division(num1, num2):
    eredmeny = None
    try:
        eredmeny = num1 / num2    
    except Exception as err:
        print(err)        
    finally:
        print("Ez mindenképpen lefut")

    return eredmeny

temp = division(1, 1)

print(temp)