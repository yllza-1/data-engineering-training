-- Count all orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Count only completed orders
SELECT COUNT(*) AS completed_orders
FROM orders
WHERE status = 'completed';

-- Count only pending orders
SELECT COUNT(*) AS pending_orders
FROM orders
WHERE status = 'pending';

-- Count only cancelled orders
SELECT COUNT(*) AS cancelled_orders
FROM orders
WHERE status = 'cancelled';

-- Calculate total quantity ordered across all statuses
SELECT SUM(quantity) AS total_quantity_ordered
FROM orders;

-- Calculate total quantity ordered only from completed orders
SELECT SUM(quantity) AS completed_quantity_ordered
FROM orders
WHERE status = 'completed';

-- Find the average product price
SELECT AVG(price) AS average_product_price
FROM products;

-- Find the cheapest product price
SELECT MIN(price) AS cheapest_product_price
FROM products;

-- Find the most expensive product price
SELECT MAX(price) AS most_expensive_product_price
FROM products;

-- Calculate completed revenue using quantity * price
SELECT SUM(o.quantity * p.price) AS completed_revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
WHERE o.status = 'completed';

-- Calculate potential value from pending and cancelled orders
SELECT SUM(o.quantity * p.price) AS non_completed_potential_value
FROM orders o
JOIN products p
ON o.product_id = p.product_id
WHERE o.status IN ('pending', 'cancelled');

-- Pending and cancelled orders are not counted as real revenue because they are not completed transactions and payment has not been received.