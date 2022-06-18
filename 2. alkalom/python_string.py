# my_str1 = "ricsi"
# my_str2 = 3

# # str

# print(my_str1 + str(my_str2) + my_str1 + str(my_str2) + my_str1 + str(my_str2)) # string concatenációnak



my_string = "Ricsi vagyok"
my_age = 32

# print(my_age)

# print(my_string + " és " + hex(my_age) + " éves")


# 4 módszert fogunk megnézi a string formázásra

# 1. "régi" string formatting: %

my_num = 50159747054
name = "Ricsi"

print("Név: %s" % my_num)

print("Név: %s, hexadecimal: %x" % (name, my_num))
print("Név: %(name)s, hexadecimal: %(my_num)x" % {'name': name, 'my_num': my_num})
####################################################################################
# 2. "New Style" string formatting: str.format
my_age = 32
my_name = "Ricsi"

# Ricsi vagyok és 32 éves
print("print -------------------")
print("{name:s} vagyok és {age:x} éves".format(name=my_name, age=my_age))

################################################################################
# 3. String interpoláció / f-string

age = 32
my_name = "Ricsi"

print(f"{my_name} vagyok és {age} éves")


# 4. Template Strings
from string import Template

my_template = Template('$name vagyok és $age éves')

test = my_template.substitute(name=name, age=age)

print(test)