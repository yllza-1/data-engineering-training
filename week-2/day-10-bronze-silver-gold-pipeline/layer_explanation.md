# Layer Explanation - Day 10

## Bronze layer

### What files are stored here?

- orders_raw.csv
- customers_raw.csv
- products_raw.csv

### Why do we keep raw data unchanged?

Raw data is kept unchanged so we always have the original source. This allows us to trace errors, reprocess the data, and compare cleaned data with the original files.

### What data problems did you notice?

- Different status values (Completed, complete, done)
- Different channel values (Online, web, mobile)
- Different city name formats (prishtina, VUSHTRRI)
- Missing order dates
- Missing quantities
- Invalid quantities
- Duplicate order IDs
- Invalid customer IDs
- Invalid product IDs
- Missing product categories
- Invalid product prices

---

## Silver layer

### What cleaning rules did you apply?

- Normalized order status values
- Normalized sales channels
- Normalized city names
- Replaced missing product categories with "Unknown"
- Removed products with invalid prices
- Converted order dates to YYYY-MM-DD format
- Validated customer IDs
- Validated product IDs
- Checked duplicate order IDs
- Validated positive order quantities

### Which records became invalid and why?

Orders became invalid because of:

- Invalid customer ID
- Invalid product ID
- Duplicate order ID
- Missing order date
- Invalid quantity

### What columns were added during enrichment?

- customer_name
- city
- product_name
- category
- price
- total_amount

### Why is Silver safer than Bronze?

Silver contains cleaned, validated, and enriched data. Invalid records are removed, making the data more reliable for reporting.

---

## Gold layer

### Which reports did you create?

- revenue_by_category.csv
- revenue_by_city.csv
- revenue_by_customer.csv
- top_products.csv
- executive_summary.txt
- data_quality_report.txt

### Which business questions do these reports answer?

- Which category generates the most revenue?
- Which city has the highest revenue?
- Which customers generate the most revenue?
- Which products sell the most?
- What is the overall business performance?
- What are the main data quality issues?

### Why should dashboards use Gold outputs instead of raw Bronze data?

Gold data is already cleaned, validated, enriched, and aggregated. It provides accurate and trusted information for dashboards and business decisions.
