import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

teacher_id = 1  # Замініть на відповідне значення

query = f'''
    SELECT AVG(grades.grade) as average_grade
    FROM grades
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.teacher_id = {teacher_id};
'''

cursor.execute(query)
result = cursor.fetchone()

print(f"Average Grade by Teacher ID {teacher_id}: {result[0]}")

conn.close()
