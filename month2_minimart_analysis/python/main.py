# Entry point for the MiniMart data reporting system

from report_generator import generate_sales_summary
from utils import convert_currency, apply_discount
from utils import print_newline

# Sample product catalog
products = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Headphones", "price": 199.99},
    3: {"name": "Notebook", "price": 4.99},
    4: {"name": "Mouse", "price": 49.99}
}

# Simulated orders list
orders = [
    {"customer": "Alice", "product_id": 1, "quantity": 1},
    {"customer": "Bob",   "product_id": 2, "quantity": 2},
    {"customer": "Alice", "product_id": 3, "quantity": 5},
    {"customer": "Diana", "product_id": 4, "quantity": 3},
    {"customer": "Ethan", "product_id": 2, "quantity": 1}
]

print_newline()
# Apply conditional flags
for order in orders:
    product = products[order['product_id']]
    total_cost = product['price'] * order['quantity']
    if total_cost > 100:
        print(f"⚠️ Large order flagged for {order['customer']}: ${total_cost:.2f}")
        print('applying discount of 10%...')

        discounted = apply_discount(total_cost)
        print(f"Final price after discount: ${discounted:.2f}")
        print(f"Price in EUR: €{convert_currency(discounted)}")
        print_newline()

# Generate report
report = generate_sales_summary(orders, products)

# Print the report summary
print("\n📊 MiniMart Sales Report")
print("---------------------------")
print(f"Total products sold:        {report['total_products_sold']}")
print(f"Most popular product:       {report['most_popular_product']}")
print(f"Revenue per customer:       {report['revenue_per_customer']}\n")

