import json

with open('students.json', 'r') as f:
    students = json.loads(f)

top_student = max(students, key=lambda x: x['age'])
print(f"Eng katta yoshli talaba: {top_student['name']} {top_student['surname']} - {top_student['age']} yosh")
