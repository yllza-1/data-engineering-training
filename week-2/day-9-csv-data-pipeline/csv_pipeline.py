import csv
import os
from datetime import datetime

def write_csv(file_path, rows, fieldnames):

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def load_csv(file_path):
    data = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


def load_orders():
    orders = load_csv("data/orders_raw.csv")
    print(f"Raw orders loaded: {len(orders)}")
    return orders


def load_customers():
    customers = load_csv("data/customers_raw.csv")
    print(f"Customers loaded: {len(customers)}")
    return customers


def load_products():
    products = load_csv("data/products_raw.csv")
    print(f"Products loaded: {len(products)}")
    return products


def build_lookup_table(rows, key_field):
    lookup = {}

    for row in rows:
        lookup[row[key_field]] = row

    return lookup

def normalize_status(status):
    status = status.strip().lower()

    status_map = {
        "completed": "completed",
        "complete": "completed",
        "done": "completed",
        "pending": "pending",
        "cancelled": "cancelled",
        "canceled": "cancelled"
    }

    return status_map.get(status, status)

def normalize_city(city):
    city = city.strip().lower()

    city_map = {
        "prishtina": "Prishtina",
        "vushtrri": "Vushtrri"
    }

    return city_map.get(city, city.title())

def normalize_channel(channel):
    channel = channel.strip().lower()

    channel_map = {
        "online": "online",
        "web": "online",
        "store": "store",
        "": "unknown"
    }

    return channel_map.get(channel, channel)

def normalize_category(category):
    category = category.strip().lower()

    category_map = {
        "accessories": "Accessories",
        "electronics": "Electronics",
        "furniture": "Furniture"
    }

    return category_map.get(category, category.title())


def normalize_order_date(order_date):

    formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%m-%d-%Y"
    ]

    for date_format in formats:
        try:
            date = datetime.strptime(order_date, date_format)
            return date.strftime("%Y-%m-%d")
        except ValueError:
            pass

    return order_date


def is_positive_integer(value):
    try:
        return int(value) > 0
    except ValueError:
        return False
    

def validate_order(order, customers_lookup, products_lookup):

    if not order["order_id"]:
        return False, "missing_order_id"

    if not order["customer_id"]:
        return False, "missing_customer_id"

    if order["customer_id"] not in customers_lookup:
        return False, "invalid_customer_id"

    if not order["product_id"]:
        return False, "missing_product_id"

    if order["product_id"] not in products_lookup:
        return False, "invalid_product_id"

    if not order["order_date"]:
        return False, "missing_order_date"

    quantity = order["quantity"]

    if not quantity:
        return False, "missing_quantity"

    try:
        quantity = int(quantity)

        if quantity < 0:
            return False, "negative_quantity"

        if quantity == 0:
            return False, "invalid_quantity"

    except ValueError:
        return False, "invalid_quantity"


    if not order["status"]:
      return False, "missing_status"

    status = normalize_status(order["status"])

    if status not in ["completed", "pending", "cancelled"]:
      return False, "invalid_status"

    channel = normalize_channel(order["channel"])

    if channel not in ["online", "store", "unknown"]:
        return False, "invalid_channel"

    return True, "valid"


def calculate_total_amount(order):
    quantity = int(order["quantity"])
    price = int(order["price"])

    return quantity * price


def enrich_order(order, customers_lookup, products_lookup):

    customer = customers_lookup[order["customer_id"]]
    product = products_lookup[order["product_id"]]

    enriched_order = {
        "order_id": order["order_id"],
        "customer_id": order["customer_id"],
        "customer_name": customer["customer_name"],
        "city": normalize_city(customer["city"]),
        "product_id": order["product_id"],
        "product_name": product["product_name"],
        "category": normalize_category(product["category"]),
        "quantity": int(order["quantity"]),
        "price": int(product["price"]),    
        "status": normalize_status(order["status"]),
        "channel": normalize_channel(order["channel"]),
        "order_date": normalize_order_date(order["order_date"])
    }

    enriched_order["total_amount"] = calculate_total_amount(enriched_order)

    return enriched_order

def create_clean_orders(orders, customers_lookup, products_lookup):

    clean_orders = []
    invalid_orders = []

    for order in orders:

        is_valid, reason = validate_order(
            order,
            customers_lookup,
            products_lookup
        )

        if is_valid:
            clean_orders.append(
                enrich_order(
                    order,
                    customers_lookup,
                    products_lookup
                )
            )
        else:
            order["reason"] = reason
            invalid_orders.append(order)

    return clean_orders, invalid_orders


