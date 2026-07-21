# Day 11 - Python + SQL Pipeline Preparation

## Project Goal

The goal of this project is to build a data pipeline using Python and SQL.

The pipeline reads raw Bronze data, cleans and validates the data into Silver layer, and creates business reports in Gold layer.

---

## Bronze Data

### What raw files did you receive?

The Bronze layer contains three raw CSV files:

- orders_raw.csv
- customers_raw.csv
- products_raw.csv

These files contain the original data before cleaning.

### What problems did you notice?

The raw data contained several quality issues:

- Missing quantity values
- Invalid quantity values
- Negative and zero quantities
- Missing order status
- Unknown status values
- Different formats of status values
- Different formats of city names
- Different formats of channel values
- Missing order dates
- Invalid customer IDs
- Invalid product IDs
- Duplicate order IDs

---

## Silver Data

### What validation rules did you apply?

The following validation rules were applied:

- order_id must not be duplicated
- quantity must exist
- quantity must be numeric
- quantity must be greater than zero
- status must be completed, pending, or cancelled
- order_date must exist
- customer_id must exist in customers data
- product_id must exist in products data

### Which records became invalid and why?

Records became invalid because of:

- missing quantity
- invalid quantity
- duplicate order_id
- missing status
- invalid status
- missing order date
- invalid customer_id
- invalid product_id

Invalid records were saved in:

data/silver/invalid_orders.csv

### What did you normalize?

The pipeline normalized:

- Status values:
  - Completed -> completed
  - done -> completed
  - canceled -> cancelled

- City names:
  - prishtina -> Prishtina
  - VUSHTRRI -> Vushtrri

- Channel values:
  - Online -> online
  - Store -> store
  - missing values -> unknown

---

## Gold Reports

### What business reports did you create?

The Gold layer contains:

- revenue_by_city.csv
- revenue_by_category.csv
- top_customers.csv
- executive_summary.txt

These reports provide business information from trusted Silver data.

### Which report is most useful for a manager?

The executive_summary.txt report is the most useful because it provides a quick overview of:

- total valid orders
- invalid orders
- completed orders
- completed revenue

---

## Python vs SQL

### What did Python help you do?

Python was used for:

- reading CSV files
- cleaning data
- validating records
- normalizing values
- joining customers and products
- creating Silver data
- generating Gold reports

### What did SQL help you do?

SQL was used for:

- querying clean Silver data
- creating business reports
- calculating revenue
- counting orders
- analyzing customers, cities, and categories

---

## Data Quality Notes

Data quality was improved by removing invalid records and keeping only trusted data.

The pipeline ensures that:

- only valid orders enter Silver layer
- only completed valid orders are used for revenue calculations
- raw data remains unchanged in Bronze layer

---

## Business Insights

The pipeline can show:

- total completed revenue
- revenue by city
- revenue by category
- top customers
- top orders
- order distribution by status and channel

These insights help managers understand sales performance.

---

## What I Can Explain Live

I can explain:

- Bronze, Silver, and Gold architecture
- How Python pipeline works
- How validation rules are applied
- How data is enriched using lookups
- How SQL reports use clean data
- Why invalid data should not be used for revenue

---

## What I Would Improve Next

Possible improvements:

- Add automated data quality tests
- Add logging system
- Add error handling for missing files
- Move pipeline into Databricks notebooks
- Add scheduling with workflow tools
- Connect pipeline with a real database
