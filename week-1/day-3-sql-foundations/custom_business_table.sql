-- Create custom business table

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id INTEGER,
    employee_name TEXT,
    department TEXT,
    salary INTEGER,
    experience_years INTEGER,
    status TEXT
);

-- Insert data

INSERT INTO employees (employee_id, employee_name, department, salary, experience_years, status)
VALUES
(1, 'Arta', 'Data Engineering', 1200, 3, 'Active'),
(2, 'Besa', 'Marketing', 900, 2, 'Active'),
(3, 'Luan', 'IT Support', 1000, 4, 'Inactive'),
(4, 'Diona', 'Data Engineering', 1500, 5, 'Active'),
(5, 'Erion', 'HR', 800, 1, 'Active'),
(6, 'Sara', 'Marketing', 1100, 3, 'Active'),
(7, 'Jon', 'IT Support', 1300, 6, 'Inactive'),
(8, 'Mira', 'Data Engineering', 1700, 7, 'Active');


-- 1. Show all employees
SELECT * FROM employees;


-- 2. Show employee names only
SELECT employee_name FROM employees;


-- 3. Show employees with active status
SELECT *
FROM employees
WHERE status = 'Active';


-- 4. Show employees from Data Engineering department
SELECT *
FROM employees
WHERE department = 'Data Engineering';


-- 5. Show employees with salary greater than 1000
SELECT *
FROM employees
WHERE salary > 1000;


-- 6. Show employees with experience more than 3 years
SELECT *
FROM employees
WHERE experience_years > 3;


-- 7. Sort employees by salary ascending
SELECT *
FROM employees
ORDER BY salary ASC;


-- 8. Sort employees by salary descending
SELECT *
FROM employees
ORDER BY salary DESC;


-- 9. Count total employees
SELECT COUNT(*) AS total_employees
FROM employees;


-- 10. Count employees by department
SELECT department, COUNT(*) AS total
FROM employees
GROUP BY department;


-- 11. Calculate average salary
SELECT AVG(salary) AS average_salary
FROM employees;


-- 12. Find maximum salary
SELECT MAX(salary) AS highest_salary
FROM employees;


-- 13. Find minimum salary
SELECT MIN(salary) AS lowest_salary
FROM employees;


-- 14. Calculate total salary cost
SELECT SUM(salary) AS total_salary
FROM employees;


-- 15. Show active employees ordered by salary
SELECT *
FROM employees
WHERE status = 'Active'
ORDER BY salary DESC;


-- 16. Find employees from Marketing or HR
SELECT *
FROM employees
WHERE department IN ('Marketing', 'HR');


-- 17. Find employees whose name starts with A
SELECT *
FROM employees
WHERE employee_name LIKE 'A%';


-- 18. Find employees with salary between 900 and 1500
SELECT *
FROM employees
WHERE salary BETWEEN 900 AND 1500;


-- 19. Count active and inactive employees
SELECT status, COUNT(*) AS total
FROM employees
GROUP BY status;


-- 20. Show top 3 highest paid employees
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;

-- Custom business table: products

CREATE TABLE products (
    product_id INTEGER,
    product_name TEXT,
    category TEXT,
    stock_quantity INTEGER
);

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 10),
(2, 'Phone', 'Electronics', 25),
(3, 'Keyboard', 'Accessories', 50),
(4, 'Mouse', 'Accessories', 40);

-- Connection:
-- products table stores product information.
-- orders table stores customer purchases.
-- They can connect through product_id in a real database.