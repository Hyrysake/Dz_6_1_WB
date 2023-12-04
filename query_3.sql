-- query_3.sql
SELECT groups.id as group_id, groups.group_name, AVG(grades.grade) as average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 1  -- Замініть на відповідне значення
GROUP BY groups.id
ORDER BY average_grade DESC;
