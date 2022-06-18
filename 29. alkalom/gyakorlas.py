# shallow copy - deep copy
import copy

my_list = [1, 2, 3, 4, 5]

my_list2 = copy.copy(my_list)

my_list3 = my_list

my_list4 = [item for item in my_list]


######

# print(id(my_list))
# print(id(my_list2))
# print(id(my_list3))
# print(id(my_list4))

my_list = [1, 2, [3, 4, 5]]
my_list2 = copy.copy(my_list) # shallow copy
my_list4 = [item for item in my_list]

my_list[2][0] = "Ricsi"
my_list[0] = "Pisti"

# print(my_list)
# print(my_list4)
# print(my_list2)


my_list = [1, 2, [3, 4, 5]]
my_list2 = copy.deepcopy(my_list) # deep copy
my_list4 = [item for item in my_list]

my_list[2][0] = "Ricsi"
my_list[0] = "Pisti"

# print(my_list)
# print(my_list4)
# print(my_list2)




###################################################################
# eval
a = 10
b = 5

temp = eval("a*b/5==10")


my_dict = {
    1: {
        2: [
            {
                3: {
                    4: [
                        {"kulcs": "érték"}
                    ]
                }
            }
        ]
    }    
}

my_map = [
    {
        1: "[1]"
    },
    {
        2: "[1][2]"
    },
    {
        3: "[1][2][0][3]"
    },
    {
        4: "[1][2][0][3][4]"
    },
    {
        "kulcs": "[1][2][0][3][4][0]['kulcs']"
    }
]

print(my_dict[1][2])

for item in my_map:
    for key, value in item.items():
        try:
            temp = eval(f"my_dict{value}")
            print(temp)
        except:
            print(f"value: {value}")


print("----------------------")


temp = input()

print(eval(temp))