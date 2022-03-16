
my_list = [1, 2, 3, 4, 5]

print(my_list[0] > my_list[-1])

if my_list[-1] > my_list[0]:
    print(f"{my_list[-1]} nagyobb mint a {my_list[0]}")


if my_list[0] > my_list[-1]:
    print(f"{my_list[-1]} nagyobb mint a {my_list[0]}")
else:
    print("befutottam az else ágba")

############################################################
if my_list[0] > my_list[-1]:
    print(f"{my_list[-1]} nagyobb mint a {my_list[0]}")
elif my_list[-2] > my_list[0]:
    print(f"{my_list[-2]} nagyobb mint a {my_list[0]}")
elif my_list[1] > my_list[0]:
    print(f"{my_list[1]} nagyobb mint a {my_list[0]}")
else:
    print("befutottam az else ágba")

#############################################################

if my_list[0] > my_list[-1]:
    print(f"{my_list[-1]} nagyobb mint a {my_list[0]}")

if my_list[-2] > my_list[0]:
    print(f"{my_list[-2]} nagyobb mint a {my_list[0]}")

if my_list[1] > my_list[0]:
    print(f"{my_list[1]} nagyobb mint a {my_list[0]}")

# switch case következő óra

# ternary operátor

my_value = None

if 2 > 1:
    my_value = "Ricsi"
else:
    my_value = "Józsi"

print(my_value)

# ternary operátor -> a > b?10:20
my_value = "Ricsi" if 2 > 1 else "Józsi"

print(my_value)

print("következő utasítás")

# ciklusok
# listák ás dictionaryk bejárása ciklusokkal
# függvények