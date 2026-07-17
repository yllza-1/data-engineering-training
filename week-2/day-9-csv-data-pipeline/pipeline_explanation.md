# Pipeline Explanation - Day 9

## Source Data

The source data consists of three CSV files:

- orders.csv
- customers.csv
- products.csv

These files contain the raw data used by the pipeline.

## Ingestion

The pipeline loads the CSV files using the `load_csv()` function. The data is read into Python lists of dictionaries so it can be validated, cleaned, and processed.

## Bronze Layer

The Bronze layer contains the original CSV files exactly as they were received. No changes are made to the data in this layer.

Files:

- orders.csv
- customers.csv
- products.csv

## Cleaning Rules

The pipeline cleans the data by:

- Normalizing status values.
- Normalizing city names.
- Normalizing channel values.
- Normalizing order date formats.
- Calculating the total amount for valid orders.

## Validation Rules

Each order is validated by checking:

- Order ID is present.
- Customer ID exists.
- Product ID exists.
- Order date is present.
- Quantity is a positive integer.
- Status is valid.

Invalid orders are excluded from the clean dataset.

## Silver Layer

The Silver layer contains validated and enriched data.

Files:

- output/orders_clean.csv
- output/invalid_orders.csv
- output/data_quality_report.txt

## Transformation Rules

The cleaned data is transformed by:

- Counting orders by status and city.
- Calculating completed revenue.
- Calculating revenue by category.
- Calculating revenue by channel.
- Finding the top customers.
- Finding the top products.
- Finding the most valuable completed order.

## Gold Layer

The Gold layer contains business-ready information created from the clean data.

File:

- output/business_summary.txt

## Business Output

The business summary includes:

- Completed revenue.
- Orders by status.
- Orders by city.
- Revenue by category.
- Revenue by channel.
- Top 3 customers.
- Top 3 products.
- Most valuable completed order.
- Business recommendation.

## What Makes This Data Trusted

The data is trusted because:

- Invalid records are removed.
- Values are normalized before processing.
- Revenue is calculated only from completed orders.
- All reports are generated from the cleaned data instead of the raw data.
