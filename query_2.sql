-- query_2.sql
SELECT students.id, students.student_name, AVG(grades.grade) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 1  -- Замініть на відповідне значення
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 1;
