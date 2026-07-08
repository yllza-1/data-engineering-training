orders = [
    {
        "order_id": 1,
        "customer_name": "Arta",
        "city": "Vushtrri",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "price": 700,
        "status": "completed",
        "order_date": "2026-07-01"
    },
    {
        "order_id": 2,
        "customer_name": "Blend",
        "city": "Prishtina",
        "product": "Mouse",
        "category": "Accessories",
        "quantity": 2,
        "price": 15,
        "status": "completed",
        "order_date": "2026-07-01"
    },
    {
        "order_id": 3,
        "customer_name": "Arta",
        "city": "Vushtrri",
        "product": "Keyboard",
        "category": "Accessories",
        "quantity": 1,
        "price": 40,
        "status": "cancelled",
        "order_date": "2026-07-02"
    },
    {
        "order_id": 4,
        "customer_name": "Dren",
        "city": "Mitrovica",
        "product": "Monitor",
        "category": "Electronics",
        "quantity": 1,
        "price": 180,
        "status": "completed",
        "order_date": "2026-07-02"
    },
    {
        "order_id": 5,
        "customer_name": "Elira",
        "city": "Prishtina",
        "product": "Mouse",
        "category": "Accessories",
        "quantity": 1,
        "price": 15,
        "status": "completed",
        "order_date": "2026-07-03"
    },
    {
        "order_id": 6,
        "customer_name": "Dren",
        "city": "Mitrovica",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "price": 700,
        "status": "pending",
        "order_date": "2026-07-03"
    },
    {
        "order_id": 7,
        "customer_name": "Nora",
        "city": "Vushtrri",
        "product": "Headphones",
        "category": "Accessories",
        "quantity": 1,
        "price": 50,
        "status": "completed",
        "order_date": "2026-07-04"
    },
    {
        "order_id": 8,
        "customer_name": "Leart",
        "city": "Peja",
        "product": "Monitor",
        "category": "Electronics",
        "quantity": 2,
        "price": 180,
        "status": "completed",
        "order_date": "2026-07-04"
    },
    {
        "order_id": 9,
        "customer_name": "Faton",
        "city": "Prizren",
        "product": "Desk Chair",
        "category": "Office",
        "quantity": 1,
        "price": 120,
        "status": "completed",
        "order_date": "2026-07-05"
    },
    {
        "order_id": 10,
        "customer_name": "Gresa",
        "city": "Prishtina",
        "product": "USB Cable",
        "category": "Accessories",
        "quantity": 3,
        "price": 8,
        "status": "completed",
        "order_date": "2026-07-05"
    },
    {
        "order_id": 11,
        "customer_name": "Rina",
        "city": "Vushtrri",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "price": 650,
        "status": "cancelled",
        "order_date": "2026-07-06"
    },
    {
        "order_id": 12,
        "customer_name": "Arben",
        "city": "Ferizaj",
        "product": "Desk",
        "category": "Office",
        "quantity": 1,
        "price": 220,
        "status": "pending",
        "order_date": "2026-07-06"
    },
     {
        "order_id": 13,
        "customer_name": "Arben",
        "city": "Prishtina",
        "product": "Keyboard",
        "category": "Accessories",
        "quantity": 2,
        "price": 35,
        "status": "completed"
    },
    {
        "order_id": 14,
        "customer_name": "Sara",
        "city": "Vushtrri",
        "product": "Monitor",
        "category": "Electronics",
        "quantity": 1,
        "price": 250,
        "status": "pending"
    }
]


def print_total_orders():
    print("Total orders:", len(orders))


def print_customer_names():
    print("\nCustomer names:")
    for order in orders:
        print(order["customer_name"])


def print_order_details():
    print("\nOrder details:")
    for order in orders:
        print(
            f'{order["customer_name"]} ordered {order["product"]} '
            f'from {order["city"]} and the status is {order["status"]}.'
        )

