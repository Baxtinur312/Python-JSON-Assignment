import json

students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]

with open('students.json', 'w') as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
