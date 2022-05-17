import string
import random

abc = string.ascii_letters

#print(abc)

my_list = []
my_string2 = ""

for i in range(10):
    my_string = random.choice(abc)
    my_list.append(my_string)
    my_string2 += my_string

print(my_list)
print(my_string2)

my_string3 = "".join(my_list)

print(f"my_string3: {my_string3}")