import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

group_id = 1  # Замініть на відповідне значення
subject_id = 1  # Замініть на відповідне значення

query = f'''
    SELECT students.id, students.student_name, grades.grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE students.group_id = {group_id}
      AND subjects.id = {subject_id}
    ORDER BY students.student_name;
'''

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(f"Student ID: {row[0]}, Student Name: {row[1]}, Grade: {row[2]}")

conn.close()
