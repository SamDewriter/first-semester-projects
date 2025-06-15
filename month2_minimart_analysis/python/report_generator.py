# Code to generate dictionary summary reports

import json

def generate_report(orders, products):
    total_products_sold = 0
    product_sales = {}
    customer_revenue = {}

    for order in orders:
        product_id = order['product_id']
        quantity = order['quantity']
        customer = order['customer']
        price = products[product_id]['price']
        total = quantity * price

        total_products_sold += quantity

        # Product sales count
        product_sales[product_id] = product_sales.get(product_id, 0) + quantity

        # Customer revenue
        customer_revenue[customer] = customer_revenue.get(customer, 0) + total

    # Find most popular product
    # Find most popular product
    most_popular_product_id = max(product_sales.items(), key=lambda item: item[1])[0]
    most_popular_product = products[most_popular_product_id]['name']


    report = {
        "total_products_sold": total_products_sold,
        "most_popular_product": most_popular_product,
        "revenue_per_customer": customer_revenue
    }

    return report

def print_report(report):
    print("\n=== SALES REPORT ===")
    print(f"Total Products Sold: {report['total_products_sold']}")
    print(f"Most Popular Product: {report['most_popular_product']}")
    print("Revenue Per Customer:")
    for customer, revenue in report['revenue_per_customer'].items():
        print(f"  {customer}: ${revenue:,.2f}")

def save_report_to_json(report, filename):
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"\nReport successfully saved to {filename}")
