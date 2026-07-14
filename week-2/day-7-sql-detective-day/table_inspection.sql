-- Check all records in the orders table.
SELECT *
FROM orders;

-- Check all records in the customers table.
SELECT *
FROM customers;

-- Check all records in the products table.
SELECT *
FROM products;

-- Check how many order records exist in the orders table.
SELECT COUNT(*) AS total_orders
FROM orders;

-- Check how many customer records exist in the customers table.
SELECT COUNT(*) AS total_customers
FROM customers;

-- Check how many product records exist in the products table.
SELECT COUNT(*) AS total_products
FROM products;
