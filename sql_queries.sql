-- Show all orders from the orders table
SELECT * 
FROM orders;


-- Show only the customer name and product
SELECT customer_name, product
FROM orders;


-- Show order ID, customer name, city, and status
SELECT order_id, customer_name, city, status
FROM orders;


-- Show product, category, quantity, and price
SELECT product, category, quantity, price
FROM orders;


-- Show only orders that have completed status
SELECT *
FROM orders
WHERE status = 'completed';


-- Show only orders that have pending status
SELECT *
FROM orders
WHERE status = 'pending';


-- Show only orders that have cancelled status
SELECT *
FROM orders
WHERE status = 'cancelled';


-- Show orders where the price is greater than 100
SELECT *
FROM orders
WHERE price > 100;


-- Show orders that are from Vushtrri city
SELECT *
FROM orders
WHERE city = 'Vushtrri';


-- Show orders where the category is Accessories
SELECT *
FROM orders
WHERE category = 'Accessories';


-- Show completed orders where the price is greater than 100
SELECT *
FROM orders
WHERE status = 'completed' AND price > 100;


-- Show completed orders from Prishtina
SELECT *
FROM orders
WHERE status = 'completed' AND city = 'Prishtina';


-- Show orders where the status is pending or cancelled
SELECT *
FROM orders
WHERE status = 'pending' OR status = 'cancelled';


-- Show Accessories orders where the price is less than 50
SELECT *
FROM orders
WHERE category = 'Accessories' AND price < 50;


-- Show orders from cheapest to most expensive
SELECT *
FROM orders
ORDER BY price ASC;


-- Show orders from most expensive to cheapest
SELECT *
FROM orders
ORDER BY price DESC;


-- Show the top 3 most expensive orders by price
SELECT *
FROM orders
ORDER BY price DESC
LIMIT 3;


-- Calculate total amount for each order and show the top 3 highest totals
SELECT *,
quantity * price AS total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 3;


-- Show customer name, product, quantity, price, and calculate total amount
SELECT customer_name, product, quantity, price,
quantity * price AS total_amount
FROM orders;


-- Show completed orders with customer name, product, quantity, price, and total amount
SELECT customer_name, product, quantity, price,
quantity * price AS total_amount
FROM orders
WHERE status = 'completed';


-- Show completed orders sorted by the highest total amount
SELECT customer_name, product, quantity, price,
quantity * price AS total_amount
FROM orders
WHERE status = 'completed'
ORDER BY total_amount DESC;



-- Find the customer with the most expensive single order
SELECT customer_name, product, price
FROM orders
ORDER BY price DESC
LIMIT 1;


-- Find the order with the highest total_amount
SELECT *,
quantity * price AS total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 1;


-- Find orders that should NOT be counted as real revenue because they are pending or cancelled
SELECT *
FROM orders
WHERE status = 'pending' OR status = 'cancelled';


-- Calculate completed revenue only (exclude pending and cancelled orders)
SELECT SUM(quantity * price) AS completed_revenue
FROM orders
WHERE status = 'completed';


-- Find the most valuable order with customer information and total amount
SELECT customer_name, product, quantity, price,
quantity * price AS total_amount
FROM orders
WHERE status = 'completed'
ORDER BY total_amount DESC
LIMIT 1;


-- Show all completed orders sorted by their revenue value
SELECT customer_name, product, quantity, price,
quantity * price AS total_amount
FROM orders
WHERE status = 'completed'
ORDER BY total_amount DESC;


-- Count orders by city
SELECT city, COUNT(*) AS order_count
FROM orders
GROUP BY city;


-- Count orders by category
SELECT category, COUNT(*) AS category_count
FROM orders
GROUP BY category;


-- Count orders by status
SELECT status, COUNT(*) AS status_count
FROM orders
GROUP BY status;


-- Calculate total sales for each city
SELECT city, SUM(quantity * price) AS total_sales
FROM orders
GROUP BY city;