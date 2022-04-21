import os
import json

folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'books')


# test = "C:\\WORK\\Prooktatás\\Prooktatas\\13. alkalom\\books\\A Tale of Two Cities.txt"
# os.path.join(os.path.dirname(os.path.dirname(__file__)), 'books') ==  C:\WORK\Prooktatás\Prooktatas\13. alkalom\books
#C:\WORK\Prooktatás\Prooktatas\13. alkalom\books\A Tale of Two Cities.txt

def get_book_list():
    books = []
    
    if not os.path.exists(folder_path):
        raise FileNotFoundError("A megadott elérési útvonal nem létezik")
        
    for item in os.listdir(folder_path):
       books.append(folder_path + '\\' + item)

    return books

def get_data_from_txt(file_location):
    if not os.path.exists(file_location):
        return False, f"A megadott file nem található: {file_location}"

    with open(file_location, "r", encoding="utf-8") as f:
        data = f.read()

    return data


def write_json(file_location, json_data):
    folder = os.path.dirname(file_location)
    if not os.path.exists(folder):
        return False, f"A megadott mappa nem található: {folder}"

    with open(file_location, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    return True


if __name__ == "__main__":
    test = get_book_list()
    
    # data = get_data_from_txt(test[0])

    # print(data[0:1500])

    data = get_data_from_txt(r"C:\WORK\Prooktatás\Prookttas\books\Dracula.txt")
    print(data)

    write_json('test.json', {"kulcs": "érték"})
    # print(data)
    # print(__file__)
    # print(os.path.dirname(__file__).replace('utils', 'books'))
    #print(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'books'))

    # __file__ változó: az aktuálisan használt file- elérési útját adja nekem vissza stringként
    # os.path.dirname() függvény visszaadja egy file vagy mappa melyik mappában van
    # pl: print(os.path.dirname(r"C:\WORK\Prooktatás\Prooktatas\books\Dracula.txt")) 
    # os.path.dirname(__file__) -> ez visszaadja annak a mappának az elérési útját, amelyik file-.t használjuk / futtatjuk
    # os.path.dirname(os.path.dirname(__file__) -> az előző kifejezés során visszakapott elérési útvonal
                                                # előtti mappának az elérési útvonalát adja vissza
    

    # print(os.path.dirname(os.path.dirname(__file__)))
    # print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))