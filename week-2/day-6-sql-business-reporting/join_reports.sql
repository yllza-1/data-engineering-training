-- Join orders with customers and show customer information
SELECT orders.order_id, customers.customer_name, customers.city, orders.order_date, orders.status
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;


-- Join orders with products and calculate total amount
SELECT orders.order_id, products.product_name, products.category, orders.quantity, products.price,
       (orders.quantity * products.price) AS total_amount, orders.status
FROM orders
JOIN products
ON orders.product_id = products.product_id;


-- Join all three tables and create complete order report
SELECT customers.customer_name, customers.city, products.product_name, products.category,
       orders.quantity, products.price, (orders.quantity * products.price) AS total_amount,
       orders.status, orders.order_date
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN products
ON orders.product_id = products.product_id;


-- Calculate completed revenue by product name
SELECT products.product_name, SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.product_name
ORDER BY completed_revenue DESC;


-- Calculate completed revenue by category
SELECT products.category, SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.category
ORDER BY completed_revenue DESC;


-- Count orders by city
SELECT customers.city, COUNT(orders.order_id) AS order_count
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
GROUP BY customers.city
ORDER BY order_count DESC;


-- Calculate completed revenue by city
SELECT customers.city, SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY customers.city
ORDER BY completed_revenue DESC;


-- Calculate completed revenue by customer name
SELECT customers.customer_name, SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY customers.customer_name
ORDER BY completed_revenue DESC;


-- Show customers with more than one order
SELECT customers.customer_name, COUNT(orders.order_id) AS order_count
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_name
HAVING COUNT(orders.order_id) > 1
ORDER BY order_count DESC;


-- Show top 3 customers by completed revenue
SELECT customers.customer_name, SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY customers.customer_name
ORDER BY completed_revenue DESC
LIMIT 3;


-- Show top 3 products by completed revenue
SELECT products.product_name, SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.product_name
ORDER BY completed_revenue DESC
LIMIT 3;


-- Show pending or cancelled orders with potential amount
SELECT customers.customer_name, customers.city, products.product_name,
       (orders.quantity * products.price) AS potential_amount
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status IN ('pending', 'cancelled');