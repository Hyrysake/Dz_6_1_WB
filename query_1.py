import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

query = '''
    SELECT students.id, students.student_name, AVG(grades.grade) as average_grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    GROUP BY students.id
    ORDER BY average_grade DESC
    LIMIT 5;
'''

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(f"Student ID: {row[0]}, Student Name: {row[1]}, Average Grade: {row[2]}")

conn.close()
