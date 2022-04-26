from utils.file_handler import get_book_list, get_data_from_txt, write_json, folder_path
import os

# van nekünk egy mappában x db txt file
# ezeket kell egyesével megvizsgálni
# és a feladatban leírt statisztikákat megcsinálni

def statistic_per_book():
    book_list = get_book_list()

    max_len = 0
    max_len_name = None

    min_len = 0
    min_len_name = None
    for idx, item in enumerate(book_list):
        # a basename az ha az elérési útvonal utolsó szintje
        # c:\WORK\Prooktatás\Prooktatas\13. alkalom\books\ [ez az utolsó elem]
        json_file_location = folder_path + '\\' + os.path.basename(item).replace(".txt", ".json")        
        json_file_location = folder_path + '\\' + item.split("\\")[-1].replace(".txt", ".json")

        data = get_data_from_txt(item)

        if idx == 0:
            min_len = len(data)
            min_len_name = item.split('\\')[-1][:-4]

        if len(data) > max_len:
            max_len = len(data)
            max_len_name = item.split('\\')[-1][:-4]

        if min_len > len(data):
            min_len = len(data)
            min_len_name = item.split('\\')[-1][:-4]    
        
        num_of_words = get_num_of_words(data)
        row_num = get_row_num_of_txt(data)
        page_num = get_page_num_of_txt(data)
        author, release_date = get_author_and_release_date(data)

        # hashmap hashtable - dictionary

        json_data = {
            "num_of_words": num_of_words,
            "row_num": row_num,
            "page_num": page_num,
            "author": author,
            "release_date": release_date
        }
        
        write_json(json_file_location, json_data)        

    # itt kell kiírni majd azokat a mérőszámokat, amelyek az összes 
    # könyv vizsgálatával kell elvégezni
    print(f"leghosszab könyv: {max_len_name} - hossza: {max_len}")
    print(f"legrövidebb könyv: {min_len_name} - hossza: {min_len}")

def get_num_of_words(txt_data):
    data_list = txt_data.split()

    cnt = 0
    for item in data_list:
        if len(item) > 2:
            cnt += 1
    return cnt
    

def get_row_num_of_txt(txt_data):
    data_list = txt_data.split("\n") 

    return len(data_list)

def get_page_num_of_txt(txt_data):
    return round(len(txt_data)/3000)


def get_author_and_release_date(txt_data):
    data_list = txt_data.split("\n") 

    author = None
    release_date = None

    for item in data_list:
        if 'Author:' in item:
            author = item
        if 'Release Date:' in item:
            release_date = item

        if author is not None and release_date is not None:
            break

    return author, release_date

if __name__ == "__main__":
    statistic_per_book()

    # Counter -> most_common