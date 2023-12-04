-- query_10.sql
SELECT subjects.id, subjects.subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = 1  -- Замініть на відповідне значення
  AND subjects.teacher_id = 1  -- Замініть на відповідне значення
ORDER BY subjects.subject_name;
