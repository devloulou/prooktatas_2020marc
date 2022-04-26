# Guess the Number:
# 3 próbálkozásra  kell kitalálni
# 1-10 lehet számra gondolni: minden esetben a gép fogja a számot megálmodni


# 1. be kell kérni számokat -> 1- 10-ig adjunk számokat
# 2. a számítógépnek kell generálnia egy számot 1-10 között
# 3. 3 próbálkozás lehet csak: 
# 4. logikai vizsgálat a szám egyezésre
# 5. hibakezelés??

import random

def get_the_number(nums):
    return random.randint(nums[0], nums[1])

def game(my_try, nums):
    print(f"Gondoltam egy számra! {my_try} próbálkozásod van eltalálni!")
    secret_number = get_the_number(nums)

    game_on = True
    run_cnt = 0

    while game_on:
        run_cnt += 1
        my_num = input("Kérem add meg a számot: ")

        try:
            my_num = int(my_num)

            if nums[0] > my_num or my_num > nums[1]:
                raise 

            if secret_number == my_num:
                print(f"Gratulálok! Eltaláltad a számot! {secret_number}")
                game_on = False
            else:
                if run_cnt == my_try:
                    print(f"Sajnos nem találtad el a számot {run_cnt} próbálkozásból!")
                    print(f"A szám a következő lett volna: {secret_number}")
                    game_on = False
        except Exception as e:
            print("Nem számot adtál meg vagy nem jó számot adtál meg!")
            run_cnt -= 1


if __name__ == '__main__':
    game(5, (1, 10))
    # test_num = get_the_number()
    # print(test_num)