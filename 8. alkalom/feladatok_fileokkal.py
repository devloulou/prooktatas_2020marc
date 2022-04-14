
# kontextusmanager - erőforrás management
# fileobjektumok, adatabázis kapcsolatok
# kontextusmanager - with

file_path = r"C:\WORK\Prooktatás\Prooktatas\8. alkalom\Dracula.txt"

with open(file_path, "r") as f:
    data = f.read()

#print(data[0:1000])

# file kiiras
with open('pelda.txt', 'w') as kiscica:
    kiscica.write('Ez egy teszt sor')