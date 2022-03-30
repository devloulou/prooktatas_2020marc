# file művelet alapjai

# 1. lépés: meg kell nyitni a file-t
#   - különböző megnyitási típusok vannak
# 2. lépés:
#   - attól függ, hogy írni, vagy  olvasni akarunk
#   - ha olvasni akarunk, ki kell olvasni az adatot a file-ból
#   - ha írni akarunk, akkor meg bele kell írni az adatot - bele dump-olni
# 3. lépés:
#   - minden esetben le kell zárni a filet a program futása után / során


# sortörés: \n
file_path = r"C:\WORK\Prooktatás\Prooktatas\7. alkalom\Dracula.txt"
f = open(file_path, 'r')

my_data = f.read()

# vizsgáljuk meg a my_data változót
print(type(my_data))

print(my_data[0:1500])

f.close()

################################################################

def read_data():
    f = open(file_path, 'r')
    my_data = f.readlines()
    f.close()

    return my_data

