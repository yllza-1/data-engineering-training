DROP TABLE IF EXISTS clean_orders;

CREATE TABLE clean_orders (
    order_id INTEGER,
    customer_id TEXT,
    customer_name TEXT,
    city TEXT,
    segment TEXT,
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    status TEXT,
    order_date TEXT,
    channel TEXT,
    total_amount REAL
);

SELECT * 
FROM clean_orders;