-- V1: Count all orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- V2: Count completed orders
SELECT COUNT(*) AS completed_orders
FROM orders
WHERE status = 'completed';

-- V3: Count pending orders
SELECT COUNT(*) AS pending_orders
FROM orders
WHERE status = 'pending';

-- V4: Count cancelled orders
SELECT COUNT(*) AS cancelled_orders
FROM orders
WHERE status = 'cancelled';

-- V5: Count all customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- V6: Count all products
SELECT COUNT(*) AS total_products
FROM products;

-- V7: Calculate completed revenue only
SELECT SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed';

-- V8: Calculate completed revenue by product
SELECT products.product_name,
       SUM(orders.quantity * products.price) AS revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.product_name;

-- V9: Calculate completed revenue by category
SELECT products.category,
       SUM(orders.quantity * products.price) AS revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.category;

-- V10: Count orders by city
SELECT customers.city,
       COUNT(*) AS order_count
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
GROUP BY customers.city;

-- V11: Find customers with more than one order
SELECT customer_id,
       COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- V12: Top 3 completed orders by total amount
SELECT orders.order_id,
       orders.quantity,
       products.price,
       orders.quantity * products.price AS total_amount
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
ORDER BY total_amount DESC
LIMIT 3;

-- V13: Find orders that should not count as revenue
SELECT *
FROM orders
WHERE status != 'completed';

-- V14: Category with the highest completed revenue
SELECT products.category,
       SUM(orders.quantity * products.price) AS revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.category
ORDER BY revenue DESC
LIMIT 1;

-- V15: City with the highest order activity
SELECT customers.city,
       COUNT(*) AS order_count
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
GROUP BY customers.city
ORDER BY order_count DESC
LIMIT 1;