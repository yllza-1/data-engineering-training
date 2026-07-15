from order_data import orders


def print_raw_record_count():
    print("Raw records:", len(orders))


def print_first_three_records():
    print("\nFirst three raw records:")

    for order in orders[:3]:
        print(order)


def print_unique_values(field_name, title):
    values = set()

    for order in orders:
        values.add(order[field_name])

    print(f"\n{title}:")
    print(values)

def validate_order(order):
    reasons = []

    if order["customer_name"] == "":
        reasons.append("Empty customer_name")

    if order["quantity"] <= 0:
        reasons.append("Quantity must be greater than 0")

    if order["price"] <= 0:
        reasons.append("Price must be greater than 0")

    return reasons

def print_validation_summary(valid_orders, invalid_orders):
    print("Validation Summary")
    print()
    print("Total orders:", len(valid_orders) + len(invalid_orders))
    print("Valid orders:", len(valid_orders))
    print("Invalid orders:", len(invalid_orders))


def split_valid_and_invalid_orders(orders):
    valid_orders = []
    invalid_orders = []

    for order in orders:
        reasons = validate_order(order)

        if reasons:
            invalid_orders.append(order)
        else:
            valid_orders.append(order)

    return valid_orders, invalid_orders



def normalize_status(status):
    if status == "Completed" or status == "complete":
        return "completed"

    return status.lower()


def normalize_city(city):
    if city == "Prishtine":
        return "Prishtina"

    return city


def normalize_category(category):
    if category == "accessories":
        return "Accessories"

    return category


def normalize_channel(channel):
    if channel == "Online":
        return "online"

    return channel.lower()

def calculate_total_amount(order):
    return order["quantity"] * order["price"]


def add_total_amount(orders):
    for order in orders:
        order["total_amount"] = calculate_total_amount(order)


def clean_order(order):
    clean = order.copy()

    clean["status"] = normalize_status(order["status"])
    clean["city"] = normalize_city(order["city"])
    clean["category"] = normalize_category(order["category"])
    clean["channel"] = normalize_channel(order["channel"])
    clean["total_amount"] = calculate_total_amount(order)

    return clean


def clean_valid_orders(valid_orders):
    clean_orders = []

    for order in valid_orders:
        clean_orders.append(clean_order(order))

    return clean_orders


def print_clean_unique_values(records, field_name, title):
    values = set()

    for order in records:
        values.add(order[field_name])

    print(f"\n{title}:")
    print(values)

def get_raw_record_count():
    return len(orders)


def get_valid_record_count(valid_orders):
    return len(valid_orders)


def get_invalid_record_count(invalid_orders):
    return len(invalid_orders)


def get_completed_order_count(records):
    completed = 0

    for order in records:
        if order["status"] == "completed":
            completed += 1

    return completed


def get_non_revenue_order_count(records):
    non_revenue = 0

    for order in records:
        if order["status"] in ["pending", "cancelled", "returned"]:
            non_revenue += 1

    return non_revenue


def get_completed_revenue(records):
    revenue = 0

    for order in records:
        if order["status"] == "completed":
            revenue += order["total_amount"]

    return revenue


def get_average_completed_order_value(records):
    completed_orders = get_completed_order_count(records)
    revenue = get_completed_revenue(records)

    if completed_orders == 0:
        return 0

    return revenue / completed_orders


def get_highest_completed_order(records):
    highest = 0

    for order in records:
        if order["status"] == "completed":

            if order["total_amount"] > highest:
                highest = order["total_amount"]

    return highest


def get_lowest_completed_order(records):
    lowest = None

    for order in records:
        if order["status"] == "completed":

            if lowest is None or order["total_amount"] < lowest:
                lowest = order["total_amount"]

    return lowest


def count_by_field(records, field_name):
    counts = {}

    for order in records:
        value = order[field_name]

        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    return counts


def sum_revenue_by_field(records, field_name):
    revenue = {}

    for order in records:
        if order["status"] == "completed":
            value = order[field_name]

            if value in revenue:
                revenue[value] += order["total_amount"]
            else:
                revenue[value] = order["total_amount"]

    return revenue


def get_customers_with_multiple_orders(records):
    customer_counts = {}

    for order in records:
        customer = order["customer_name"]

        if customer in customer_counts:
            customer_counts[customer] += 1
        else:
            customer_counts[customer] = 1

    multiple_customers = []

    for customer, count in customer_counts.items():
        if count > 1:
            multiple_customers.append(customer)

    return multiple_customers


