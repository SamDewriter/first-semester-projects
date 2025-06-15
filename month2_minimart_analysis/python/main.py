# Entry point for the MiniMart data reporting system

from utils import convert_currency, apply_discount
from report_generator import generate_report, print_report, save_report_to_json

# Simulated products
products = {
    1: {"name": "Wireless Mouse", "price": 25.99},
    2: {"name": "Bluetooth Headphones", "price": 79.49},
    3: {"name": "Coffee Maker", "price": 49.95},
    4: {"name": "Yoga Mat", "price": 20.00},
    5: {"name": "Smartwatch", "price": 199.99}
}

# Simulated orders
orders = [
    {"order_id": 1, "customer": "John Doe", "product_id": 2, "quantity": 1},
    {"order_id": 2, "customer": "Jane Smith", "product_id": 3, "quantity": 2},
    {"order_id": 3, "customer": "Alice Johnson", "product_id": 1, "quantity": 3},
    {"order_id": 4, "customer": "Bob Brown", "product_id": 5, "quantity": 1},
    {"order_id": 5, "customer": "Emily Davis", "product_id": 4, "quantity": 5},
    {"order_id": 6, "customer": "John Doe", "product_id": 5, "quantity": 1}
]

# Currency conversion rate (e.g., USD to EUR)
conversion_rate = 0.85

# Process orders
for order in orders:
    product_id = order['product_id']
    quantity = order['quantity']
    price = products[product_id]['price']
    total = quantity * price

    # Flag large orders
    if total > 100:
        print(f"Large Order Alert: Order {order['order_id']} total is ${total:,.2f}")

    # Currency conversion
    converted_total = convert_currency(total, conversion_rate)

    # Apply discount
    discounted_total = apply_discount(converted_total, threshold=100, discount_rate=0.10)

    # Save processed amount for potential future use
    order['converted_total'] = discounted_total

# Generate the report
report = generate_report(orders, products)

# Print report nicely
print_report(report)

# Save report to JSON file (Bonus)
save_report_to_json(report, "sales_report.json")
