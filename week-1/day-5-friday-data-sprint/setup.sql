-- Delete the existing orders table if it exists
DROP TABLE IF EXISTS orders;

-- Create a new orders table with all required columns
CREATE TABLE orders (
    order_id INTEGER,
    customer_name TEXT,
    city TEXT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    price INTEGER,
    status TEXT,
    order_date TEXT
);

-- Insert order records into the orders table
INSERT INTO orders VALUES
(1, 'Arta', 'Vushtrri', 'Laptop', 'Electronics', 1, 700, 'completed', '2026-07-01'),
(2, 'Besnik', 'Prishtina', 'Mouse', 'Accessories', 2, 25, 'pending', '2026-07-02'),
(3, 'Drita', 'Mitrovica', 'Keyboard', 'Accessories', 1, 45, 'completed', '2026-07-02'),
(4, 'Erion', 'Peja', 'Printer', 'Office', 1, 180, 'cancelled', '2026-07-03'),
(5, 'Fjolla', 'Vushtrri', 'Monitor', 'Electronics', 2, 220, 'completed', '2026-07-03'),
(6, 'Gent', 'Prishtina', 'Desk', 'Office', 1, 150, 'pending', '2026-07-04'),
(7, 'Hana', 'Gjilan', 'USB Drive', 'Accessories', 5, 15, 'completed', '2026-07-04'),
(8, 'Ilir', 'Peja', 'Laptop', 'Electronics', 1, 850, 'cancelled', '2026-07-05'),
(9, 'Jon', 'Mitrovica', 'Office Chair', 'Office', 2, 120, 'completed', '2026-07-05'),
(10, 'Klea', 'Gjilan', 'Headphones', 'Electronics', 3, 60, 'pending', '2026-07-06'),
(11, 'Luan', 'Vushtrri', 'Notebook', 'Office', 10, 5, 'completed', '2026-07-06'),
(12, 'Mira', 'Prishtina', 'Webcam', 'Accessories', 2, 80, 'cancelled', '2026-07-07'),
(13, 'Nora', 'Peja', 'Tablet', 'Electronics', 1, 400, 'completed', '2026-07-07'),
(14, 'Orhan', 'Gjilan', 'Printer Paper', 'Office', 20, 8, 'pending', '2026-07-08'),
(15, 'Petrit', 'Mitrovica', 'Speaker', 'Electronics', 2, 90, 'completed', '2026-07-08');

-- Display all orders to verify inserted data
SELECT * FROM orders;
