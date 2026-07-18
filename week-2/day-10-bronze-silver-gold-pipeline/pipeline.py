import csv
from datetime import datetime
import os

def ensure_output_folders():
    os.makedirs("data/silver", exist_ok=True)
    os.makedirs("data/gold", exist_ok=True)


def load_csv(file_path):
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_csv(file_path, rows, fieldnames):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def normalize_status(status):
    status = status.lower()

    if status in ["completed", "complete", "done"]:
        return "completed"

    if status in ["cancelled", "canceled"]:
        return "cancelled"

    if status == "pending":
        return "pending"

    return status

def normalize_channel(channel):
    channel = channel.strip().lower()

    if channel in ["online", "web", "mobile"]:
        return "online"

    if channel == "store":
        return "store"

    if channel == "":
        return "unknown"

    return channel

def normalize_city(city):
    if not city:
        return "Unknown"

    city = city.strip().lower()

    if city == "prishtina":
        return "Prishtina"

    if city == "vushtrri":
        return "Vushtrri"

    return city.title()

def is_positive_integer(value):
    try:
        return int(value) > 0
    except ValueError:
        return False
    
def is_positive_number(value):
    try:
        return float(value) > 0
    except ValueError:
        return False
    
def customer_exists(customer_id, customers_lookup):
    return customer_id in customers_lookup


def product_exists(product_id, products_lookup):
    return product_id in products_lookup


def duplicate_order(order_id, seen_order_ids):
    if order_id in seen_order_ids:
        return True

    seen_order_ids.add(order_id)
    return False

def normalize_category(category):
    if not category:
        return "Unknown"

    return category

def normalize_order_date(order_date):
    if not order_date:
        return ""

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

def clean_customers(customers):
    clean_customers = []
    customers_lookup = {}

    for customer in customers:
        customer["city"] = normalize_city(customer["city"])
        clean_customers.append(customer)
        customers_lookup = build_lookup(clean_customers, "customer_id")

    return clean_customers, customers_lookup

def clean_products(products):
    clean_products = []
    products_lookup = {}

    for product in products:
        product["category"] = normalize_category(product["category"])

        if not is_positive_number(product["price"]):
            continue

        clean_products.append(product)
        products_lookup[product["product_id"]] = product
        products_lookup = build_lookup(clean_products, "product_id")

    return clean_products, products_lookup

def validate_order(order, customers_lookup, products_lookup, seen_order_ids):

    if not customer_exists(order["customer_id"], customers_lookup):
        return False, "invalid_customer_id"

    if not product_exists(order["product_id"], products_lookup):
        return False, "invalid_product_id"

    if duplicate_order(order["order_id"], seen_order_ids):
        return False, "duplicate_order_id"

    if not order["order_date"]:
        return False, "missing_order_date"

    if not is_positive_integer(order["quantity"]):
        return False, "invalid_quantity"

    return True, ""


