# Day 2 Practice - CSV Mini Data Pipeline

## Overview

This project is a simple data pipeline built with Python. It reads a raw CSV file containing student information, identifies data quality issues, cleans the data, calculates student performance, and generates reports.

The goal of the project is to practice working with CSV files, data cleaning techniques, and basic data processing using Python.

## Files Included

- `data/students_raw.csv` – Raw student data
- `output/students_clean.csv` – Cleaned student dataset
- `output/data_quality_report.txt` – Data quality report
- `output/summary_report.txt` – Final summary report
- `csv_pipeline.py` – Main Python program
- `README.md` – Project documentation

## Input File

The project uses one input file:

- `data/students_raw.csv`

This file contains raw student data, including:

- Student ID
- Name
- City
- Course
- Age
- Attendance
- Homework Score
- Registration Date

Some records intentionally contain missing values, invalid numbers, and inconsistent text to simulate real-world datasets.

## Output Files

After running the program, the following files are created inside the `output` folder:

### `students_clean.csv`

Contains the cleaned dataset with additional calculated columns:

- `total_score`
- `performance_status`
- `risk_flag`

### `data_quality_report.txt`

Lists all detected data quality issues, including:

- Missing values
- Invalid numeric values
- Inconsistent text values

### `summary_report.txt`

Contains a summary of the cleaned dataset, including:

- Total records
- Average attendance
- Average homework score
- Students by city
- Students by course
- Strong students
- Students needing support
- At Risk students
- Top 3 students by total score

## How to Run

Open the project folder in the terminal and run:

```bash
python3 csv_pipeline.py
```

## Features

- Read CSV files
- Inspect dataset structure
- Detect data quality issues
- Clean missing and invalid values
- Standardize text values
- Calculate total scores
- Classify student performance
- Identify students at risk
- Export cleaned CSV
- Generate quality and summary reports

## Concepts Practiced

- Python functions
- CSV file handling
- Lists and dictionaries
- Loops
- Conditional statements
- Error handling (`try` / `except`)
- Data cleaning
- File writing
- Report generation
- Project organization with GitHub

## Author

**Yllza Azemi**

Unity Tech Hub × Agilyti  
Data Engineering / Databricks Training
=======

# Student Report

This project is made with Python and works with student data.

It calculates averages, groups students by city and course, and creates a final report in the terminal.

This is a practice exercise for Data Engineering.
