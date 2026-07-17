# Day 9 - CSV Data Pipeline: From Raw Data to Clean Reports

## Overview

The goal of this practice is to build a simple CSV data pipeline using Python. The pipeline reads raw CSV files, validates and cleans the data, enriches valid records, and generates reports based on the cleaned data.

This practice focuses on understanding how a data pipeline works before using external libraries.

---

## Bronze, Silver and Gold Layers

### Bronze

The Bronze layer contains the raw input CSV files without any changes.

Files:

- orders.csv
- customers.csv
- products.csv

### Silver

The Silver layer contains cleaned and validated data.

Generated files:

- output/orders_clean.csv
- output/invalid_orders.csv
- output/data_quality_report.txt

### Gold

The Gold layer contains business-ready information created from the cleaned data.

Generated file:

- output/business_summary.txt

---

## Project Structure

```
day-9-csv-data-pipeline/
│
├── input/
│   ├── orders.csv
│   ├── customers.csv
│   └── products.csv
│
├── output/
│   ├── orders_clean.csv
│   ├── invalid_orders.csv
│   ├── data_quality_report.txt
│   └── business_summary.txt
│
├── csv_pipeline.py
└── README.md
```

---

## How to Run

Run the script from the project folder:

```bash
python csv_pipeline.py
```

The script will:

- Load the CSV files.
- Validate and clean the data.
- Enrich valid orders.
- Create clean and invalid CSV files.
- Generate a data quality report.
- Generate a business summary report.

---

## Output Files

After running the script, the following files are created inside the `output` folder:

- `orders_clean.csv`
- `invalid_orders.csv`
- `data_quality_report.txt`
- `business_summary.txt`

---

## Why Pandas Was Not Used

This practice was completed without using the pandas library.

The purpose was to understand how CSV files, validation, cleaning, enrichment, aggregation, and reporting work using core Python. Learning the manual logic first provides a stronger foundation before using tools such as pandas in future data engineering projects.
