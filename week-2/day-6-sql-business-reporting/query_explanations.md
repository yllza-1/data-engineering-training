# Query Explanations

## Query 1: Count orders by status

File: group_by_reports.sql

Business question:
How many orders are completed, pending, or cancelled?

Tables used:
orders

Why GROUP BY is needed:
GROUP BY separates orders by status.

Why COUNT is needed:
COUNT counts the number of orders in each status.

What I understood:
This query shows the current order situation.

## Query 2: Completed revenue by category

File: join_reports.sql

Business question:
Which category generated the most completed revenue?

Tables used:
orders and products

Why JOIN is needed:
Orders has product_id, while products has category and price. JOIN connects them.

Why WHERE is needed:
Only completed orders are counted as real revenue.

Why GROUP BY is needed:
It groups the revenue by category.

What I understood:
This query shows which category performs better.

## Query 3: Completed revenue by product

File: join_reports.sql

Business question:
Which product generated the most revenue?

Tables used:
orders and products

Why JOIN is needed:
We need quantity from orders and price from products.

Why WHERE is needed:
Only completed orders are included.

Why GROUP BY is needed:
It calculates revenue for each product.

What I understood:
This helps find the most valuable products.

## Query 4: Count orders by customer

File: group_by_reports.sql

Business question:
How many orders does each customer have?

Tables used:
orders

Why GROUP BY is needed:
It groups orders by customer_id.

Why COUNT is needed:
It counts orders for each customer.

What I understood:
This shows customer activity.

## Query 5: Total quantity by product

File: group_by_reports.sql

Business question:
How many products were ordered?

Tables used:
orders

Why WHERE is needed:
Only completed orders are counted.

Why GROUP BY is needed:
It separates results by product.

Why SUM is needed:
SUM adds the quantities.

What I understood:
This helps understand product demand.

## Query 6: Completed revenue by customer

File: join_reports.sql

Business question:
Which customer generated the most revenue?

Tables used:
orders, customers, and products

Why JOIN is needed:
Customer names and product prices are stored in different tables.

Why WHERE is needed:
Only completed sales are included.

Why GROUP BY is needed:
It calculates revenue for each customer.

What I understood:
This helps find important customers.

## Query 7: Customers with more than one order

File: join_reports.sql

Business question:
Which customers have multiple orders?

Tables used:
orders and customers

Why JOIN is needed:
It shows customer names.

Why GROUP BY is needed:
It groups orders by customer.

Why HAVING is needed:
It shows only customers with more than one order.

What I understood:
This finds returning customers.

## Query 8: Top 3 customers by revenue

File: join_reports.sql

Business question:
Who are the top customers by revenue?

Tables used:
orders, customers, and products

Why JOIN is needed:
Information comes from multiple tables.

Why GROUP BY is needed:
Revenue is calculated for each customer.

Why ORDER BY and LIMIT are needed:
They show only the highest three customers.

What I understood:
This helps focus on valuable customers.

## Query 9: Pending and cancelled orders value

File: join_reports.sql

Business question:
What is the value of unfinished orders?

Tables used:
orders, customers, and products

Why JOIN is needed:
We need customer and product information.

Why WHERE is needed:
Only pending and cancelled orders are selected.

What I understood:
This shows possible revenue that was not completed.

## Query 10: Top 3 products by revenue

File: join_reports.sql

Business question:
Which products generated the most revenue?

Tables used:
orders and products

Why JOIN is needed:
Orders has quantity and products has price.

Why GROUP BY is needed:
Revenue is calculated for each product.

Why ORDER BY and LIMIT are needed:
They show the top three products.

What I understood:
This helps the business understand the best products.
