# Query Explanations

## Fixed Query 1

**What it does:** Counts the number of orders from each city.
**Tables used:** orders, customers.
**Why JOIN is needed:** The city column is stored in the customers table, so the tables must be joined using customer_id.
**Result meaning:** Shows which cities have the highest number of orders.

---

## Fixed Query 2

**What it does:** Calculates revenue for each completed product.
**Tables used:** orders, products.
**Why JOIN is needed:** The product name and price are stored in the products table.
**Result meaning:** Shows how much revenue each product generated.

---

## Fixed Query 3

**What it does:** Counts orders for each status and sorts them from highest to lowest.
**Tables used:** orders.
**Why JOIN is not needed:** All required columns are in the orders table.
**Result meaning:** Shows how many orders are completed, pending, or cancelled.

---

## Fixed Query 4

**What it does:** Displays each order with its quantity, product price, and total amount.
**Tables used:** orders, products.
**Why JOIN is needed:** The product price is stored in the products table.
**Result meaning:** Shows the value of every order.

---

## Fixed Query 5

**What it does:** Calculates the total completed quantity sold for each category.
**Tables used:** orders, products.
**Why JOIN is needed:** The category column is stored in the products table.
**Result meaning:** Shows which categories sold the most items.

---

## Fixed Query 8

**What it does:** Displays each order together with the customer name.
**Tables used:** orders, customers.
**Why JOIN is needed:** Customer names are stored in the customers table.
**Result meaning:** Makes it easy to identify which customer placed each order.

---

## Fixed Query 9

**What it does:** Shows the customer ID, product ID, and product price.
**Tables used:** orders, products.
**Why JOIN is needed:** The product price comes from the products table.
**Result meaning:** Links each order to the correct product price.

---

## Fixed Query 10

**What it does:** Displays orders that are not completed.
**Tables used:** orders.
**Why JOIN is not needed:** Only the orders table is required.
**Result meaning:** Identifies orders that should not be included in revenue.

# Validation Query Explanations

## Validation Query V1

**What it does:** Counts all orders.
**Tables used:** orders.
**Why JOIN is not needed:** The data comes from one table.
**Result meaning:** Shows the total number of orders.

---

## Validation Query V7

**What it does:** Calculates total revenue from completed orders.
**Tables used:** orders, products.
**Why JOIN is needed:** Product prices are stored in the products table.
**Result meaning:** Shows the total verified revenue.

---

## Validation Query V8

**What it does:** Calculates completed revenue for each product.
**Tables used:** orders, products.
**Why JOIN is needed:** Product names and prices come from the products table.
**Result meaning:** Shows which products generate the most revenue.

---

## Validation Query V10

**What it does:** Counts orders by city.
**Tables used:** orders, customers.
**Why JOIN is needed:** The city information is stored in the customers table.
**Result meaning:** Shows which cities have the most orders.

---

## Validation Query V12

**What it does:** Finds the three completed orders with the highest total amount.
**Tables used:** orders, products.
**Why JOIN is needed:** The product price is needed to calculate the total amount.
**Result meaning:** Identifies the highest-value completed orders.
