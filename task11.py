import os
import json

if not os.path.exists('students.json'):
    with open('students.json', 'w') as f:
        json.dump([], f, indent=4)
    print("students.json fayli yaratildi.")
else:
    print("Fayl allaqachon mavjud.")
