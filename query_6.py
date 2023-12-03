import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

group_id = 1  # Замініть на відповідне значення

query = f'''
    SELECT students.id, students.student_name
    FROM students
    WHERE students.group_id = {group_id}
    ORDER BY students.student_name;
'''

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(f"Student ID: {row[0]}, Student Name: {row[1]}")

conn.close()
