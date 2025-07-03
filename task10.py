import json

with open('students.json', 'r') as f:
    students = json.load(f)

sorted_students = sorted(students, key=lambda x: x['age'])
for student in sorted_students:
    print(f"{student['name']} - {student['age']} yosh")
