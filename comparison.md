# Python vs SQL Comparison

## Task 1: Show all orders

### Python approach:

- Loop through the orders list.
- Print every order from the list.

### SQL approach:

- Use `SELECT *` to get all records from the orders table.

### What I understood:

Both approaches display all available data. Python reads items from a list, while SQL retrieves rows from a table.

---

## Task 2: Show completed orders

### Python approach:

- Loop through the orders list.
- Check if `order["status"] == "completed"`.
- Print only completed orders.

### SQL approach:

- Use `SELECT` to choose the data.
- Use `WHERE status = 'completed'` to filter records.

### What I understood:

Both approaches filter data. Python uses conditions, while SQL uses the WHERE clause.

---

## Task 3: Show orders with price greater than 100

### Python approach:

- Loop through orders.
- Check if `order["price"] > 100`.
- Keep matching orders.

### SQL approach:

- Use `WHERE price > 100`.

### What I understood:

Both methods compare values and return only records that match the condition.

---

## Task 4: Calculate total_amount

### Python approach:

- Loop through orders.
- Multiply `quantity * price`.
- Store the result as `total_amount`.

### SQL approach:

- Use `quantity * price AS total_amount`.

### What I understood:

Both approaches calculate new values from existing data. Python calculates during the loop, while SQL calculates during the query.

---

## Task 5: Sort orders by price descending

### Python approach:

- Use `sorted()`.
- Use price as the sorting key.
- Set descending order.

### SQL approach:

- Use `ORDER BY price DESC`.

### What I understood:

Both approaches organize data from highest to lowest value.

---

## Task 6: Show top 3 expensive orders

### Python approach:

- Sort orders by price.
- Use slicing `[:3]` to get the first three records.

### SQL approach:

- Use `ORDER BY price DESC LIMIT 3`.

### What I understood:

Both methods first sort data and then limit the number of results.

---

## Task 7: Find orders that are pending or cancelled

### Python approach:

- Loop through orders.
- Check if status is `pending` or `cancelled`.
- Store these orders.

### SQL approach:

- Use `WHERE status = 'pending' OR status = 'cancelled'`.

### What I understood:

Both approaches identify records based on multiple conditions.

---

## Task 8: Calculate completed revenue

### Python approach:

- Loop through orders.
- Check if the status is completed.
- Add `quantity * price` to the total revenue.

### SQL approach:

- Use `SUM(quantity * price)`.
- Filter using `WHERE status = 'completed'`.

### What I understood:

Both methods calculate business results while excluding unwanted data.

---

## Task 9: Count orders by city

### Python approach:

- Create an empty dictionary.
- Loop through orders.
- Increase the count for each city.

### SQL approach:

- Use `COUNT(*)`.
- Group results with `GROUP BY city`.

### What I understood:

Both approaches group data and count how many records belong to each category.

---

## Task 10: Count orders by category

### Python approach:

- Create a dictionary for categories.
- Loop through orders.
- Increase the category counter.

### SQL approach:

- Use `COUNT(*)`.
- Use `GROUP BY category`.

### What I understood:

Both Python and SQL can summarize data. Python uses dictionaries, while SQL uses aggregation functions.
