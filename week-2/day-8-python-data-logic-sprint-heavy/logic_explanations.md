# Logic Explanations

## 1. Why did I do validation before revenue calculation?

I validated the records before calculating revenue to make sure only correct data is used. Records with an empty customer name, quantity less than or equal to zero, or price less than or equal to zero are invalid. If these records were included, the revenue would be incorrect. After validation, only valid records are used for all business metrics.

---

## 2. How does status normalization work?

The status normalization function converts different versions of the same status into one standard value.

For example:

- Completed → completed
- complete → completed
- Pending → pending
- Cancelled → cancelled
- Returned → returned

This makes all status values consistent so they can be counted and filtered correctly.

---

## 3. Why do only completed orders count as revenue?

Revenue should only come from completed orders because those orders represent successful sales.

Pending orders are not finished yet.

Cancelled orders were never completed.

Returned orders were refunded or returned by the customer.

Including these orders would make the revenue incorrect.

---

## 4. How does count_by_field work?

The function starts with an empty dictionary.

It loops through every record.

For each record it reads the selected field, such as city, category, or status.

If the value is not already in the dictionary, it creates it with a value of 0.

Then it increases the count by 1.

After all records are processed, the dictionary contains the count for every unique value.

---

## 5. How does sum_revenue_by_field work?

The function starts with an empty dictionary.

It loops through all cleaned records.

It only processes records where the status is completed.

For each completed order it gets the selected field, such as customer, city, category, or channel.

If the value does not exist in the dictionary, it creates it with a revenue of 0.

Then it adds the order's total_amount to the existing revenue.

When the loop finishes, the dictionary contains the completed revenue for every value.

---

## 6. How is sorting used to find top records?

The program uses the sorted() function with reverse=True.

The records are sorted from the highest value to the lowest value.

After sorting, the first records in the list are the top records.

For example, the first five completed orders after sorting are the Top 5 completed orders.

---

## 7. What does main() do and why does it improve the script structure?

The main() function controls the entire program.

It calls all the other functions in the correct order.

It prints the raw data, validates records, creates cleaned records, calculates business metrics, generates rankings, and prints the final investigation.

Using main() keeps the code organized, easier to read, and easier to maintain because each function has a single responsibility.

---

## 8. Explain one metric from the report.

Completed Revenue

The function starts with a revenue value of 0.

It loops through every cleaned order.

If the order status is completed, it adds the order's total_amount to the revenue.

Orders with pending, cancelled, or returned status are ignored.

When the loop finishes, the function returns the total completed revenue.
