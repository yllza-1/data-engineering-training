-- Completed revenue by order date
-- This report shows the total revenue generated only from completed orders for each date.

SELECT
    orders.order_date,
    SUM(orders.quantity * orders.price) AS completed_revenue
FROM orders
WHERE orders.status = 'completed'
GROUP BY orders.order_date
ORDER BY orders.order_date;


-- Average completed order value by category
-- This report shows the average value of completed orders for each product category.

SELECT
    products.category,
    AVG(orders.quantity * orders.price) AS average_completed_order_value
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.category
ORDER BY average_completed_order_value DESC;


-- Product performance report
-- This report shows order statistics and revenue information for every product.

SELECT
    products.product_name,

    COUNT(orders.order_id) AS total_orders,

    SUM(
        CASE
            WHEN orders.status = 'completed' THEN 1
            ELSE 0
        END
    ) AS completed_orders,

    SUM(
        CASE
            WHEN orders.status = 'completed' THEN orders.quantity
            ELSE 0
        END
    ) AS completed_quantity,

    SUM(
        CASE
            WHEN orders.status = 'completed'
            THEN orders.quantity * orders.price
            ELSE 0
        END
    ) AS completed_revenue

FROM products
LEFT JOIN orders
ON products.product_id = orders.product_id

GROUP BY products.product_name
ORDER BY completed_revenue DESC;


-- City performance report
-- This report shows order information and completed revenue for every city.

SELECT
    customers.city,

    COUNT(orders.order_id) AS total_orders,

    SUM(
        CASE
            WHEN orders.status = 'completed' THEN 1
            ELSE 0
        END
    ) AS completed_orders,

    SUM(
        CASE
            WHEN orders.status = 'pending'
            OR orders.status = 'cancelled'
            THEN 1
            ELSE 0
        END
    ) AS pending_or_cancelled_orders,

    SUM(
        CASE
            WHEN orders.status = 'completed'
            THEN orders.quantity * orders.price
            ELSE 0
        END
    ) AS completed_revenue

FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id

GROUP BY customers.city
ORDER BY completed_revenue DESC;

-- Adding two new orders for testing reports

INSERT INTO orders
(order_id, customer_id, product_id, quantity, price, status, order_date)
VALUES
(13, 2, 3, 2, 150, 'completed', '2026-07-13'),
(14, 4, 1, 1, 80, 'pending', '2026-07-13');