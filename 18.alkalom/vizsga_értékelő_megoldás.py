# Egyetemi féléves értékelő: írjatok egy olyan programot - függvények segíségével - ,
# amely az alábbi tanulók féléves jegyét meghatározza.
# Az értékelésnél a következő szabályokat kell betartani:

## a beadando a jegy 10%-át adja
## a vizsga a jegy 70%-át
## a labor gyakorlat pedig a jegy 20%-át

# Az eredmények a következők szerint kell meghatározni
# 90 - 100 => 5
# 80 - 89 => 4
# 70 - 79 => 3
# 60 - 69 => 2
# 0  - 59 => 1

# példa az elvárt eredményre:
#
#
# kriszta = { "tanulo":"Kriszta",
#          "beadando" : [70, 60, 30, 10],
#          "vizsga" : [70, 75],
#          "labor" : [68.20, 77.20]
#        }
# (ez egy lekalkulált eredmény)
# Kriszta
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# Kriszta átlag pontszáma: 69.54
# Kriszta tanuló eredménye: 2

# 2. feladat: az osztály átlag eredményeit is határozzátok meg:
# példa outputra:
#
# Osztály átlag pontszáma 72.79
# Osztály eredménye 3


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

osztaly = [karcsi, jani, denes, emese, tomi]

def get_result(point):
    if point >= 90:
        return 5
    elif point >= 80 and 90 > point:
        return 4
    elif point >= 70 and 80 > point:
        return 3
    elif point >= 60 and 70 > point:
        return 2
    else:
        return 1

def create_point_from_student(student):
        return avg(student['beadando']) * 0.1 + avg(student['vizsga']) * 0.7 + avg(student['labor']) * 0.2

def avg(points_list):    
    return sum(points_list)/len(points_list)

def class_results(class_list):
    point = 0
    for student in class_list:
        point += create_point_from_student(student)

    result = get_result(round(point/len(class_list), 2))
    print(f"Az osztály átlag pontszáma: {round(point/len(class_list), 2)} \n Érdemjegy: {result}")


if __name__ == '__main__':
    for student in osztaly:
        point = create_point_from_student(student)
        result = get_result(point)
        print(f" {student['tanulo']} pontszáma: {point}\n Érdemjegy: {result}")

        print("####################")

    class_results(osztaly)