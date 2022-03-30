# minden python file hasznáéható modulként
# modulként úgy használunk egy file-t, hogy az import szó után
# a file nevét kiírjuk a kiterjesztés nélkül

# a modulként beimportált file-t a python végig scanneli
# mindne változó létehozást - értékadás - elvégez
# minden a modulban lévő függvényhívást elvégez
# minden cikluson - ami nem függvényben van deklarálva - végigmegy
# minden if -else ágat ellenőriz, kiértékel - ami nem függvényben van deklarálva -

def greetings(name):
    print(f"Hello, {name}!")

print("Sziasztok, ez egy print")

my_list = [1, 2, 3, 4, 5]

print(__name__)

if __name__ == '__main__':
    greetings('Mercédesz')
else:
    greetings('Mária')