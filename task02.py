import json

with open('students.json', 'r') as f:
    students = json.load(f)

for student in students:
    print(f"{student['name']} - {student['age']} yosh")
