 \c covid_data
 CREATE TABLE IF NOT EXISTS public."teacher"(teacher_id int, subject_id int, dept_id int);

 \copy teacher FROM 'C:\\Users\\ravir\\Downloads\\task 12-05-2023 dataset - Google Sheets.csv' DELIMITER ',' CSV HEADER;
 SELECT teacher_id, COUNT(DISTINCT subject_id) as cnt FROM teacher GROUP BY teacher_id;