/*markdown
### Employees Table
*/

-- Create Database for employees

CREATE DATABASE IF NOT EXISTS company_db;

-- Use Database

USE company_db;

-- Create Table Department

CREATE TABLE IF NOT EXISTS department (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(255)
);


-- Create Table Employees

CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(255),
    location VARCHAR(255),
    phone_number VARCHAR(255),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

-- Insert Data

INSERT INTO department (dept_name)
VALUES 
    ("Frontend"),
    ("Backend"),
    ("DevOps"),
    ("QA"),
    ("UI/UX");

INSERT INTO employees (emp_name, location, phone_number, dept_id)
    VALUES
    ("Mohamed", "Cairo", "01064447777", 1),
    ("Ahmed", "Giza", "01063336666", 2),
    ("Sara", "Alexandria", "01062225555", 3),
    ("Omar", "Cairo", "01061114444", 4),
    ("Nour", "Mansoura", "01065558888", 5),
    ("Hana", "Cairo", "01060001111", 1),
    ("Youssef", "Giza", "01069992222", 2),
    ("Mariam", "Alexandria", "01067773333", 3),
    ("Ali", "Cairo", "01068884444", 4),
    ("Layla", "Mansoura", "01066665555", 5);



/*markdown
#### Q1 : Write a SQL query to retrieve all columns from a table named employees
*/

-- Get Columns Names
DESCRIBE employees;

-- Get All Values
SELECT * FROM employees;

/*markdown
#### Q2 : Write a SQL query to retrieve the emp_id, emp_name, and dept_id from the employees table, where the location is 'Cairo'.
*/

SELECT 
    emp_id, emp_name, dept_id
FROM
    Employees
WHERE
    location = 'Cairo';

/*markdown
#### Q3: Write a SQL query that displays distinct dept_id values from the employees table
*/

SELECT DISTINCT dept_id from employees;

/*markdown
#### Q4: Write a SQL query to create a table students with the following columns: 
- ID (Primary Key), 
- First_Name (not null), 
- Last_Name (default 'Unknown'), 
- Address (default 'N/A'), 
- City (default 'N/A')
- Birth_Date.

*/

CREATE TABLE IF NOT EXISTS students (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(255) NOT NULL,
    Last_Name  VARCHAR(255) DEFAULT 'Unknown',
    Address    VARCHAR(255) DEFAULT 'N/A',
    City       VARCHAR(255) DEFAULT 'N/A',
    Birth_Date DATE
);

/*markdown
#### Q5 : Write a SQL query to drop the students table
*/

DROP TABLE students;

/*markdown
#### Q7: Write a SQL query to insert the following values into the students table: ('Ahmed', 'Ali', 'Downtown', 'Cairo', '1995-01-01')
*/

INSERT INTO students (First_Name, Last_Name, Address, City, Birth_Date)
VALUES
    ('Ahmed', 'Ali', 'Downtown', 'Cairo', '1995-01-01'),
    ('Sara', 'Hassan', 'Garden City', 'Cairo', '1996-03-12'),
    ('Omar', 'Khalid', 'Maadi', 'Cairo', '1994-07-22'),
    ('Mariam', 'Youssef', 'Alexandria Corniche', 'Alexandria', '1997-05-05'),
    ('Youssef', 'Mohamed', 'Giza', 'Giza', '1995-11-11'),
    ('Ali', 'Ahmed', 'Downtown', 'Cairo', '1995-01-01');

INSERT INTO students (First_Name, Birth_Date)
VALUES
    ('Ali', '2000-01-01'),
    ('Sara', '1999-05-15'),
    ('Omar', '2001-07-22');

/*markdown
#### Q8: Write a SQL query to update the Address of the student with Last_Name = 'Ahmed' to 'Garden City'
*/

UPDATE students set Address= 'Garden City' WHERE Last_Name = 'Ahmed';

SELECT * from students;

/*markdown
#### Q9: Write a SQL query to delete the rows from the students table where City is 'Cairo', and then rollback the transaction.
*/

-- on Workbench
--      Run all
-- On Sql Notebook
--      Run Each Line Seperately

START TRANSACTION;

-- Just Disable Safe Update As DELETE Safe mode is restricted to Primary Keys

SET SQL_SAFE_UPDATES = 0;

-- Delete Query

DELETE FROM students WHERE City = 'Cairo';

-- Activate It Again

SET SQL_SAFE_UPDATES = 1;

-- Preview Before RollBack

SELECT * FROM students;

-- Rollback (if to save it we use COMMIT)

ROLLBACK;

