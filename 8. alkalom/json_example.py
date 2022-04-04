import json

file_location = r"C:\WORK\Prooktatás\Prooktatas\8. alkalom\first_json.json"

with open(file_location, 'r', encoding="utf-8") as file_obj:
    data = json.load(file_obj)

data['prooktatás'] = "python kurzus"

with open('test.json', 'w', encoding="utf-8") as file_obj:
    json.dump(data, file_obj, ensure_ascii=False, indent=4)


json_formatted_string = json.dumps(data)

with open("formatted_json.json", 'w') as file_obj:
    json.dump(json_formatted_string, file_obj)

print(data)
print("########################")
print(json_formatted_string)

print("########################")

my_dict= {"kulcs": "ertek"}

print(my_dict)


print('Józsi """""')
print("'90-es években")
my_list = [10, 10, 10]
############################


my_data = json.loads(json_formatted_string)

print(my_data)