def get_products_ordered_more_than_once(records):
    product_counts = {}

    for order in records:
        product = order["product"]

        if product in product_counts:
            product_counts[product] += 1
        else:
            product_counts[product] = 1

    products = []

    for product, count in product_counts.items():
        if count > 1:
            products.append(product)

    return products

def get_completed_revenue_by(records, field):
    revenue = {}

    for order in records:
        if order["status"] == "completed":

            key = order[field]

            if key not in revenue:
                revenue[key] = 0

            revenue[key] += order["total_amount"]

    return revenue

def print_ranking(title, revenue, top=None):
    print(f"\n{title}")

    sorted_items = sorted(revenue.items(), key=lambda item: item[1], reverse=True)

    if top is not None:
        sorted_items = sorted_items[:top]

    for name, amount in sorted_items:
        print(name, "-", amount)

def print_top_completed_orders(records):
    completed_orders = []

    for order in records:
        if order["status"] == "completed":
            completed_orders.append(order)

    completed_orders = sorted(
        completed_orders,
        key=lambda order: order["total_amount"],
        reverse=True
    )

    print("\nTop 5 Completed Orders")

    for order in completed_orders[:5]:
        print(
            order["order_id"],
            order["customer_name"],
            order["product"],
            order["total_amount"]
        )


def print_invalid_records_removed(invalid_orders):
    print("\nWhich invalid records were removed and why?")

    for order in invalid_orders:
        reasons = validate_order(order)
        print(f"Order ID: {order['order_id']}")
        print("Reasons:", ", ".join(reasons))
        print()


def print_valid_non_revenue_orders(clean_orders):
    print("\nHow many valid orders do not count as revenue?")
    print(get_non_revenue_order_count(clean_orders))


def print_status_before_normalization():
    print("\nWhich status values existed before normalization?")
    print_unique_values("status", "Raw statuses")


def print_normalization_changes():
    print("\nWhich city/category/channel values changed after normalization?")

    print("Status:")
    print("- Completed -> completed")
    print("- complete -> completed")

    print("\nCity:")
    print("- Prishtine -> Prishtina")

    print("\nCategory:")
    print("- accessories -> Accessories")

    print("\nChannel:")
    print("- Online -> online")


def print_validation_effect():
    print("\nWhat would go wrong if we calculated revenue before validation?")
    print("- Invalid records would be included in revenue.")
    print("- Orders with invalid quantity or price would produce incorrect revenue.")
    print("- Business reports would not be accurate.")


def print_non_revenue_effect():
    print("\nWhat would go wrong if pending, cancelled, and returned orders counted as revenue?")
    print("- Revenue would be higher than the real sales.")
    print("- Pending orders are not completed.")
    print("- Cancelled orders were never sold.")
    print("- Returned orders should not count as revenue.")
    print("- Business reports would be misleading.")


def add_risk_flag(orders):
    for order in orders:
        if order["total_amount"] >= 500:
            order["risk_flag"] = "high_value"
        else:
            order["risk_flag"] = "normal"


def revenue_by_date(orders):
    revenue = {}

    for order in orders:
        if order["status"] == "completed":
            date = order["order_date"]

            if date not in revenue:
                revenue[date] = 0

            revenue[date] += order["total_amount"]

    return revenue


def city_with_most_non_revenue_orders(orders):
    cities = {}

    for order in orders:
        if order["status"] != "completed":
            city = order["city"]

            if city not in cities:
                cities[city] = 0

            cities[city] += 1

    highest_city = max(cities, key=cities.get)

    print("\nCity with the highest number of non-revenue orders:")
    print(highest_city, "-", cities[highest_city])


def customers_with_completed_and_failed_orders(orders):
    completed = set()
    failed = set()

    for order in orders:
        if order["status"] == "completed":
            completed.add(order["customer_name"])

        if order["status"] in ["cancelled", "returned"]:
            failed.add(order["customer_name"])

    result = completed.intersection(failed)

    print("\nCustomers with completed revenue and cancelled/returned orders:")
    for customer in result:
        print(customer)


