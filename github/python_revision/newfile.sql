-- CREATE DATABASE test_01;
-- \C test_01;

-- CREATE TABLE IF NOT EXISTS public."transaction_log_loyalty" (
    -- id int,
    -- user_id int,
    -- loyalty_id varchar,
    -- bill_number varchar,
    -- modified_bill_number varchar,
    -- txn_date varchar,
    -- txn_time varchar,
    -- store_id int,
    -- amount varchar,
    -- discount varchar,
    -- tax_amount varchar,
    -- points_collected varchar,
    -- points_spent varchar,
    -- points_used varchar,
    -- points_available varchar,
    -- points_lapsed varchar,
    -- bill_outlier_status varchar,
    -- is_migrated varchar,
    -- visit_rank varchar,
    -- insertion_date varchar,
    -- insertion_time varchar,
    -- modified_date varchar,
    -- modified_time varchar,
    -- created_by varchar,
    -- modified_by varchar,
    -- days_since_last_visit varchar,
    -- id_ int,
    -- store_code int,
    -- store_name varchar,
    -- zone varchar,
    -- brand varchar,
    -- concept varchar,
    -- address varchar,
    -- state varchar,
    -- city varchar,
    -- Pin varchar,
    -- manager varchar,
    -- contact_no varchar,
    -- store_type varchar,
    -- is_active varchar,
    -- opening_date varchar,
    -- closing_date varchar,
    -- region varchar,
    -- insertiondate varchar
-- );

-- \copy <table_name> from '</path/to/file/filename.csv>' delimiter ',' CSV HEADER;
\! cls

-- ALTER TABLE transaction_log_loyalty ALTER COLUMN store_code TYPE VARCHAR;

-- \copy transaction_log_loyalty FROM 'E:\\transaction_log_loyalty.csv' DELIMITER '|' CSV HEADER;

-- SELECT 
-- id,
-- user_id,
-- loyalty_id, 
-- bill_number,
-- modified_bill_number,
-- txn_date FROM transaction_log_loyalty LIMIT 5;

-- SELECT sum(id) as id_Sum from transaction_log_loyalty;
-- SELECT avg(id) as id_avg from transaction_log_loyalty;
-- SELECT count(bill_number) as no_of_bill from transaction_log_loyalty;
-- CREATE PROCEDURE insert_data(   
--     id int,user_id int,loyalty_id varchar,bill_number varchar,modified_bill_number varchar,txn_date varchar,txn_time varchar,store_id int,amount varchar,
--     discount varchar,tax_amount varchar,points_collected varchar,points_spent varchar,points_used varchar,points_available varchar,points_lapsed varchar,
--     bill_outlier_status varchar,is_migrated varchar,visit_rank varchar,insertion_date varchar,insertion_time varchar,modified_date varchar,modified_time varchar,created_by varchar,
--     modified_by varchar,days_since_last_visit varchar,id_ int,store_code int,store_name varchar, zone varchar,
--     brand varchar,concept varchar,address varchar,state varchar,city varchar,Pin varchar,manager varchar,contact_no varchar,store_type varchar,is_active varchar,opening_date varchar,
--     closing_date varchar,region varchar,insertiondate varchar)
-- LANGUAGE sql
-- BEGIN ATOMIC
--   INSERT INTO transaction_log_loyalty VALUES (id,user_id,loyalty_id,bill_number,modified_bill_number,txn_date,txn_time,store_id,amount,
--     discount,tax_amount,points_collected,points_spent,points_used,points_available,points_lapsed,
--     bill_outlier_status,is_migrated,visit_rank,insertion_date,insertion_time,modified_date,modified_time,created_by,
--     modified_by,days_since_last_visit,id_,store_code,store_name, zone,
--     brand,concept,address,state,city,Pin,manager,contact_no,store_type,is_active,opening_date,
--     closing_date,region,insertiondate);
-- END;
-- CALL insert_data(123,456,'444636','234','rtu45','20-12-2022','3:00',3456,'500.00',
--     '50','234','45','456','34','23','12',
--     '234',NULL,'23,24-02-2022','3:45','22-03-2022','4:00','4567',
--     '23-3-45',03,24,34,'milan', 'mumbai',
--     'clothes','fashion','gondia','mh','gindia','368316','ravi','65218585','fashion','TRue','23-4-2018',
--     '23-04-23','mumbai','23-03-2018'
--     );
-- CREATE OR REPLACE PROCEDURE get_txn()
-- LANGUAGE SQL
-- BEGIN ATOMIC
--    SELECT * from transaction_log_loyalty where id=1706;
-- END;


-- CALL get_txn();
-- CREATE OR REPLACE FUNCTION fx()
-- RETURNS SETOF transaction_log_loyalty AS $$
-- BEGIN
--   RETURN QUERY SELECT * FROM transaction_log_loyalty;
-- END
-- $$ LANGUAGE plpgsql;

-- SELECT * FROM fx();
CREATE OR REPLACE PROCEDURE get_employee_details(a INTEGER)
AS $$
BEGIN
  SELECT * FROM transaction_log_loyalty WHERE id = a;
END;
$$ LANGUAGE plpgsql;

CALL get_employee_details(1706)


