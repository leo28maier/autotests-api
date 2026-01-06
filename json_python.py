import json
from xml.etree.ElementTree import indent

json_data = '{"name": "Ivan", "age": 30, "is_student": false}'
parsed_json = json.loads(json_data)
print(parsed_json, type(parsed_json))

data = {
    'name': 'Ivan',
    'age': 30,

    'is_student': False
}

json_data = json.dumps(data, indent=4)
print(json_data)



with open('Json_example.json', 'r', encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data, type(data))


with open('Json_user.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)