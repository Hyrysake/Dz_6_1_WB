import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

subject_id = 1 # Замініть на відповідне значення предмету
query = '''
    SELECT student_id, AVG(grade) AS average_grade
    FROM grades
    WHERE subject_id = :subject_id
    GROUP BY student_id
    ORDER BY average_grade DESC
    LIMIT 1;
'''

cursor.execute(query, {'subject_id': subject_id})
result = cursor.fetchall()

for row in result:
    print(f"Student ID: {row[0]}, Average Grade: {row[1]}")

conn.close()
