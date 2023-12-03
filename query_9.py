import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

student_id = 1  # Замініть на відповідне значення

query = f'''
    SELECT subjects.id, subjects.subject_name
    FROM subjects
    JOIN grades ON subjects.id = grades.subject_id
    WHERE grades.student_id = {student_id}
    ORDER BY subjects.subject_name;
'''

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(f"Subject ID: {row[0]}, Subject Name: {row[1]}")

conn.close()
