import json
import csv

with open('students.json', 'r') as f:
    students = json.load(f)

with open('students.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'surname', 'age'])
    writer.writeheader()
    writer.writerows(students)
