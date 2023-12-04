-- query_6.sql
SELECT students.id, students.student_name
FROM students
WHERE students.group_id = 1  -- Замініть на відповідне значення
ORDER BY students.student_name;
