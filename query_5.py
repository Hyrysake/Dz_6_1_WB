import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

teacher_id = 1  # Замініть на відповідне значення

query = f'''
    SELECT subjects.id, subjects.subject_name
    FROM subjects
    WHERE subjects.teacher_id = {teacher_id}
    ORDER BY subjects.subject_name;
'''

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(f"Subject ID: {row[0]}, Subject Name: {row[1]}")

conn.close()
