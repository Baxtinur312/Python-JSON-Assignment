import json

with open('students.json', 'r') as f:
    students = json.load(f)

students.append({"name": "Shahzoda", "surname": "Nazarova", "age": 22})

with open('students.json', 'w') as f:
    json.dump(students, f, indent=4)
