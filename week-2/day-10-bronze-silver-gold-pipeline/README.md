# Day 10 - Bronze / Silver / Gold Pipeline with Python

## Project goal

The goal of this project is to build a simple ETL pipeline using Python. The pipeline reads raw data from the Bronze layer, cleans and validates it in the Silver layer, and creates business-ready reports in the Gold layer.

---

## Bronze layer

The Bronze layer stores the original raw CSV files without changing them.

Files:

- orders_raw.csv
- customers_raw.csv
- products_raw.csv

The pipeline loads these files and counts the number of raw records before any cleaning is performed.

---

## Silver layer

The Silver layer cleans, validates, and enriches the data.

Cleaning rules:

- Normalize order status values.
- Normalize channel values.
- Normalize city names.
- Convert order dates to YYYY-MM-DD format.
- Replace missing product categories with "Unknown".
- Remove products with invalid prices.
- Validate customer IDs.
- Validate product IDs.
- Validate duplicate order IDs.
- Validate positive quantities.

Enrichment:

- Added customer_name.
- Added city.
- Added product_name.
- Added category.
- Added price.
- Added total_amount.

The Silver layer creates:

- customers_clean.csv
- products_clean.csv
- orders_clean.csv
- invalid_orders.csv

---

## Gold layer

The Gold layer creates business-ready reports using only the clean Silver data.

Generated reports:

- revenue_by_category.csv
- revenue_by_city.csv
- revenue_by_customer.csv
- top_products.csv
- executive_summary.txt
- data_quality_report.txt
- pipeline_log.txt

---

## How to run the pipeline

Run the following command:

```bash
python pipeline.py
```

The pipeline automatically:

- Loads Bronze files.
- Cleans and validates data.
- Creates Silver files.
- Creates Gold reports.
- Generates the summary, quality report, and pipeline log.

---

## Files generated

Silver:

- customers_clean.csv
- products_clean.csv
- orders_clean.csv
- invalid_orders.csv

Gold:

- revenue_by_category.csv
- revenue_by_city.csv
- revenue_by_customer.csv
- top_products.csv
- executive_summary.txt
- data_quality_report.txt
- pipeline_log.txt

---

## Data quality checks

The pipeline checks:

- Invalid customer IDs
- Invalid product IDs
- Duplicate order IDs
- Missing order dates
- Invalid quantities
- Invalid product prices
- Missing customer cities
- Invalid status values

Invalid orders are stored separately with the reason for failure.

---

## Business insights

The Gold reports show:

- Revenue by category
- Revenue by city
- Revenue by customer
- Top-selling products
- Total completed revenue
- Business summary
- Data quality statistics

These reports help identify the best-performing products, customers, and cities.

---

## What I can explain and defend

I can explain the complete ETL pipeline from Bronze to Silver and Gold.

I can explain:

- Why raw data should never be modified.
- How data is cleaned and validated.
- Why invalid orders are separated.
- How customer and product information is added during enrichment.
- How total_amount is calculated.
- How revenue reports are created from completed orders only.
- Why business reports should use Gold data instead of Bronze data.

The most important result I can defend is that all business reports are created only from validated Silver data, making the reports more accurate and reliable.

---

## What was difficult

The most challenging parts were:

- Building the validation logic.
- Handling duplicate order IDs.
- Creating lookup dictionaries.
- Generating business reports automatically.
- Organizing the project into reusable functions.

---

## What I would improve next

Future improvements:

- Add more validation rules.
- Generate charts automatically.
- Support larger datasets.
- Add logging with timestamps.
- Add unit tests.
- Improve error handling.
- Load file paths from a configuration file instead of hardcoding them.
