import json

with open('students.json', 'r') as f:
    students = json.load(f)

avg = sum(s['age'] for s in students) / len(students)
print(f"O‘rtacha yosh: {avg}")
