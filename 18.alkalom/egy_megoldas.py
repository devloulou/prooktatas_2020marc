karcsi = { "tanulo":"Horváth Károly",
         "beadando" : [80, 50, 40, 20],
         "vizsga" : [75, 75],
         "labor" : [78.20, 77.20]
       }


jani = { "tanulo":"Potter János",
          "beadando" : [82, 56, 44, 30],
          "vizsga" : [80, 80],
          "labor" : [67.90, 78.72]
        }


denes = { "tanulo" : "Neumann Dénes",
          "beadando" : [77, 82, 23, 39],
          "vizsga" : [78, 77],
          "labor" : [80, 80]
        }


emese = { "tanulo" : "Morvai Emese",
         "beadando" : [67, 55, 77, 21],
         "vizsga" : [40, 50],
         "labor" : [69, 44.56]
       }


tomi = { "tanulo" : "Kiss Tamás",
        "beadando" : [29, 89, 60, 56],
        "vizsga" : [65, 56],
        "labor" : [50, 40.6]
}


def sulyozott_atlag_beadando(tanulo):
    return (sum(tanulo["beadando"]) / len(tanulo["beadando"]))*0.1

def sulyozott_atlag_vizsga(tanulo):
    return (sum(tanulo["vizsga"]) / len(tanulo["vizsga"]))*0.7

def sulyozott_atlag_labor(tanulo):
    return (sum(tanulo["labor"]) / len(tanulo["labor"]))*0.2

def atlag_pontszam(tanulo):
    tanulo_neve = tanulo["tanulo"]
    atlag_pontszam =  sulyozott_atlag_beadando(tanulo) + sulyozott_atlag_vizsga(tanulo) + sulyozott_atlag_labor(tanulo)
    print(f"{tanulo_neve} átlag pontszáma: {atlag_pontszam}")
    return atlag_pontszam

def tanulo_eredmenye(tanulo):
    tanulo_neve = tanulo["tanulo"]
    if atlag_pontszam(tanulo) >= 90:
        eredmeny = 5
    elif atlag_pontszam(tanulo) >= 80 and atlag_pontszam(tanulo)<90:
        eredmeny = 4
    elif atlag_pontszam(tanulo) >= 70 and atlag_pontszam(tanulo) <80:
        eredmeny = 3
    elif atlag_pontszam(tanulo) >= 60 and atlag_pontszam(tanulo) <70:
        eredmeny = 2
    else:
        eredmeny = 1

    print(f"{tanulo_neve} eredménye: {eredmeny}")

    return tanulo_eredmenye


atlag_pontszam(denes)
tanulo_eredmenye(denes)