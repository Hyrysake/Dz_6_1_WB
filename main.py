import sqlite3
from faker import Faker

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створення таблиці груп
cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        group_name TEXT
    );
''')

# Створення таблиці викладачів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        teacher_name TEXT
    );
''')

# Створення таблиці предметів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        subject_name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    );
''')

# Створення таблиці студентів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        student_name TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups (id)
    );
''')

# Створення таблиці оцінок
cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date_received DATE,
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
    );
''')

# Заповнення таблиці груп даними
cursor.executemany('INSERT INTO groups (group_name) VALUES (?)', [('Group A',), ('Group B',), ('Group C',)])

# Заповнення таблиці викладачів даними
cursor.executemany('INSERT INTO teachers (teacher_name) VALUES (?)', [('Teacher 1',), ('Teacher 2',), ('Teacher 3',)])

# Заповнення таблиці предметів даними
fake = Faker()
subjects_data = [(fake.word(), teacher_id) for teacher_id in range(1, 4) for _ in range(5)]
cursor.executemany('INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)', subjects_data)

# Заповнення таблиці студентів даними
students_data = [(fake.name(), group_id) for group_id in range(1, 4) for _ in range(10)]
cursor.executemany('INSERT INTO students (student_name, group_id) VALUES (?, ?)', students_data)

# Заповнення таблиці оцінок даними
grades_data = [(student_id, subject_id, fake.random_int(min=60, max=100), fake.date_this_decade()) for student_id in range(1, 31) for subject_id in range(1, 16)]
cursor.executemany('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)', grades_data)

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()
