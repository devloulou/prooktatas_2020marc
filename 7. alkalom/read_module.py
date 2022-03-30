import os

print(__file__)
folder_path = os.path.dirname(__file__)
print(folder_path)

file_path = folder_path + '\'' + 'Dracula.txt'
file_path = f"{folder_path}\Dracula.txt"

file_path = os.path.join(folder_path, 'Dracula.txt')
print(file_path)

#file_path = r"C:\WORK\Prooktatás\Prooktatas\7. alkalom\Dracula.txt"

def read_data():
    f = open(file_path, 'r')
    my_data = f.readlines()
    f.close()

    return my_data

# ebből csináljunk majd generátor függvényt
# nagy file-ok kezelése
def read_data_by_line():
    f = open(file_path, 'r')
    my_data = []

    for item in f.readlines():
        print(item)
        my_data.append(item)    
    f.close()
    return my_data

def write_to_file(file_location):
    my_list = ['Ricsi', '\n', 'ZOli', '\n', 'Karcsi', '\n', 'Peti']
    f = open(file_location, 'w')
    f.writelines(my_list)
    for item in my_list:        
        f.write(item + '\n') # csúnya módszer
        
    f.close()



if __name__ == '__main__':
    write_to_file('test.txt')

    exit()
    read_data_by_line()

    data = read_data()

    print(len(data))
    print(data[-1])