def enrich_order(order, customers_lookup, products_lookup):
    customer = customers_lookup[order["customer_id"]]
    product = products_lookup[order["product_id"]]

    return {
        "order_id": order["order_id"],
        "customer_id": order["customer_id"],
        "customer_name": customer["customer_name"],
        "city": customer["city"],
        "product_id": order["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "quantity": order["quantity"],
        "price": product["price"],
        "total_amount": int(order["quantity"]) * float(product["price"]),
        "status": order["status"],
        "channel": order["channel"],
        "order_date": order["order_date"]
    }


def create_silver_orders(orders, customers_lookup, products_lookup):
    clean_orders = []
    invalid_orders = []
    seen_order_ids = set()

    for order in orders:

        order["status"] = normalize_status(order["status"])
        order["channel"] = normalize_channel(order["channel"])
        order["order_date"] = normalize_order_date(order["order_date"])

        valid, reason = validate_order(
            order,
            customers_lookup,
            products_lookup,
            seen_order_ids
        )

        if valid:
            clean_order = enrich_order(
                order,
                customers_lookup,
                products_lookup
            )

            clean_orders.append(clean_order)

        else:
            invalid_order = {
                "order_id": order["order_id"],
                "customer_id": order["customer_id"],
                "product_id": order["product_id"],
                "order_date": order["order_date"],
                "quantity": order["quantity"],
                "status": order["status"],
                "channel": order["channel"],
                "reason": reason
            }

            invalid_orders.append(invalid_order)

    return clean_orders, invalid_orders


def create_revenue_by_category(orders):
    report = {}

    for order in orders:
        if order["status"] != "completed":
            continue

        category = order["category"]

        if category not in report:
            report[category] = {
                "category": category,
                "completed_revenue": 0,
                "total_completed_orders": 0
            }

        report[category]["completed_revenue"] += float(order["total_amount"])
        report[category]["total_completed_orders"] += 1

    write_csv(
        "data/gold/revenue_by_category.csv",
        list(report.values()),
        ["category", "completed_revenue", "total_completed_orders"]
    )

def build_lookup(rows, key_field):
    lookup = {}

    for row in rows:
        lookup[row[key_field]] = row

    return lookup

def create_revenue_by_city(orders):
    report = {}

    for order in orders:
        if order["status"] != "completed":
            continue

        city = order["city"]

        if city not in report:
            report[city] = {
                "city": city,
                "completed_revenue": 0,
                "total_completed_orders": 0
            }

        report[city]["completed_revenue"] += float(order["total_amount"])
        report[city]["total_completed_orders"] += 1

    write_csv(
        "data/gold/revenue_by_city.csv",
        list(report.values()),
        ["city", "completed_revenue", "total_completed_orders"]
    )


def create_revenue_by_customer(orders):
    report = {}

    for order in orders:
        if order["status"] != "completed":
            continue

        customer = order["customer_name"]

        if customer not in report:
            report[customer] = {
                "customer_name": customer,
                "city": order["city"],
                "completed_revenue": 0,
                "total_completed_orders": 0
            }

        report[customer]["completed_revenue"] += float(order["total_amount"])
        report[customer]["total_completed_orders"] += 1

    write_csv(
        "data/gold/revenue_by_customer.csv",
        list(report.values()),
        ["customer_name", "city", "completed_revenue", "total_completed_orders"]
    )


def create_top_products(orders):
    report = {}

    for order in orders:
        if order["status"] != "completed":
            continue

        product = order["product_name"]

        if product not in report:
            report[product] = {
                "product_name": product,
                "category": order["category"],
                "total_quantity_sold": 0,
                "completed_revenue": 0
            }

        report[product]["total_quantity_sold"] += int(order["quantity"])
        report[product]["completed_revenue"] += float(order["total_amount"])

    write_csv(
        "data/gold/top_products.csv",
        list(report.values()),
        ["product_name", "category", "total_quantity_sold", "completed_revenue"]
    )

def create_executive_summary(raw_orders, clean_orders, invalid_orders):
    completed_orders = 0
    pending_orders = 0
    cancelled_orders = 0
    completed_revenue = 0

    category_revenue = {}
    city_revenue = {}
    customer_revenue = {}
    product_revenue = {}
    invalid_reasons = {}

    for order in clean_orders:

        if order["status"] == "completed":
            completed_orders += 1
            revenue = int(order["total_amount"])
            completed_revenue += revenue

            category_revenue[order["category"]] = category_revenue.get(order["category"], 0) + revenue
            city_revenue[order["city"]] = city_revenue.get(order["city"], 0) + revenue
            customer_revenue[order["customer_name"]] = customer_revenue.get(order["customer_name"], 0) + revenue
            product_revenue[order["product_name"]] = product_revenue.get(order["product_name"], 0) + revenue

        elif order["status"] == "pending":
            pending_orders += 1

        elif order["status"] == "cancelled":
            cancelled_orders += 1

    for order in invalid_orders:
        reason = order["reason"]
        invalid_reasons[reason] = invalid_reasons.get(reason, 0) + 1

    top_category = max(category_revenue, key=category_revenue.get)
    top_city = max(city_revenue, key=city_revenue.get)
    top_customer = max(customer_revenue, key=customer_revenue.get)
    top_product = max(product_revenue, key=product_revenue.get)
    most_common_invalid_reason = max(invalid_reasons, key=invalid_reasons.get)

    with open("data/gold/executive_summary.txt", "w", encoding="utf-8") as file:

        file.write("Executive Summary - Day 10 Pipeline\n\n")

        file.write(f"Total raw orders: {len(raw_orders)}\n")
        file.write(f"Valid silver orders: {len(clean_orders)}\n")
        file.write(f"Invalid orders: {len(invalid_orders)}\n")
        file.write(f"Completed orders: {completed_orders}\n")
        file.write(f"Pending orders: {pending_orders}\n")
        file.write(f"Cancelled orders: {cancelled_orders}\n")
        file.write(f"Completed revenue: {completed_revenue:.2f}\n")
        file.write(f"Top category: {top_category}\n")
        file.write(f"Top city: {top_city}\n")
        file.write(f"Top customer: {top_customer}\n")
        file.write(f"Top product: {top_product}\n")
        file.write(f"Most common invalid reason: {most_common_invalid_reason}\n")
        file.write("Business recommendation: Focus on the top-performing category and products while reducing the most common data quality issue.\n")

def create_data_quality_report(raw_orders, clean_orders, invalid_orders):
    duplicate_order_ids = 0
    missing_dates = 0
    invalid_quantities = 0
    invalid_statuses = 0
    invalid_products = 0
    invalid_customers = 0
    invalid_product_prices = 0
    missing_customer_cities = 0

    reasons = {}

    valid_statuses = ["completed", "pending", "cancelled"]
    seen_order_ids = set()

    for order in raw_orders:

        if order["order_id"] in seen_order_ids:
            duplicate_order_ids += 1
        else:
            seen_order_ids.add(order["order_id"])

        if not order["order_date"]:
            missing_dates += 1

        if not is_positive_integer(order["quantity"]):
            invalid_quantities += 1

        if normalize_status(order["status"]) not in valid_statuses:
            invalid_statuses += 1

    for order in invalid_orders:
        reason = order["reason"]
        reasons[reason] = reasons.get(reason, 0) + 1

        if reason == "invalid_customer_id":
            invalid_customers += 1

        elif reason == "invalid_product_id":
            invalid_products += 1

    with open("data_quality_report.txt", "w", encoding="utf-8") as file:

        file.write("Validation Checks\n\n")

        file.write(f"Raw orders count: {len(raw_orders)}\n")
        file.write(f"Silver clean orders count: {len(clean_orders)}\n")
        file.write(f"Invalid orders count: {len(invalid_orders)}\n")

        if len(raw_orders) == len(clean_orders) + len(invalid_orders):
            file.write("Raw = Silver + Invalid: YES\n")
        else:
            file.write("Raw = Silver + Invalid: NO\n")

        file.write(f"Customer IDs checked: {len(raw_orders)}\n")
        file.write(f"Product IDs checked: {len(raw_orders)}\n")
        file.write(f"Duplicate order IDs found: {duplicate_order_ids}\n")
        file.write(f"Missing dates found: {missing_dates}\n")
        file.write(f"Invalid quantities found: {invalid_quantities}\n")
        file.write(f"Invalid statuses found: {invalid_statuses}\n")
        file.write(f"Invalid products found: {invalid_products}\n")
        file.write(f"Invalid customers found: {invalid_customers}\n")
        file.write(f"Invalid product prices found: {invalid_product_prices}\n")
        file.write(f"Missing customer cities found: {missing_customer_cities}\n")

        file.write("\nInvalid records by reason:\n")

        for reason, count in reasons.items():
            file.write(f"- {reason}: {count}\n")

def create_pipeline_log():
    with open("pipeline_log.txt", "w", encoding="utf-8") as file:
        file.write("Pipeline Log - Day 10\n\n")
        file.write("Step 1: Loaded Bronze files.\n")
        file.write("Step 2: Cleaned customers.\n")
        file.write("Step 3: Cleaned products.\n")
        file.write("Step 4: Validated orders.\n")
        file.write("Step 5: Created Silver clean orders.\n")
        file.write("Step 6: Created invalid orders file.\n")
        file.write("Step 7: Created Gold revenue reports.\n")
        file.write("Step 8: Created executive summary.\n")
        file.write("Pipeline completed successfully.\n")

def create_revenue_by_channel(orders):
    report = {}

    for order in orders:
        if order["status"] != "completed":
            continue

        channel = order["channel"]

        if channel not in report:
            report[channel] = {
                "channel": channel,
                "completed_revenue": 0,
                "total_completed_orders": 0
            }

        report[channel]["completed_revenue"] += float(order["total_amount"])
        report[channel]["total_completed_orders"] += 1

    rows = sorted(
        report.values(),
        key=lambda x: x["completed_revenue"],
        reverse=True
    )

    write_csv(
        "data/gold/revenue_by_channel.csv",
        rows,
        ["channel", "completed_revenue", "total_completed_orders"]
    )

def create_invalid_reasons_summary(invalid_orders):
    report = {}

    for order in invalid_orders:
        reason = order["reason"]
        report[reason] = report.get(reason, 0) + 1

    rows = []

    for reason, count in report.items():
        rows.append({
            "reason": reason,
            "count": count
        })

    write_csv(
        "data/gold/invalid_reasons_summary.csv",
        rows,
        ["reason", "count"]
    )
def products_never_sold(products, orders):

    sold = set()

    for order in orders:
        if order["status"] == "completed":
            sold.add(order["product_id"])

    with open("products_never_sold.txt", "w") as file:

        for product in products:
            if product["product_id"] not in sold:
                file.write(product["product_name"] + "\n")

def customers_never_ordered(customers, orders):

    ordered = set()

    for order in orders:
        ordered.add(order["customer_id"])

    with open("customers_never_ordered.txt", "w") as file:

        for customer in customers:
            if customer["customer_id"] not in ordered:
                file.write(customer["customer_name"] + "\n")
            

def create_dashboard_data(orders):

    revenue = 0
    completed = 0

    for order in orders:

        if order["status"] == "completed":
            completed += 1
            revenue += float(order["total_amount"])

    row = [{
        "total_orders": len(orders),
        "completed_orders": completed,
        "completed_revenue": revenue
    }]

    write_csv(
        "data/gold/dashboard_data.csv",
        row,
        ["total_orders", "completed_orders", "completed_revenue"]
    )

def create_pipeline_summary():

    with open("pipeline_summary.md", "w", encoding="utf-8") as file:

        file.write("# Pipeline Summary\n\n")

        file.write("## Source Data\n")
        file.write("orders_raw.csv, customers_raw.csv, products_raw.csv\n\n")

        file.write("## Ingestion\n")
        file.write("CSV files are loaded using Python.\n\n")

        file.write("## Storage\n")
        file.write("Bronze -> Silver -> Gold\n\n")

        file.write("## Cleaning\n")
        file.write("Normalize and validate data.\n\n")

        file.write("## Transformation\n")
        file.write("Enrich orders and calculate total_amount.\n\n")

        file.write("## Business Output\n")
        file.write("Revenue reports, executive summary and dashboard data.\n")


def main():
    ensure_output_folders()
    orders = load_csv("data/bronze/orders_raw.csv")
    customers = load_csv("data/bronze/customers_raw.csv")
    products = load_csv("data/bronze/products_raw.csv")

    print("Bronze Layer - Raw Data")
    print("Orders:", len(orders))
    print("Customers:", len(customers))
    print("Products:", len(products))

    clean_customers_data, customers_lookup = clean_customers(customers)

    clean_products_data, products_lookup = clean_products(products)

    orders_clean, invalid_orders = create_silver_orders(
        orders,
        customers_lookup,
        products_lookup
    )

    write_csv(
        "data/silver/customers_clean.csv",
        clean_customers_data,
        clean_customers_data[0].keys()
    )

    write_csv(
        "data/silver/products_clean.csv",
        clean_products_data,
        clean_products_data[0].keys()
    )

    if orders_clean:
        write_csv(
            "data/silver/orders_clean.csv",
            orders_clean,
            orders_clean[0].keys()
        )

    if invalid_orders:
        write_csv(
            "data/silver/invalid_orders.csv",
            invalid_orders,
            invalid_orders[0].keys()
        )

    print("\nSilver layer created successfully!")

    create_revenue_by_category(orders_clean)
    create_revenue_by_city(orders_clean)
    create_revenue_by_customer(orders_clean)
    create_top_products(orders_clean)
    create_executive_summary(
        orders,
        orders_clean,
        invalid_orders
    )

    create_data_quality_report(
    orders,
    orders_clean,
    invalid_orders
)

    create_pipeline_log()


    create_revenue_by_channel(orders_clean)
    create_invalid_reasons_summary(invalid_orders)
    products_never_sold(clean_products_data, orders_clean)
    customers_never_ordered(clean_customers_data, orders_clean)
    create_dashboard_data(orders_clean)
    create_pipeline_summary()

if __name__ == "__main__":
    main()