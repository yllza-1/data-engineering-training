-- Count orders by status
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status
ORDER BY order_count DESC;

-- Count orders by order date
SELECT order_date, COUNT(*) AS order_count
FROM orders
GROUP BY order_date
ORDER BY order_count DESC;

-- Count orders by customer
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
ORDER BY order_count DESC;

-- Count orders by product
SELECT product_id, COUNT(*) AS order_count
FROM orders
GROUP BY product_id
ORDER BY order_count DESC;

-- Calculate total quantity by product for completed orders only
SELECT product_id, SUM(quantity) AS total_quantity
FROM orders
WHERE status = 'completed'
GROUP BY product_id
ORDER BY total_quantity DESC;

-- Calculate completed revenue by product
SELECT products.product_id, SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.product_id
ORDER BY completed_revenue DESC;

-- Calculate completed revenue by status
SELECT status, SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY status
ORDER BY completed_revenue DESC;

-- Show customers with more than one order using HAVING
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1
ORDER BY order_count DESC;

-- Show products with completed quantity greater than 2 using HAVING
SELECT product_id, SUM(quantity) AS completed_quantity
FROM orders
WHERE status = 'completed'
GROUP BY product_id
HAVING SUM(quantity) > 2
ORDER BY completed_quantity DESC;

-- Revenue by category sorted from highest to lowest
SELECT
    category,
    SUM(quantity * price) AS completed_revenue
FROM orders
WHERE status = 'completed'
GROUP BY category
ORDER BY completed_revenue DESC;


-- Orders by city sorted from highest to lowest
SELECT
    city,
    COUNT(*) AS total_orders
FROM orders
GROUP BY city
ORDER BY total_orders DESC;


-- Orders by category sorted from highest to lowest
SELECT
    category,
    COUNT(*) AS total_orders
FROM orders
GROUP BY category
ORDER BY total_orders DESC;


-- Completed orders by product sorted from highest to lowest revenue
SELECT
    product,
    COUNT(*) AS completed_orders,
    SUM(quantity) AS completed_quantity,
    SUM(quantity * price) AS completed_revenue
FROM orders
WHERE status = 'completed'
GROUP BY product
ORDER BY completed_revenue DESC;


-- Average order value by category sorted from highest to lowest
SELECT
    category,
    AVG(quantity * price) AS average_order_value
FROM orders
WHERE status = 'completed'
GROUP BY category
ORDER BY average_order_value DESC;


-- Completed revenue by order date sorted from highest to lowest
SELECT
    order_date,
    SUM(quantity * price) AS daily_revenue
FROM orders
WHERE status = 'completed'
GROUP BY order_date
ORDER BY daily_revenue DESC;


-- City report sorted from highest to lowest completed revenue
SELECT
    city,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed_orders,
    SUM(CASE WHEN status IN ('pending', 'cancelled') THEN 1 ELSE 0 END) AS pending_or_cancelled_orders,
    SUM(CASE WHEN status = 'completed' THEN quantity * price ELSE 0 END) AS completed_revenue
FROM orders
GROUP BY city
ORDER BY completed_revenue DESC;
