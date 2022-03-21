# while ciklus - hátultesztelős ciklus

#while logikai vizsgálat:
#   ciklusban a programkódok
#

szam = 10
while szam >= 0:
    print(szam)
    #szam = szam - 1
    szam -= 1

# mikor célszerű használni a while ciklust:
# ha valamilyen event jelenséget kell vizsgálnod, figyelned
# a pythonban 2 sor kód elég a végtelen ciklushoz

while True:
    print(szam)