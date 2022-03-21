# dictionary

# kulcs - érték párok vannak benne

my_dict = {
    "auto": "BWM",
    "color": "fehér",
    "motor_type": "benzin"
}

my_dict['auto']

for item in my_dict:
    print(my_dict[item])

print(my_dict.get('utasok_szama'))

print("###################################")

for key, value in my_dict.items():
    print(f"{key} - {value}")

print("###################################")

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
print("###################################")

print(type(4))
print(type("Ricsi"))
print(type([]))
print("###################################")

for key, value in my_dict.items():
    if key == 'bank':
        if type(value) == list: # vagy tuple
            pass
        if type(value) == dict:
            pass

##############################################
# listákkal, dictionary-vel, if-else ágakkal és a for ciklussal kapcsolatban

# comprehension műveletek
# függvények alapjai