# Python Tasks Implementation

# 1. Create lists/dictionaries to simulate new order data
new_orders = [
    {
        'customer': {'id': 6, 'name': 'Bola Adekunle', 'email': 'bola@example.com'},
        'order_date': '2025-06-05',
        'items': [
            {'product_id': 1, 'name': 'Phone', 'price': '2.99', 'quantity': 3},
            {'product_id': 5, 'name': 'Chicken', 'price': '5.99', 'quantity': 2}
        ]
    },
    {
        'customer': {'id': 7, 'name': 'Yemi Alade', 'email': 'yemi@example.com'},
        'order_date': '2025-06-06',
        'items': [
            {'product_id': 3, 'name': 'Eggs', 'price': '3.49', 'quantity': 5}
        ]
    }
]

# 2. Use if, and, or to identify customers who placed large orders
print("Customers with large orders:")
for order in new_orders:
    total = sum(float(item['price']) * item['quantity'] for item in order['items'])
    if total > 15 or (order['customer']['name'].startswith('B') and total > 10):
        print(f"{order['customer']['name']} placed a large order worth ${total:.2f}")

# 3. Convert product prices from string to float and apply discounts
print("\nApplying 10% discount to all products:")
for order in new_orders:
    for item in order['items']:
        original_price = float(item['price'])
        discounted_price = original_price * 0.9  # 10% discount
        item['price'] = str(discounted_price)
        print(f"{item['name']}: ${original_price:.2f} → ${discounted_price:.2f}")

# 4. Create a dictionary report summarizing sales
def generate_sales_report(orders):
    report = {
        'total_products_sold': 0,
        'products': {},
        'customers': {},
        'most_popular_product': {'name': '', 'quantity': 0},
        'total_revenue': 0.0
    }
    
    for order in orders:
        customer_name = order['customer']['name']
        if customer_name not in report['customers']:
            report['customers'][customer_name] = {'total_spent': 0.0, 'items': 0}
        
        for item in order['items']:
            # Update product stats
            product_name = item['name']
            quantity = item['quantity']
            price = float(item['price'])
            
            if product_name not in report['products']:
                report['products'][product_name] = 0
            report['products'][product_name] += quantity
            
            # Update customer stats
            report['customers'][customer_name]['total_spent'] += price * quantity
            report['customers'][customer_name]['items'] += quantity
            
            # Update totals
            report['total_products_sold'] += quantity
            report['total_revenue'] += price * quantity
            
            # Check for most popular product
            if report['products'][product_name] > report['most_popular_product']['quantity']:
                report['most_popular_product'] = {'name': product_name, 'quantity': report['products'][product_name]}
    
    return report

# Generate and display the report
sales_report = generate_sales_report(new_orders)
print("\nSales Report:")
print(f"Total products sold: {sales_report['total_products_sold']}")
print(f"Most popular product: {sales_report['most_popular_product']['name']} ({sales_report['most_popular_product']['quantity']} units)")
print(f"Total revenue: ${sales_report['total_revenue']:.2f}")

print("\nRevenue by customer:")
for customer, data in sales_report['customers'].items():
    print(f"{customer}: ${data['total_spent']:.2f} (for {data['items']} items)")

print("\nProducts sold:")
for product, quantity in sales_report['products'].items():
    print(f"{product}: {quantity} units")