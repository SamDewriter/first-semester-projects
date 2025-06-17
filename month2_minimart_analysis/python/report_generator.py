# Code to generate dictionary summary reports
from collections import defaultdict
from utils import convert_currency, apply_discount

def generate_sales_summary(orders, products):
    total_products_sold = 0
    product_sales = defaultdict(int)
    customer_revenue = defaultdict(float)

    for order in orders:
        product_id = order['product_id']
        quantity = order['quantity']
        price = products[product_id]['price']
        customer = order['customer']

        total_products_sold += quantity
        product_sales[product_id] += quantity
        customer_revenue[customer] += quantity * price

    most_popular_product_id = max(product_sales, key=product_sales.get, default=None)
    most_popular_product = products[most_popular_product_id]['name'] if most_popular_product_id else None

    return {
        'total_products_sold': total_products_sold,
        'most_popular_product': most_popular_product,
        'revenue_per_customer': dict(customer_revenue)
    }
