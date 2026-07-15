# Day 8 - Python Data Logic Sprint Heavy Version

## Business Scenario

This project analyzes raw order data from a Kosovo-based technology and office equipment business. The data contains inconsistent values and invalid records. The goal is to validate, clean, normalize, and analyze the data to produce accurate business metrics and reports.

## Files and Folders

- `order_data.py` – contains the raw orders dataset.
- `python_data_analysis.py` – contains all Python functions and analysis logic.
- `output/`
  - `business_report.txt`
  - `validation_report.txt`
  - `invalid_records.txt`

- `README.md`

## How to Run

Run the following command in the project folder:

```bash
python3 python_data_analysis.py
```

## Output Files

The script generates the following output files:

- `business_report.txt`
- `validation_report.txt`
- `invalid_records.txt`

## Main Python Concepts Practiced

- Functions
- Dictionaries
- Lists
- Loops
- Conditional statements
- Data validation
- Data cleaning and normalization
- File handling
- Business reporting

## What Was Difficult

The most challenging part of this practice was organizing the code into reusable functions and making the reports dynamic using dictionaries instead of hardcoding values. It also required careful validation and normalization to ensure that only valid completed orders were included in the final business metrics and revenue calculations.
