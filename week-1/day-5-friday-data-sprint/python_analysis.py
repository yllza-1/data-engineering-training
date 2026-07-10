import csv


def load_orders(filename):
    orders = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["quantity"] = int(row["quantity"])
            row["price"] = float(row["price"])
            orders.append(row)

    return orders

def calculate_total_amount(orders):
    for order in orders:
        order["total_amount"] = order["quantity"] * order["price"]


def get_completed_orders(orders):
    completed = []

    for order in orders:
        if order["status"] == "completed":
            completed.append(order)

    return completed


def get_pending_orders(orders):
    pending = []

    for order in orders:
        if order["status"] == "pending":
            pending.append(order)

    return pending


def get_cancelled_orders(orders):
    cancelled = []

    for order in orders:
        if order["status"] == "cancelled":
            cancelled.append(order)

    return cancelled


def calculate_completed_revenue(orders):
    revenue = 0

    for order in orders:
        if order["status"] == "completed":
            revenue += order["total_amount"]

    return revenue


def most_expensive_order(orders):
    most_expensive = orders[0]

    for order in orders:
        if order["price"] > most_expensive["price"]:
            most_expensive = order

    return most_expensive


def highest_total_amount_order(orders):
    highest_order = orders[0]

    for order in orders:
        if order["total_amount"] > highest_order["total_amount"]:
            highest_order = order

    return highest_order


def count_by_status(orders):
    counts = {}

    for order in orders:
        status = order["status"]

        if status in counts:
            counts[status] += 1
        else:
            counts[status] = 1

    return counts


def count_by_city(orders):
    counts = {}

    for order in orders:
        city = order["city"]

        if city in counts:
            counts[city] += 1
        else:
            counts[city] = 1

    return counts


def count_by_category(orders):
    counts = {}

    for order in orders:
        category = order["category"]

        if category in counts:
            counts[category] += 1
        else:
            counts[category] = 1

    return counts


def print_business_report(orders):
    completed_orders = get_completed_orders(orders)
    pending_orders = get_pending_orders(orders)
    cancelled_orders = get_cancelled_orders(orders)

    revenue = calculate_completed_revenue(orders)

    expensive_order = most_expensive_order(orders)
    highest_order = highest_total_amount_order(orders)

    print("\n========== BUSINESS REPORT ==========\n")

    print("Total Orders:", len(orders))
    print("Completed Orders:", len(completed_orders))
    print("Pending Orders:", len(pending_orders))
    print("Cancelled Orders:", len(cancelled_orders))

    print("\nCompleted Revenue: €", revenue)

    print("\nMost Expensive Product:")
    print("Order #", expensive_order["order_id"])
    print("Product:", expensive_order["product"])
    print("Price: €", expensive_order["price"])

    print("\nHighest Total Amount Order:")
    print("Order #", highest_order["order_id"])
    print("Product:", highest_order["product"])
    print("Total Amount: €", highest_order["total_amount"])

    print("\nOrders by Status:")
    status_counts = count_by_status(orders)
    for status in status_counts:
        print(status + ":", status_counts[status])

    print("\nOrders by City:")
    city_counts = count_by_city(orders)
    for city in city_counts:
        print(city + ":", city_counts[city])

    print("\nOrders by Category:")
    category_counts = count_by_category(orders)
    for category in category_counts:
        print(category + ":", category_counts[category])

    print("\n=====================================")


def main():
    orders = load_orders("week-1/day-5-friday-data-sprint/data/orders.csv")
    calculate_total_amount(orders)
    print_business_report(orders)

# Run the main function only when this file is executed directly
if __name__ == "__main__":
    main()


