import json

with open('students.json', 'r') as f:
    students = json.loads(f)

print(f"Umumiy talabalar soni: {len(students)} ta")
