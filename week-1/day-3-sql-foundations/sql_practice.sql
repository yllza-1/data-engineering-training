-- Query 1: Show all orders
SELECT *
FROM orders;

-- Query 2: Show only customer names and products
SELECT customer_name, product
FROM orders;

-- Query 3: Show order ID, product, and status
SELECT order_id, product, status
FROM orders;

-- Query 4: Show customer name as customer and product as item
SELECT customer_name AS customer, product AS item
FROM orders;

-- Query 5: Show product, quantity, and price
SELECT product, quantity, price
FROM orders;

-- Query 6: Show order ID and customer name
SELECT order_id, customer_name
FROM orders;

-- Query 7: Show only completed orders
SELECT *
FROM orders
WHERE status = 'completed';

-- Query 8: Show only pending orders
SELECT *
FROM orders
WHERE status = 'pending';

-- Query 9: Show only cancelled orders
SELECT *
FROM orders
WHERE status = 'cancelled';

-- Query 10: Show orders where price is greater than 100
SELECT *
FROM orders
WHERE price > 100;

-- Query 11: Show orders where price is less than 100
SELECT *
FROM orders
WHERE price < 100;

-- Query 12: Show orders where price is greater than or equal to 180
SELECT *
FROM orders
WHERE price >= 180;

-- Query 13: Show orders where status is not cancelled
SELECT *
FROM orders
WHERE status != 'cancelled';

-- Query 14: Show orders where customer_name is Arta
SELECT *
FROM orders
WHERE customer_name = 'Arta';

-- Query 15: Show orders where product is Mouse
SELECT *
FROM orders
WHERE product = 'Mouse';

-- Query 16: Show completed orders where price is greater than 50
SELECT *
FROM orders
WHERE status = 'completed' AND price > 50;

-- Query 17: Show completed orders where product is Mouse
SELECT *
FROM orders
WHERE status = 'completed' AND product = 'Mouse';

-- Query 18: Show orders where status is pending OR cancelled
SELECT *
FROM orders
WHERE status = 'pending' OR status = 'cancelled';

-- Query 19: Show completed orders for customer Dren
SELECT *
FROM orders
WHERE customer_name = 'Dren' AND status = 'completed';

-- Query 20: Show Laptop orders with price 700
SELECT *
FROM orders
WHERE product = 'Laptop' AND price = 700;

-- Query 21: Show completed orders OR orders with price greater than 500
SELECT *
FROM orders
WHERE status = 'completed' OR price > 500;

-- Query 22: Show orders that are not cancelled and have price greater than 100
SELECT *
FROM orders
WHERE status != 'cancelled' AND price > 100;

-- Query 23: Show all orders from cheapest to most expensive
SELECT *
FROM orders
ORDER BY price ASC;

-- Query 24: Show all orders from most expensive to cheapest
SELECT *
FROM orders
ORDER BY price DESC;

-- Query 25: Show the top 3 most expensive orders
SELECT *
FROM orders
ORDER BY price DESC
LIMIT 3;

-- Query 26: Show the cheapest 2 orders
SELECT *
FROM orders
ORDER BY price ASC
LIMIT 2;

-- Query 27: Show completed orders from highest price to lowest price
SELECT *
FROM orders
WHERE status = 'completed'
ORDER BY price DESC;

-- Query 28: Show products sorted alphabetically by product name
SELECT *
FROM orders
ORDER BY product ASC;

-- Query 29: Show customers sorted alphabetically by customer_name
SELECT *
FROM orders
ORDER BY customer_name ASC;

-- Query 30: Show customer name, product, quantity, price, and total amount
SELECT customer_name, product, quantity, price,
       quantity * price AS total_amount
FROM orders;

-- Query 31: Show only completed orders with total amount
SELECT customer_name, product, quantity, price,
       quantity * price AS total_amount
FROM orders
WHERE status = 'completed';

-- Query 32: Show completed orders with total amount sorted from highest to lowest
SELECT customer_name, product, quantity, price,
       quantity * price AS total_amount
FROM orders
WHERE status = 'completed'
ORDER BY total_amount DESC;

-- Query 33: Show cancelled or pending orders with total amount
SELECT customer_name, product, quantity, price,
       quantity * price AS total_amount
FROM orders
WHERE status = 'cancelled' OR status = 'pending';

-- Query 34: Show customer as customer, product as item, and total amount
SELECT customer_name AS customer,
       product AS item,
       quantity * price AS total_amount
FROM orders;

-- Query 35: Show the top 3 orders by total amount
SELECT customer_name, product,
       quantity * price AS total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 3;

-- Query 36: Show only orders where total amount is greater than 100
SELECT customer_name, product,
       quantity * price AS total_amount
FROM orders
WHERE quantity * price > 100;

-- This query shows only completed orders.
-- It helps us see which orders have been successfully finished.
SELECT *
FROM orders
WHERE status = 'completed';

-- This query shows the three most expensive orders.
-- It helps us identify the highest-value orders.
SELECT *
FROM orders
ORDER BY price DESC
LIMIT 3;

-- This query calculates the total amount for each order.
-- It helps us see the value of every order instead of only quantity and price.
SELECT customer_name, product, quantity, price,
       quantity * price AS total_amount
FROM orders;

-- This query shows completed orders and calculates the total amount.
-- It helps us see completed sales and their total value.
SELECT customer_name, product,
       quantity * price AS total_amount
FROM orders
WHERE status = 'completed';

-- This query shows only orders with a total amount greater than 100.
-- It helps us find high-value orders for business analysis.
SELECT customer_name, product,
       quantity * price AS total_amount
FROM orders
WHERE quantity * price > 100;

DROP TABLE IF EXISTS memberships;

CREATE TABLE memberships (
    member_id INTEGER,
    member_name TEXT,
    plan TEXT,
    monthly_price INTEGER,
    visits INTEGER,
    status TEXT
);

INSERT INTO memberships VALUES
(1, 'Arta', 'Basic', 25, 8, 'active'),
(2, 'Blend', 'Premium', 40, 15, 'active'),
(3, 'Dren', 'Basic', 25, 3, 'inactive'),
(4, 'Elira', 'Premium', 40, 18, 'active'),
(5, 'Sara', 'VIP', 60, 20, 'active'),
(6, 'Ardian', 'Basic', 25, 5, 'inactive'),
(7, 'Lira', 'Premium', 40, 12, 'active'),
(8, 'Besa', 'VIP', 60, 22, 'active');


-- Query 37: Show all rows from the memberships table
SELECT *
FROM memberships;

-- Query 38: Show only member name and membership plan
SELECT member_name, plan
FROM memberships;

-- Query 39: Show only active members
SELECT *
FROM memberships
WHERE status = 'active';

-- Query 40: Show members with monthly price greater than 30
SELECT *
FROM memberships
WHERE monthly_price > 30;

-- Query 41: Show members sorted by number of visits from highest to lowest
SELECT *
FROM memberships
ORDER BY visits DESC;

-- Query 42: Show the first 3 members from the table
SELECT *
FROM memberships
LIMIT 3;

-- Query 43: Calculate total income using monthly price and visits
SELECT member_name,
       monthly_price,
       visits,
       monthly_price * visits AS total_income
FROM memberships;

-- Query 44: Show active members with their total income sorted from highest to lowest
SELECT member_name,
       monthly_price * visits AS total_income
FROM memberships
WHERE status = 'active'
ORDER BY total_income DESC;