def create_data_quality_report(raw_orders, clean_orders, invalid_orders):

    os.makedirs("output", exist_ok=True)

    invalid_reasons = {}

    for order in invalid_orders:
        reason = order["reason"]

        if reason in invalid_reasons:
            invalid_reasons[reason] += 1
        else:
            invalid_reasons[reason] = 1

    with open("output/data_quality_report.txt", "w") as file:

        file.write("Data Quality Report - Day 9\n\n")

        file.write(f"Total raw orders: {len(raw_orders)}\n")
        file.write(f"Valid orders: {len(clean_orders)}\n")
        file.write(f"Invalid orders: {len(invalid_orders)}\n\n")

        file.write("Invalid records by reason:\n")
        for reason in invalid_reasons:
            file.write(f"{reason}: {invalid_reasons[reason]}\n")

        file.write("\nStatus values after cleaning:\n")
        for status in set(order["status"] for order in clean_orders):
            file.write(f"{status}\n")

        file.write("\nChannel values after cleaning:\n")
        for channel in set(order["channel"] for order in clean_orders):
            file.write(f"{channel}\n")

        file.write("\nCity values after cleaning:\n")
        for city in set(order["city"] for order in clean_orders):
            file.write(f"{city}\n")

        file.write("\nBronze input files checked:\n")
        file.write("orders.csv\n")
        file.write("customers.csv\n")
        file.write("products.csv\n")

        file.write("\nSilver output files created:\n")
        file.write("orders_clean.csv\n")
        file.write("invalid_orders.csv\n")

        file.write("\nMain data quality problems found:\n")
        for reason in invalid_reasons:
            file.write(f"{reason}: {invalid_reasons[reason]}\n")

def get_completed_orders(rows):

    completed_orders = []

    for row in rows:
        if row["status"] == "completed":
            completed_orders.append(row)

    return completed_orders

def count_by_field(rows, field_name):

    counts = {}

    for row in rows:
        value = row[field_name]

        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    return counts

def sum_by_field(rows, group_field, amount_field):

    totals = {}

    for row in rows:
        group = row[group_field]
        amount = float(row[amount_field])

        if group in totals:
            totals[group] += amount
        else:
            totals[group] = amount

    return totals

