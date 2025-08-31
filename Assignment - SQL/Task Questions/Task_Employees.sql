/*markdown
## Task Questions
*/

-- Create Database for employees

CREATE DATABASE IF NOT EXISTS company_employee_db;


-- Use Database

USE company_employee_db;



-- Create Table Department

CREATE TABLE IF NOT EXISTS department (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(255)
);



-- Create Table Employees

CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    fname VARCHAR(255) NOT NULL,
    lname VARCHAR(255) DEFAULT 'N/A',
    location VARCHAR(255),
    phone_number VARCHAR(255),
    hire_date DATE,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);



-- Create Table Project

CREATE Table IF NOT EXISTS project (
    p_id INT PRIMARY Key AUTO_INCREMENT,
    p_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);



-- Table Works On

CREATE Table IF NOT EXISTS works_on (
    proj_id INT,
    emp_id INT,
    hours int,
    FOREIGN KEY (proj_id) REFERENCES project(p_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    PRIMARY KEY (proj_id, emp_id)
);



-- Insert Data Department

INSERT INTO department (dept_name)
VALUES 
    ("Frontend"),
    ("Backend"),
    ("DevOps"),
    ("QA"),
    ("UI/UX");


-- insert data employees

INSERT INTO employees (fname, lname, location, phone_number, hire_date, dept_id)
VALUES
    ('Mohamed', 'Ali', 'Cairo', '01064447777', '2020-01-15', 1),
    ('Sara', 'Hassan', 'Giza', '01063336666', '2019-03-22', 2),
    ('Omar', 'Khalid', 'Alexandria', '01062225555', '2021-06-10', 3),
    ('Mariam', 'Youssef', 'Cairo', '01061114444', '2020-11-05', 4),
    ('Youssef', 'Mohamed', 'Mansoura', '01065558888', '2018-08-20', 5),
    ('Layla', 'Nabil', 'Cairo', '01060001111', '2022-02-18', 1),
    ('Hassan', 'Adel', 'Giza', '01069992222', '2017-09-12', 2),
    ('Noor', 'Sami', 'Alexandria', '01067773333', '2021-12-01', 3),
    ('Ali', 'Salah', 'Cairo', '01068884444', '2020-05-15', 4),
    ('Fatma', 'Mahmoud', 'Tanta', '01066665555', '2019-07-30', 5);



INSERT INTO project (p_name, start_date, end_date)
VALUES
    ('Website Redesign', '2023-01-01', '2023-06-30'),
    ('Mobile App', '2023-02-15', '2023-08-15'),
    ('Cloud Migration', '2023-03-01', '2023-09-30'),
    ('Automation Testing', '2023-04-10', '2023-10-10'),
    ('UI Overhaul', '2023-05-01', '2023-11-30');

INSERT INTO works_on (proj_id, emp_id, hours)
VALUES
    (1, 1, 120),
    (1, 6, 80),
    (2, 2, 150),
    (2, 7, 100),
    (3, 3, 200),
    (3, 8, 160),
    (4, 4, 90),
    (4, 9, 110),
    (5, 5, 130),
    (5, 10, 70),
    (1, 5, 17);



/*markdown
#### T1: Creating a Simple View
*/


-- 1st Method

CREATE OR REPLACE VIEW vw_employee_details AS
(
    SELECT 
        fname, lname, dept_name
    FROM
        employees e, department d
    WHERE
        e.dept_id = d.dept_id
);



-- 2nd Method

CREATE OR REPLACE VIEW vw_employee_details AS
(
    SELECT 
        fname, lname, dept_name
    FROM
        employees
    INNER JOIN department ON
        employees.dept_id = department.dept_id
);


SELECT * FROM vw_employee_details;



/*markdown
#### T2 : Modify the existing view vw_work_hrs to only include employees working in department number 5.


*/

-- 1st method

CREATE OR REPLACE VIEW vw_work_hrs AS 
(
    SELECT
        fname, lname, p_name, hours
    FROM
        employees e, works_on w, project p
    WHERE
        e.emp_id = w.emp_id
        AND
        w.proj_id = p.p_id
        AND
        dept_id = 5
);



-- 2nd Method

CREATE OR REPLACE VIEW vw_work_hrs AS 
(
    SELECT
        fname, lname, p_name, hours
    FROM
        employees e
    INNER JOIN works_on w ON
        e.emp_id = w.emp_id
    INNER JOIN project p ON
        w.proj_id = p.p_id
    WHERE
        dept_id = 5
);



SELECT * FROM vw_work_hrs;

/*markdown
#### T3 : Create a view named vw_high_status_suppliers to display all suppliers with a status greater than 15, and ensure that any updates or inserts through the view still meet the status condition.
*/

-- Suppliers Schema

CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(255) NOT NULL,
    contact_name VARCHAR(255),
    phone_number VARCHAR(50),
    status INT
);

