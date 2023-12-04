-- query_5.sql
SELECT subjects.id, subjects.subject_name
FROM subjects
WHERE subjects.teacher_id = 1  -- Замініть на відповідне значення
ORDER BY subjects.subject_name;
