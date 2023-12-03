import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

subject_id = 1  # Замініть на відповідне значення

query = f'''
    SELECT groups.id as group_id, groups.group_name, AVG(grades.grade) as average_grade
    FROM groups
    JOIN students ON groups.id = students.group_id
    JOIN grades ON students.id = grades.student_id
    WHERE grades.subject_id = {subject_id}
    GROUP BY groups.id
    ORDER BY average_grade DESC;
'''

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(f"Group ID: {row[0]}, Group Name: {row[1]}, Average Grade: {row[2]}")

conn.close()
