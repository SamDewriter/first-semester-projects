# Entry point for the MiniMart data reporting system
from utils import convert_currency, apply_discount, flag_large_orders
from report_generator import generate_report, print_report
products = [
    {'product_id': 1, 'product_name': '50g peak Milk', 'category': 'Dairy', 'price': 5000.00},
    {'product_id': 2, 'product_name': 'Bokku Bread', 'category': 'Bakery', 'price': 1300.00},
    {'product_id': 3, 'product_name': 'Egg', 'category': 'Dairy', 'price': 300.00},
    {'product_id': 4, 'product_name': 'Apples', 'category': 'fruit', 'price': 1000.00},
    {'product_id': 5, 'product_name': 'Coke 50cl', 'category': 'Drinks', 'price': 500.00},
    {'product_id': 6, 'product_name': 'Table water', 'category': 'Drinks', 'price': 200.00}
]

customers = [
    {'customer_id': 1, 'name': 'Opeyemi Ayeni', 'email': 'a.opeyemi@gmail.com','date':'2023-01-15','phone':'08165114690' },
    {'customer_id': 2, 'name': 'Michael Chinedu', 'email': 'michael.c@gmail.com','date':'2023-02-20','phone':'08166004690'},
    {'customer_id': 3, 'name': 'Emma Orunkoyi', 'email': 'emma.r@gmail.com','date':'2023-05-05','phone':'08175114690'},
    {'customer_id': 4, 'name': 'Kim Dave', 'email': 'davidkim@yahoo.com','date':'2023-05-05','phone':'08175114690'},
    {'customer_id': 5, 'name': 'Ayeni Moyinoluwa', 'email': 'moyin@yahoo.com','date':'2023-06-17','phone':'08165114100'}
]

# Simulate new orders
orders = [
    {'customer_id': 1, 'product_id': 3, 'quantity': 2, 'order_date': '2023-11-01'},
    {'customer_id': 2, 'product_id': 1, 'quantity': 1, 'order_date': '2024-10-02'},
    {'customer_id': 3, 'product_id': 4, 'quantity': 3, 'order_date': '2023-11-02'},
    {'customer_id': 1, 'product_id': 2, 'quantity': 2, 'order_date': '2024-11-03'},
    {'customer_id': 4, 'product_id': 5, 'quantity': 6, 'order_date': '2024-11-03'},
    {'customer_id': 5, 'product_id': 6, 'quantity': 15, 'order_date': '2024-11-04'}  # New large order
]

# Process orders
for order in orders:
    product = next(p for p in products if p['product_id'] == order['product_id'])
    original_price = product['price']
    
    # Convert to USD (assuming 1 USD = 1500 Naira)
    usd_price = convert_currency(original_price, 1/1500)
    
    # Apply quantity discount
    discounted_price = apply_discount(original_price, order['quantity'])
    
    # Calculate total
    order['total'] = discounted_price * order['quantity']
    order['original_total'] = original_price * order['quantity']
    order['usd_total'] = convert_currency(order['total'], 1/1500)

# Flag large orders
orders = flag_large_orders(orders, threshold=500)

# Generate and display report
report = generate_report(orders, products, customers)
print_report(report)

# Saving report to JSON
from utils import save_to_json
save_to_json(report, 'minimart_report.json')
print("\nReport saved to 'minimart_report.json'")