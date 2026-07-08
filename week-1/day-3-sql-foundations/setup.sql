DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INTEGER,
    customer_name TEXT,
    product TEXT,
    quantity INTEGER,
    price INTEGER,
    status TEXT
);

INSERT INTO orders (order_id, customer_name, product, quantity, price, status)
VALUES
(1, 'Arta', 'Laptop', 1, 800, 'Completed'),
(2, 'Besa', 'Phone', 2, 500, 'Pending'),
(3, 'Luan', 'Keyboard', 3, 50, 'Completed'),
(4, 'Diona', 'Mouse', 5, 25, 'Pending'),
(5, 'Erion', 'Monitor', 2, 300, 'Completed'),
(6, 'Sara', 'Headphones', 4, 100, 'Cancelled'),
(7, 'Jon', 'Tablet', 1, 450, 'Completed'),
(8, 'Era', 'Printer', 1, 200, 'Pending'),
(9, 'Leon', 'Webcam', 3, 75, 'Completed'),
(10, 'Mira', 'USB Cable', 10, 10, 'Completed');