def top_n_values(revenue_dict, n):
    sorted_values = sorted(
        revenue_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_values[:n]


def print_risk_recommendation(orders):
    high_value_orders = 0

    for order in orders:
        if order["risk_flag"] == "high_value":
            high_value_orders += 1

    print("\nBusiness Recommendation:")

    if high_value_orders > 0:
        print("Review all high-value orders before shipment.")
    else:
        print("No high-value orders found.")


def run_checks(completed_revenue, invalid_records, cleaned_orders):
    print("\nUnit-like Checks")

    print("Completed revenue greater than 0:",
          completed_revenue > 0)

    print("Invalid records list is not empty:",
          len(invalid_records) > 0)

    has_total_amount = all(
        "total_amount" in order
        for order in cleaned_orders
    )

    print("Every cleaned order has total_amount:",
          has_total_amount)



def main():
    print_raw_record_count()
    print_first_three_records()

    print_unique_values("status", "Raw statuses")
    print_unique_values("city", "Raw cities")
    print_unique_values("category", "Raw categories")
    print_unique_values("channel", "Raw channels")

    valid_orders, invalid_orders = split_valid_and_invalid_orders(orders)

    print_validation_summary(valid_orders, invalid_orders)

    for order in orders:
        reasons = validate_order(order)

        if reasons:
            print("Order ID:", order["order_id"])
            print("Reasons:", reasons)
            print()

    clean_orders = clean_valid_orders(valid_orders)

    add_total_amount(clean_orders)

    print_clean_unique_values(clean_orders, "status", "Clean statuses")
    print_clean_unique_values(clean_orders, "city", "Clean cities")
    print_clean_unique_values(clean_orders, "category", "Clean categories")
    print_clean_unique_values(clean_orders, "channel", "Clean channels")

    print("\nBusiness Metrics")
    print("Raw Records:", get_raw_record_count())
    print("Valid Records:", get_valid_record_count(clean_orders))
    print("Invalid Records:", get_invalid_record_count(invalid_orders))
    print("Completed Orders:", get_completed_order_count(clean_orders))
    print("Non-Revenue Orders:", get_non_revenue_order_count(clean_orders))
    print("Completed Revenue:", get_completed_revenue(clean_orders))
    print("Average Completed Order Value:", get_average_completed_order_value(clean_orders))
    print("Highest Order:", get_highest_completed_order(clean_orders))
    print("Lowest Completed Order:", get_lowest_completed_order(clean_orders))
    print("\nOrders by status")
    print(count_by_field(clean_orders, "status"))

    print("\nOrders by city")
    print(count_by_field(clean_orders, "city"))

    print("\nOrders by category")
    print(count_by_field(clean_orders, "category"))

    print("\nOrders by channel")
    print(count_by_field(clean_orders, "channel"))

    print("\nCompleted revenue by city")
    print(sum_revenue_by_field(clean_orders, "city"))

    print("\nCompleted revenue by category")
    print(sum_revenue_by_field(clean_orders, "category"))

    print("\nCompleted revenue by channel")
    print(sum_revenue_by_field(clean_orders, "channel"))

    print("\nCompleted revenue by customer")
    print(sum_revenue_by_field(clean_orders, "customer_name"))

    print("\nCustomers with more than one valid order")
    print(get_customers_with_multiple_orders(clean_orders))

    print("\nProducts ordered more than once")
    print(get_products_ordered_more_than_once(clean_orders))
  
    print_top_completed_orders(clean_orders)

    customer_revenue = get_completed_revenue_by(clean_orders, "customer_name")
    print_ranking("Top 3 Customers", customer_revenue, 3)

    product_revenue = get_completed_revenue_by(clean_orders, "product")
    print_ranking("Top 3 Products", product_revenue, 3)

    city_revenue = get_completed_revenue_by(clean_orders, "city")
    print_ranking("Top 3 Cities", city_revenue, 3)

    category_revenue = get_completed_revenue_by(clean_orders, "category")
    print_ranking("Categories by Revenue", category_revenue)

    channel_revenue = get_completed_revenue_by(clean_orders, "channel")
    print_ranking("Channels by Revenue", channel_revenue)


    print_invalid_records_removed(invalid_orders)
    print_valid_non_revenue_orders(clean_orders)
    print_status_before_normalization()
    print_normalization_changes()
    print_validation_effect()
    print_non_revenue_effect()
    
    add_risk_flag(clean_orders)

    date_revenue = revenue_by_date(clean_orders)

    print("\nRevenue by date:")
    for date, amount in date_revenue.items():
     print(date, ":", amount)

    city_with_most_non_revenue_orders(clean_orders)

    customers_with_completed_and_failed_orders(clean_orders)

    print("\nTop 3 revenue values:")
    print(top_n_values(date_revenue, 3))

    print_risk_recommendation(clean_orders)

    run_checks(
    get_completed_revenue(clean_orders),
    invalid_orders,
    clean_orders
)

if __name__ == "__main__":
    
    main()