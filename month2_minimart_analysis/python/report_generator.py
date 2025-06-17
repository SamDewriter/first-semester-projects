# Code to generate dictionary summary reports
from typing import Dict, List
from utils import save_to_json

def generate_report(orders: List[Dict], products: List[Dict], customers: List[Dict]) -> Dict:
    "Generating a comprehensive sales report"
   # Initialize report dictionary
    report = {
        'total_products_sold': 0,
        'most_popular_product': None,
        'revenue_per_customer': [],
        'total_revenue': 0
    }
    
    # Return empty report if no orders exist
    if not orders:
        return report
    
    # Calculate total products sold
    report['total_products_sold'] = sum(order['quantity'] for order in orders)
    
    # Find most popular product
    product_sales = {}
    for order in orders:
        product_id = order['product_id']
        product_sales[product_id] = product_sales.get(product_id, 0) + order['quantity']
    
    if product_sales:  # Only try to find most popular if there are sales
        most_popular_product_id = max(product_sales, key=product_sales.get)
        most_popular_product = next(
            p for p in products if p['product_id'] == most_popular_product_id
        )
        report['most_popular_product'] = {
            'product_id': most_popular_product['product_id'],
            'product_name': most_popular_product['product_name'],
            'quantity_sold': product_sales[most_popular_product_id]
        }
    # Calculate revenue per customer
    revenue_per_customer = {}
    for order in orders:
        customer_id = order['customer_id']
        revenue = order['total']
        revenue_per_customer[customer_id] = revenue_per_customer.get(customer_id, 0) + revenue
    
    return {
        'total_products_sold': total_products_sold,
        'most_popular_product': {
            'product_id': most_popular_product['product_id'],
            'product_name': most_popular_product['product_name'],
            'quantity_sold': product_sales[most_popular_product_id]
        },
        'revenue_per_customer': [
            {
                'customer_id': cust_id,
                'revenue': revenue,
                'customer_name': next(
                    c['name'] for c in customers if c['customer_id'] == cust_id
                )
            }
            for cust_id, revenue in revenue_per_customer.items()
        ],
        'total_revenue': sum(revenue_per_customer.values())
    }

def print_report(report: Dict) -> None:
    "Print a nicely formatted report summary"
    print("\n=== MINIMART SALES REPORT ===")
    print(f"Total Products Sold: {report['total_products_sold']}")
    print(f"\nMost Popular Product:")
    print(f"  - Name: {report['most_popular_product']['product_name']}")
    print(f"  - Quantity Sold: {report['most_popular_product']['quantity_sold']}")
    
    print("\nRevenue by Customer:")
    for customer in report['revenue_per_customer']:
        print(f"  - {customer['customer_name']}: ₦{customer['revenue']:.2f}")
    
    print(f"\nTotal Revenue: ₦{report['total_revenue']:.2f}")