def print_completed_orders():
    print("\nCompleted orders:")
    for order in orders:
        if order["status"] == "completed":
            print(f'{order["order_id"]} - {order["customer_name"]} - {order["product"]}')

def print_pending_orders():
    print("\nPending orders:")
    for order in orders:
        if order["status"] == "pending":
            print(f'{order["order_id"]} - {order["customer_name"]} - {order["product"]}')


def print_cancelled_orders():
    print("\nCancelled orders:")
    for order in orders:
        if order["status"] == "cancelled":
            print(f'{order["order_id"]} - {order["customer_name"]} - {order["product"]}')


def print_expensive_orders():
    print("\nOrders where price is greater than 100:")
    for order in orders:
        if order["price"] > 100:
            print(f'{order["order_id"]} - {order["customer_name"]} - {order["product"]}')


def print_accessories_orders():
    print("\nAccessories orders:")
    for order in orders:
        if order["category"] == "Accessories":
            print(f'{order["order_id"]} - {order["customer_name"]} - {order["product"]}')

def print_order_totals():
    print("\nOrder totals:")

    for order in orders:
        total_amount = order["quantity"] * order["price"]

        print(
            f'{order["customer_name"]} - {order["product"]} - '
            f'{order["quantity"]} x {order["price"]} = {total_amount}'
        )
        

def sort_by_price():
    print("\nOrders sorted by price (most expensive to cheapest):")

    sorted_orders = sorted(
        orders,
        key=lambda order: order["price"],
        reverse=True
    )

    for order in sorted_orders:
        print(f'{order["customer_name"]} - {order["product"]} - {order["price"]}')

def sort_by_total_amount():
    print("\nOrders sorted by total amount (highest to lowest):")

    sorted_orders = sorted(
        orders,
        key=lambda order: order["quantity"] * order["price"],
        reverse=True
    )

    for order in sorted_orders:
        total_amount = order["quantity"] * order["price"]
        print(f'{order["customer_name"]} - {order["product"]} - {total_amount}')
    
def print_top_3_orders():
    print("\nTop 3 orders by total amount:")

    sorted_orders = sorted(
        orders,
        key=lambda order: order["quantity"] * order["price"],
        reverse=True
    )

    for order in sorted_orders[:3]:
        total_amount = order["quantity"] * order["price"]
        print(f'{order["customer_name"]} - {order["product"]} - {total_amount}')

def print_status_summary():
    status_counts = {
        "completed": 0,
        "pending": 0,
        "cancelled": 0
    }

    completed_revenue = 0

    for order in orders:
        status = order["status"]

        if status in status_counts:
            status_counts[status] += 1

        if order["status"] == "completed":
            completed_revenue += order["quantity"] * order["price"]

    print("\nStatus counts:")
    print(f'completed: {status_counts["completed"]}')
    print(f'pending: {status_counts["pending"]}')
    print(f'cancelled: {status_counts["cancelled"]}')

    print(f"Completed revenue: {completed_revenue}")


def print_customers_with_multiple_orders():
    customer_counts = {}

    for order in orders:
        customer = order["customer_name"]

        if customer in customer_counts:
            customer_counts[customer] += 1
        else:
            customer_counts[customer] = 1

    print("\nCustomers with more than one order:")

    for customer, count in customer_counts.items():
        if count > 1:
            print(f"{customer}: {count} orders")



city_count = {}

for order in orders:
    city = order["city"]

    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print(city_count)



category_count = {}

for order in orders:
    category = order["category"]

    if category in category_count:
        category_count[category] += 1
    else:
        category_count[category] = 1

print(category_count)


def main():
    print_total_orders()
    print_customer_names()
    print_order_details()

    print_completed_orders()
    print_pending_orders()
    print_cancelled_orders()
    print_expensive_orders()
    print_accessories_orders()

    print_order_totals()

    sort_by_price()
    sort_by_total_amount()
    print_top_3_orders()

    print_status_summary()
    print_customers_with_multiple_orders()


main()