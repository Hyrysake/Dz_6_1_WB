import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

query = '''
    SELECT AVG(grade) AS average_grade
    FROM grades;
'''

cursor.execute(query)
result = cursor.fetchone()

print(f"Average Grade across all students: {result[0]}")

conn.close()