-- insert Supplier Data

INSERT INTO suppliers (supplier_name, contact_name, phone_number, status)
VALUES
    ('Alpha Supplies', 'Mohamed Ali', '01064440001', 20),
    ('Beta Traders', 'Sara Hassan', '01064440002', 18),
    ('Gamma Co.', 'Omar Khalid', '01064440003', 15),
    ('Delta Corp.', 'Mariam Youssef', '01064440004', 10),
    ('Epsilon Ltd.', 'Youssef Mohamed', '01064440005', 25),
    ('Zeta Inc.', 'Layla Nabil', '01064440006', 30),
    ('Eta Enterprises', 'Hassan Adel', '01064440007', 12),
    ('Theta Supplies', 'Noor Sami', '01064440008', 17),
    ('Iota Traders', 'Ali Salah', '01064440009', 22),
    ('Kappa Corp.', 'Fatma Mahmoud', '01064440010', 14);

CREATE OR REPLACE VIEW vw_high_status_suppliers AS
(
    SELECT
        *
    FROM
        suppliers
    WHERE
        status > 15
)
WITH CHECK OPTION;

SELECT * FROM vw_high_status_suppliers;

-- Try insert status > 15
INSERT INTO vw_high_status_suppliers (supplier_name, contact_name, phone_number, status)
VALUES ('Lambda Supplies', 'Ahmed Sami', '01064441111', 25);


-- Try insert status > 15
INSERT INTO vw_high_status_suppliers (supplier_name, contact_name, phone_number, status)
VALUES ('Mu Traders', 'Sara Ali', '01064442222', 10);

/*markdown
#### T4 : Write a SQL query to retrieve all employees who were hired within the last 30 days from the current date.
*/


-- insert employees within 30 days

INSERT INTO employees (fname, lname, location, phone_number, hire_date, dept_id)
VALUES
    ('Ayman', 'Khaled', 'Cairo', '01064443333', CURRENT_DATE(), 1),
    ('Laila', 'Hassan', 'Giza', '01064442222', DATE_SUB(CURRENT_DATE(), INTERVAL 10 DAY), 2);



-- 1st Method
SELECT
    *
FROM
    employees
WHERE DATEDIFF(CURRENT_DATE(), hire_date) <= 30;

-- 2nd Method
SELECT
    * 
FROM
    employees
WHERE hire_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY);

/*markdown
#### T5 : Create a stored procedure named sp_get_employee_hours that retrieves the first name, last name, and total hours worked on projects for a given employee ID.
*/

DROP PROCEDURE IF EXISTS sp_get_employee_hours;


CREATE PROCEDURE sp_get_employee_hours(IN e_id INT)
BEGIN
    SELECT
        fname, lname, SUM(w.hours) as total_hours
    FROM
        employees e
    JOIN works_on w ON
        e.emp_id = w.emp_id
    WHERE
        e.emp_id = e_id
    GROUP BY e.emp_id;
END;

CALL sp_get_employee_hours(5);

/*markdown
#### T6 : Create a stored procedure named sp_department_employee_count that retrieves the department ID, department name, and the number of employees in each department, but only for departments with more than 5 employees.
*/

DROP PROCEDURE IF EXISTS sp_department_employee_count;

CREATE PROCEDURE sp_department_employee_count(IN d_id INT)
BEGIN
    SELECT
        d.dept_id, d.dept_name, COUNT(d.dept_id) as employees_count
    FROM
        department d
    JOIN employees e ON
        d.dept_id = e.dept_id
    GROUP BY d.dept_id
    HAVING COUNT(d.dept_id) > 5;
END

-- More Employees
INSERT INTO employees (fname, lname, location, phone_number, hire_date, dept_id)
VALUES
    ('Omar', 'Hassan', 'Cairo', '01064440011', '2025-08-01', 5),
    ('Sara', 'Ali', 'Giza', '01064440012', '2025-08-05', 5),
    ('Youssef', 'Khaled', 'Cairo', '01064440013', '2025-08-10', 5),
    ('Mariam', 'Adel', 'Alex', '01064440014', '2025-08-15', 5),
    ('Ahmed', 'Fahmy', 'Cairo', '01064440015', '2025-08-20', 5);

CALL sp_department_employee_count(5);