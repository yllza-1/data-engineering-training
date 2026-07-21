# Pipeline Explanation - Day 11

## Data Understanding

### How many raw orders exist?

There are 24 raw orders in orders_raw.csv.

### Which columns are used to join orders with customers and products?

Orders are joined with customers using customer_id.

Orders are joined with products using product_id.

### Which values look inconsistent?

Status values:

- completed
- Completed
- done
- cancelled
- canceled
- returned
- pending
- missing value

Channel values:

- online
- Online
- store
- Store
- web
- bank
- missing value

Quantity values:

- missing quantity
- negative quantity
- zero quantity
- non numeric quantity (abc)

Order date:

- missing order date

Customer ID:

- C013 does not exist in customers_raw.csv

Product ID:

- P999 does not exist in products_raw.csv

City values:

- Prishtina
- prishtina
- VUSHTRRI
- ferizaj

### Which records should not be trusted for revenue?

Do not use orders for revenue when they have:

- missing quantity
- invalid quantity
- negative quantity
- zero quantity
- missing status
- invalid status
- missing order date
- invalid customer_id
- invalid product_id

### Which file is Bronze, which output should be Silver, and which output should be Gold?

Bronze:

- data/bronze/orders_raw.csv
- data/bronze/customers_raw.csv
- data/bronze/products_raw.csv

Silver:

- data/silver/orders_clean.csv
- data/silver/customers_clean.csv
- data/silver/products_clean.csv
- data/silver/invalid_orders.csv

Gold:

- data/gold/revenue_by_category.csv
- data/gold/revenue_by_city.csv
- data/gold/revenue_by_customer.csv
- data/gold/top_products.csv
- data/gold/executive_summary.txt
