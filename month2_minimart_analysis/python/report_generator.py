# Code to generate dictionary summary reports
from collections import Counter


def generate_sales_report(orders, products):
    # 1. Total products sold
    total_products_sold = sum(order['quantity'] for order in orders)

    # 2. Most popular product
    product_quantities = Counter()
    for order in orders:
        product_quantities[order['product_id']] += order['quantity']
    
    most_popular_product_id = product_quantities.most_common(1)[0][0]
    most_popular_product_name = products[most_popular_product_id]['name']

    # 3. Revenue per customer
    revenue_per_customer = {}
    for order in orders:
        customer = order['customer_id']
        product_price = products[order['product_id']]['price']
        order_revenue = product_price * order['quantity']
        
        revenue_per_customer[customer] = revenue_per_customer.get(customer, 0) + order_revenue
    
    # Format the revenue to two decimal places
    formatted_revenue = {f"Customer_{c}": f"${rev:.2f}" for c, rev in revenue_per_customer.items()}

    # Assemble the final report dictionary
    report = {
        "sales_summary": {
            "total_items_sold": total_products_sold,
            "most_popular_product": most_popular_product_name
        },
        "customer_revenue": formatted_revenue
    }

    return report
