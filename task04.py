import json

name = input("Ism: ")
surname = input("Familiya: ")
age = int(input("Yosh: "))

with open('students.json', 'r') as f:
    students = json.loads(f)

students.append({"name": name, "surname": surname, "age": age})

with open('students.json', 'w') as f:
    json.dump(students, f, indent=4)
