my_dict = {

    "bank": {
        "new_positions": [
            {
                "position_name": "Junior Developer",
                "salary": 650000
            },
            {
                "position_name": "Senior Developer",
                "salary": 1300000
            }
        ]
    },

    "startup": {
        "new_positions": [
            {
                "position_name": "Junior Developer",
                "salary": 850000
            },
            {
                "position_name": "Senior Developer",
                "salary": 1600000
            }
        ]
    }

}

print(my_dict.keys())

# my_dict['bank']['new_positions'][1]['salary'] *= 1.15 

# print(my_dict['bank']['new_positions'][1]['salary'])



# items() -> visszaadja a kulcs - érték párt egy tuple-ben
print("########################################")
for key, value in my_dict.items():
    if key == 'bank':
        for idx, item in enumerate(value['new_positions']):
            print(f"{idx} - {item}")
            item['salary'] = item['salary'] * 1.15

# ciklusokat lehet egymás ágyazni

print("########################################")

print(my_dict['bank'])

my_list = [1,2,3,4]

# ciklusváltozót megváltoztatom, az nincs hatással a listára

# for(int x=0; x > 10; x++) {

# }


for idx, item in enumerate(my_list):
    #item = item * 2
    item *= 2
    my_list[idx] *= 2

print(my_list)

print("########################################")

# hogyan lehet vezérelni a for ciklusokat

# a ciklust meg lehet állítani - a futása ilyenkor befejeződik: break
# a ciklusokat tovább lehet léptetni: continue

my_list = [1,2,3,4]

for item in my_list:
    if item == 3:
        break    
    print(f" az {item} duplája: {item*2}")

print("########################################")

for item in my_list:
    if item == 3:
        continue
    print(f" az {item} duplája: {item*2}")

#######################################################################################
print("########################################")

my_list = []
for i in range(0, 5):
    my_list.append(i+1)

print(my_list)

# comprehension művelet - list comprehension

# inplace hozunk létre változót értékekkel
my_list = [num for num in range(0, 5)]

# list, comprehension-nek, listanak, tuple-nek, dict-nek: memóriába tart minden adatot, kiértékelve

# for ciklus esetén pedig hozzá fűzunk meglévő listához értéket
for i in range(0, 5):
    my_list.append(i+1)


my_list = [num + 1 for num in range(0, 1000000)]

# generator comprehension
my_obj = (num + 1 for num in range(10, 1000000))


print(my_list.__sizeof__())
print(my_obj.__sizeof__())
print("########################################")

print(next(my_obj))
print(next(my_obj))
print(next(my_obj))
print(next(my_obj))
print(next(my_obj))
print(next(my_obj))
print(next(my_obj))
print(next(my_obj))

print("########################################")

cnt = 0
for item in my_obj:
    cnt += 1
    print(item)

    if cnt == 50:
        break