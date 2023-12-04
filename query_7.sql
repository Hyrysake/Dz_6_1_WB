-- query_7.sql
SELECT students.id, students.student_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = 1  -- Замініть на відповідне значення
  AND subjects.id = 1  -- Замініть на відповідне значення
ORDER BY students.student_name;
