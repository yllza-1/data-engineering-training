# Day 6 - SQL Business Reporting Sprint

## Goal of the Practice

The goal of this practice is to learn how SQL can be used for business reporting.
We worked with tables, aggregation functions, GROUP BY, HAVING, and JOIN queries to analyze data and answer business questions.

## Files Included

- setup.sql - Creates tables and inserts sample data.
- basic_aggregation.sql - Contains basic calculations using SQL functions.
- group_by_reports.sql - Contains reports using GROUP BY.
- having_reports.sql - Contains filtered reports using HAVING.
- join_reports.sql - Contains queries that combine data from multiple tables.
- query_explanations.md - Explains important business queries.

## How to Run the SQL Files

Run the SQL files in this order:

1. Open SQLiteOnline.com.
2. Select SQLite database.
3. Run setup.sql first to create the tables and add data.
4. Run basic_aggregation.sql.
5. Run group_by_reports.sql.
6. Run having_reports.sql.
7. Run join_reports.sql.
8. Check query_explanations.md for explanations of the main queries.

## Tool Used

SQLiteOnline.com was used to create tables, insert data, and test all SQL queries.

## SQL Concepts Explanation

### Basic Aggregation

Basic aggregation is used to calculate simple results from data.
Functions like COUNT(), SUM(), AVG(), MIN(), and MAX() help us find totals, averages, and other important values.

### GROUP BY

GROUP BY is used to organize data into groups based on a specific column.
For example, we can group orders by category to see how much revenue each category generated.

### HAVING

HAVING is used to filter grouped results after using GROUP BY.
It helps us show only groups that meet a specific condition, such as categories with revenue higher than a certain amount.

### JOIN

JOIN is used to combine data from multiple tables.
It allows us to get more complete information by connecting related data, such as orders with product details.

## Business Insight Found

The most important business insight found was identifying which product categories generated the highest completed revenue.
This helps the business understand which products perform better and where to focus future sales strategies.
