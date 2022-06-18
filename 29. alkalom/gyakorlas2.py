# egy olyan függvényt, amely a duplikált elemek összes előfordulását törli
my_list = ['apple', 'banana', 'melon', 'apple', 'orange', 'tomato', 'orange', 'plum']

def my_func(my_list):
    my_list2 = []
    for item in my_list:
        if my_list.count(item) == 1:
            my_list2.append(item)

    return my_list2


my_list = my_func(my_list)
#print(my_list)

my_list = ['apple', 'banana', 'melon', 'apple', 'orange', 'tomato', 'orange', 'plum']

from collections import Counter

my_c = Counter(my_list)



def my_func(my_list):
    from collections import Counter
    my_c = dict(Counter(my_list))

    for key, value in my_c.items():
        if value > 1:
            for _ in range(value):
                my_list.remove(key)

    return my_list


my_func(my_list)

# print(my_list)

#####################
# 3. feladat: Írjatok egy olyan függvényt, amely 
# lehetőséget teremt arra, hogy tetszőleges mennyiségű és típusú email címet hozzá tudjunk adni.
# a feladat során gondoljatok arra, hogy első futás során nincs még email, a többi futásnál pedig már lesz email adat.

#     "email_addresses": [
#       {"type": "business", "email": "business@email.com"},
#       {"type":  "private", "email": "private@email.com"}    
#   ]


my_dict ={
    "firstName": "Rack",
    "lastName": "Jackon",
    "gender": "man",
    "age": 24,
    "address": {
        "streetAddress": "126",
        "city": "San Jone",
        "state": "CA",
        "postalCode": "394221"
    },
    "phoneNumbers": [
        { "type": "home", "number": "7383627627" }
    ]
}

def add_email(email):
    if not my_dict.get('email_addressess'):
        if type(email) == dict:
            my_dict['email_addressess'] = [email]
        elif isinstance(email, list):
            my_dict['email_addressess'] = email
    else:
        if isinstance(email, dict):
            my_dict['email_addressess'].append(email)        
        elif isinstance(email, list):
            my_dict['email_addressess'].extend(email)

test_emails = [
      {"type": "business", "email": "business@email.com"},
      {"type":  "private", "email": "private@email.com"}    
  ]
add_email(test_emails)


add_email(test_emails)


print(my_dict)