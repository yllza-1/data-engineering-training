import csv
import os

def load_csv(file_path):
    rows = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return rows

def write_csv(file_path, rows, fieldnames):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def ensure_folders():
    os.makedirs("data/silver",exist_ok=True)
    os.makedirs("data/gold",exist_ok=True)

def normalize_status(status):
    status = status.strip().lower()

    if status in ["completed", "done"]:
        return "completed"

    if status == "pending":
        return "pending"

    if status in ["cancelled", "canceled"]:
        return "cancelled"

    return status

def normalize_city(city):
    city = city.strip().lower()

    city_map = {
        "prishtina": "Prishtina",
        "vushtrri": "Vushtrri",
        "mitrovica": "Mitrovica",
        "peja": "Peja",
        "prizren": "Prizren",
        "ferizaj": "Ferizaj",
        "gjilan": "Gjilan"
    }

    return city_map.get(city, city.title())

def normalize_channel(channel):
    channel = channel.strip().lower()

    if channel == "":
        return "unknown"

    if channel in ["online", "store", "web", "bank"]:
        return channel

    return "unknown"

def build_lookup(rows, key):
    lookup = {}

    for row in rows:
        lookup[row[key]] = row

    return lookup

def validate_order(order, customers_lookup, products_lookup, seen_order_ids):

    if order["order_id"] in seen_order_ids:
        return False, "duplicate_order_id"

    if order["quantity"] == "":
        return False, "missing_quantity"

    try:
        if int(order["quantity"]) <= 0:
            return False, "invalid_quantity"
    except ValueError:
        return False, "invalid_quantity"

    if order["status"] == "":
        return False, "missing_status"

    if order["status"] not in ["completed", "pending", "cancelled"]:
        return False, "invalid_status"

    if order["order_date"] == "":
        return False, "missing_order_date"

    if order["customer_id"] not in customers_lookup:
        return False, "invalid_customer_id"

    if order["product_id"] not in products_lookup:
        return False, "invalid_product_id"

    return True, ""

def enrich_order(order, customers_lookup, products_lookup):

    customer = customers_lookup[order["customer_id"]]
    product = products_lookup[order["product_id"]]

    quantity = int(order["quantity"])
    price = float(product["price"])

    return {
        "order_id": order["order_id"],
        "customer_id": customer["customer_id"],
        "customer_name": customer["customer_name"],
        "city": normalize_city(customer["city"]),
        "segment": customer["segment"],
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "quantity": quantity,
        "price": price,
        "status": order["status"],
        "order_date": order["order_date"],
        "channel": order["channel"],
        "total_amount": quantity * price
    }

def create_silver_orders(orders, customers_lookup, products_lookup):

    clean_orders = []
    invalid_orders = []
    seen_order_ids = set()

    for order in orders:

        order["status"] = normalize_status(order["status"])
        order["channel"] = normalize_channel(order["channel"])

        valid, reason = validate_order(
            order,
            customers_lookup,
            products_lookup,
            seen_order_ids
        )

        seen_order_ids.add(order["order_id"])

        if valid:
            clean_orders.append(
                enrich_order(order, customers_lookup, products_lookup)
            )

        else:
            invalid = order.copy()
            invalid["invalid_reason"] = reason
            invalid_orders.append(invalid)

    return clean_orders, invalid_orders

def create_revenue_by_city(clean_orders):

    revenue = {}

    for order in clean_orders:
        if order["status"] == "completed":

            city = order["city"]
            revenue[city] = revenue.get(city, 0) + order["total_amount"]

    return [
        {
            "city": city,
            "revenue": total
        }
        for city, total in revenue.items()
    ]

def create_revenue_by_category(clean_orders):

    revenue = {}

    for order in clean_orders:
        if order["status"] == "completed":

            category = order["category"]
            revenue[category] = revenue.get(category, 0) + order["total_amount"]

    return [
        {
            "category": category,
            "revenue": total
        }
        for category, total in revenue.items()
    ]

def create_top_customers(clean_orders):

    customers = {}

    for order in clean_orders:
        if order["status"] == "completed":

            name = order["customer_name"]
            customers[name] = customers.get(name, 0) + order["total_amount"]

    rows = []

    for name, total in customers.items():
        rows.append({
            "customer_name": name,
            "revenue": total
        })

    return sorted(
        rows,
        key=lambda x: x["revenue"],
        reverse=True
    )[:5]

def create_executive_summary(clean_orders, invalid_orders):

    completed_revenue = 0
    completed_orders = 0

    for order in clean_orders:

        if order["status"] == "completed":

            completed_orders += 1
            completed_revenue += order["total_amount"]


    text = f"""
Executive Summary

Total valid orders: {len(clean_orders)}

Total invalid orders: {len(invalid_orders)}

Completed orders: {completed_orders}

Completed revenue: {completed_revenue}
"""


    with open(
        "data/gold/executive_summary.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)

def main():
    ensure_folders()

    orders = load_csv("data/bronze/orders_raw.csv")
    customers = load_csv("data/bronze/customers_raw.csv")
    products = load_csv("data/bronze/products_raw.csv")

    customers_lookup = build_lookup(customers, "customer_id")
    products_lookup = build_lookup(products, "product_id")

    clean_orders, invalid_orders = create_silver_orders(
        orders,
        customers_lookup,
        products_lookup
    )

    write_csv(
        "data/silver/orders_clean.csv",
        clean_orders,
        clean_orders[0].keys()
    )

    write_csv(
        "data/silver/invalid_orders.csv",
        invalid_orders,
        invalid_orders[0].keys()
    )

    print("Silver layer created")
    print("Valid orders:", len(clean_orders))
    print("Invalid orders:", len(invalid_orders))

    revenue_by_city = create_revenue_by_city(clean_orders)

    revenue_by_category = create_revenue_by_category(clean_orders)

    top_customers = create_top_customers(clean_orders)

    write_csv(
        "data/gold/revenue_by_city.csv",
        revenue_by_city,
        ["city", "revenue"]
    )

    write_csv(
        "data/gold/revenue_by_category.csv",
        revenue_by_category,
        ["category", "revenue"]
    )

    write_csv(
        "data/gold/top_customers.csv",
        top_customers,
        ["customer_name", "revenue"]
    )

    create_executive_summary(
        clean_orders,
        invalid_orders
    )
if __name__ == "__main__":
    main()