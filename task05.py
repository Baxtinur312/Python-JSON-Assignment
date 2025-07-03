import json

with open('students.json', 'r') as f:
    students = json.load(f)

for student in students:
    if student['age'] > 20:
        print(f"{student['name']} - {student['age']} yosh")
