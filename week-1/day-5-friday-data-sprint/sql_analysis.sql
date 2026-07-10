-- Show only completed orders
SELECT *
FROM orders
WHERE status = 'completed';


-- Show pending or cancelled orders
SELECT *
FROM orders
WHERE status IN ('pending', 'cancelled');


-- Show total amount calculated as quantity multiplied by price
SELECT *,
       quantity * price AS total_amount
FROM orders;


-- Show completed orders with their total amount
SELECT *,
       quantity * price AS total_amount
FROM orders
WHERE status = 'completed';


-- Calculate total revenue from completed orders
SELECT SUM(quantity * price) AS completed_revenue
FROM orders
WHERE status = 'completed';


-- Count orders grouped by status
SELECT status,
       COUNT(*) AS total_orders
FROM orders
GROUP BY status;

-- Count orders grouped by city
SELECT city,
       COUNT(*) AS total_orders
FROM orders
GROUP BY city;

-- Count orders grouped by category
SELECT category,
       COUNT(*) AS total_orders
FROM orders
GROUP BY category;

-- Show the top 3 orders with the highest total amount
SELECT *,
       quantity * price AS total_amount
FROM orders
ORDER BY quantity * price DESC
LIMIT 3;

-- Find the most valuable order
SELECT *,
       quantity * price AS total_amount
FROM orders
ORDER BY quantity * price DESC
LIMIT 1;