def get_top_n_by_field(rows, field_name, n):

    totals = sum_by_field(rows, field_name, "total_amount")

    sorted_totals = sorted(
        totals.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_totals[:n]

def create_business_summary(clean_orders):

    completed_orders = get_completed_orders(clean_orders)

    completed_revenue = 0

    for order in completed_orders:
        completed_revenue += float(order["total_amount"])

    orders_by_status = count_by_field(clean_orders, "status")
    orders_by_city = count_by_field(clean_orders, "city")

    revenue_by_category = sum_by_field(
        completed_orders,
        "category",
        "total_amount"
    )

    revenue_by_channel = sum_by_field(
        completed_orders,
        "channel",
        "total_amount"
    )

    top_customers = get_top_n_by_field(
        completed_orders,
        "customer_name",
        3
    )

    top_products = get_top_n_by_field(
        completed_orders,
        "product_name",
        3
    )

    most_valuable_order = max(
        completed_orders,
        key=lambda order: float(order["total_amount"])
    )

    with open("output/business_summary.txt", "w") as file:

        file.write("Business Summary - Day 9\n\n")

        file.write(f"Completed revenue: {completed_revenue}\n\n")

        file.write("Orders by status:\n")
        for status, count in orders_by_status.items():
            file.write(f"{status}: {count}\n")

        file.write("\nOrders by city:\n")
        for city, count in orders_by_city.items():
            file.write(f"{city}: {count}\n")

        file.write("\nRevenue by category:\n")
        for category, revenue in revenue_by_category.items():
            file.write(f"{category}: {revenue}\n")

        file.write("\nRevenue by channel:\n")
        for channel, revenue in revenue_by_channel.items():
            file.write(f"{channel}: {revenue}\n")

        file.write("\nTop 3 customers by completed revenue:\n")
        for customer, revenue in top_customers:
            file.write(f"{customer}: {revenue}\n")

        file.write("\nTop 3 products by completed revenue:\n")
        for product, revenue in top_products:
            file.write(f"{product}: {revenue}\n")

        file.write("\nMost valuable completed order:\n")
        file.write(
            f'{most_valuable_order["order_id"]} - '
            f'{most_valuable_order["customer_name"]} - '
            f'{most_valuable_order["total_amount"]}\n'
        )

        file.write("\nOrders that should not count as revenue:\n")
        file.write(f"{len(clean_orders) - len(completed_orders)}\n")

        file.write("\nBusiness recommendation:\n")
        file.write("Focus on increasing completed orders and reducing cancelled orders.\n")

        file.write("\nWhy this Gold output can be trusted:\n")
        file.write("Only completed orders are included in revenue.\n")
        file.write("Pending and cancelled orders are excluded from revenue.\n")
        file.write("All numbers are calculated from clean data.\n")

def find_duplicate_order_ids(rows):

    seen = set()
    duplicates = []

    for row in rows:
        order_id = row["order_id"]

        if order_id in seen:
            duplicates.append(order_id)
        else:
            seen.add(order_id)

    return duplicates

def create_completed_orders_csv(completed_orders, fieldnames):

    write_csv(
        "output/completed_orders.csv",
        completed_orders,
        fieldnames
    )

def create_revenue_by_city_report(completed_orders):

    revenue = sum_by_field(
        completed_orders,
        "city",
        "total_amount"
    )

    sorted_revenue = sorted(
        revenue.items(),
        key=lambda item: item[1],
        reverse=True
    )

    with open("output/revenue_by_city.txt", "w") as file:

        file.write("Revenue by City\n\n")

        for city, amount in sorted_revenue:
            file.write(f"{city}: {amount}\n")

def create_revenue_by_category_report(completed_orders):

    revenue = sum_by_field(
        completed_orders,
        "category",
        "total_amount"
    )

    sorted_revenue = sorted(
        revenue.items(),
        key=lambda item: item[1],
        reverse=True
    )

    with open("output/revenue_by_category.txt", "w") as file:

        file.write("Revenue by Category\n\n")

        for category, amount in sorted_revenue:
            file.write(f"{category}: {amount}\n")

def create_top_customers_report(completed_orders):

    top_customers = get_top_n_by_field(
        completed_orders,
        "customer_name",
        3
    )

    with open("output/top_customers.txt", "w") as file:

        file.write("Top Customers\n\n")

        for customer, revenue in top_customers:
            file.write(f"{customer}: {revenue}\n")

def create_top_products_report(completed_orders):

    top_products = get_top_n_by_field(
        completed_orders,
        "product_name",
        3
    )

    with open("output/top_products.txt", "w") as file:

        file.write("Top Products\n\n")

        for product, revenue in top_products:
            file.write(f"{product}: {revenue}\n")

def create_cleaning_log():

    with open("output/cleaning_log.txt", "w") as file:

        file.write("Cleaning Log\n\n")
        file.write("- Normalized status values.\n")
        file.write("- Normalized city names.\n")
        file.write("- Normalized channel values.\n")
        file.write("- Validated customer IDs.\n")
        file.write("- Validated product IDs.\n")
        file.write("- Removed invalid records.\n")
        file.write("- Calculated total_amount.\n")

def run_tests():

    print("\nTest Results")

    print(normalize_status("Complete") == "completed")
    print(normalize_channel("Online") == "online")
    print(is_positive_integer("5") == True)
    print(is_positive_integer("-5") == False)


def main():

    # 1. Load raw CSV files
    orders = load_orders()
    customers = load_customers()
    products = load_products()

    # 2. Build lookup tables
    customers_lookup = build_lookup_table(customers, "customer_id")
    products_lookup = build_lookup_table(products, "product_id")

    # Normalize customer, product and order data
    for customer in customers:
        customer["city"] = normalize_city(customer["city"])

    for product in products:
        product["category"] = normalize_category(product["category"])

    for order in orders:
        order["status"] = normalize_status(order["status"])
        order["channel"] = normalize_channel(order["channel"])
        order["order_date"] = normalize_order_date(order["order_date"])

    # Bonus - Check duplicate order IDs
    duplicates = find_duplicate_order_ids(orders)

    if duplicates:
        print("Duplicate order IDs:", duplicates)
    else:
        print("No duplicate order IDs found.")

    # 3. Validate and clean orders
    clean_orders, invalid_orders = create_clean_orders(
        orders,
        customers_lookup,
        products_lookup
    )

    os.makedirs("output", exist_ok=True)

    clean_fieldnames = [
        "order_id",
        "customer_id",
        "customer_name",
        "city",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "price",
        "total_amount",
        "status",
        "channel",
        "order_date"
    ]

    # 4. Enrich valid orders
    # (Enrichment is done inside create_clean_orders)

    # 5. Write clean and invalid CSV files
    write_csv(
        "output/orders_clean.csv",
        clean_orders,
        clean_fieldnames
    )

    if invalid_orders:
        invalid_fieldnames = list(invalid_orders[0].keys())

        write_csv(
            "output/invalid_orders.csv",
            invalid_orders,
            invalid_fieldnames
        )

    print("Valid orders:", len(clean_orders))
    print("Invalid orders:", len(invalid_orders))

    # 6. Create data quality report
    create_data_quality_report(
        orders,
        clean_orders,
        invalid_orders
    )

    # 7. Create business summary report
    create_business_summary(clean_orders)

    # Bonus outputs
    completed_orders = get_completed_orders(clean_orders)

    create_completed_orders_csv(
        completed_orders,
        clean_fieldnames
    )

    create_revenue_by_city_report(completed_orders)

    create_revenue_by_category_report(completed_orders)

    create_top_customers_report(completed_orders)

    create_top_products_report(completed_orders)

    create_cleaning_log()

    run_tests()


if __name__ == "__main__":
    main()