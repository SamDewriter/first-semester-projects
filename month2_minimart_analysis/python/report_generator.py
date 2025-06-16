#!/usr/bin/env python3
"""
Mini-Mart Analysis System
========================
This script analyzes mini-mart sales data using Python data structures
and provides comprehensive reporting with JSON export functionality.
"""

import json
from datetime import datetime
from collections import defaultdict

# Sample data (simulating database records)
customers = [
    {"customer_id": 1, "name": "John Smith", "email": "john.smith@email.com", "join_date": "2024-01-15"},
    {"customer_id": 2, "name": "Sarah Johnson", "email": "sarah.johnson@email.com", "join_date": "2024-02-20"},
    {"customer_id": 3, "name": "Mike Brown", "email": "mike.brown@email.com", "join_date": "2024-03-10"},
    {"customer_id": 4, "name": "Emily Davis", "email": "emily.davis@email.com", "join_date": "2024-04-05"},
    {"customer_id": 5, "name": "David Wilson", "email": "david.wilson@email.com", "join_date": "2024-05-12"},
    {"customer_id": 6, "name": "Lisa Anderson", "email": "lisa.anderson@email.com", "join_date": "2024-06-01"}
]

products = [
    {"product_id": 1, "product_name": "Coca Cola", "category": "Drinks", "price": 1.50},
    {"product_id": 2, "product_name": "Pepsi", "category": "Drinks", "price": 1.45},
    {"product_id": 3, "product_name": "Bread Loaf", "category": "Bakery", "price": 2.99},
    {"product_id": 4, "product_name": "Milk Gallon", "category": "Dairy", "price": 3.89},
    {"product_id": 5, "product_name": "Chips", "category": "Snacks", "price": 2.25},
    {"product_id": 6, "product_name": "Orange Juice", "category": "Drinks", "price": 4.50},
    {"product_id": 7, "product_name": "Cookies", "category": "Snacks", "price": 3.75},
    {"product_id": 8, "product_name": "Cheese", "category": "Dairy", "price": 5.99}
]

orders = [
    {"order_id": 1, "customer_id": 1, "product_id": 1, "quantity": 2, "order_date": "2024-06-01"},
    {"order_id": 2, "customer_id": 1, "product_id": 3, "quantity": 1, "order_date": "2024-06-01"},
    {"order_id": 3, "customer_id": 2, "product_id": 2, "quantity": 3, "order_date": "2024-06-02"},
    {"order_id": 4, "customer_id": 2, "product_id": 5, "quantity": 2, "order_date": "2024-06-02"},
    {"order_id": 5, "customer_id": 3, "product_id": 4, "quantity": 1, "order_date": "2024-06-03"},
    {"order_id": 6, "customer_id": 4, "product_id": 6, "quantity": 2, "order_date": "2024-06-04"},
    {"order_id": 7, "customer_id": 4, "product_id": 7, "quantity": 1, "order_date": "2024-06-04"},
    {"order_id": 8, "customer_id": 5, "product_id": 1, "quantity": 4, "order_date": "2024-06-05"},
    {"order_id": 9, "customer_id": 5, "product_id": 8, "quantity": 1, "order_date": "2024-06-05"},
    {"order_id": 10, "customer_id": 1, "product_id": 2, "quantity": 1, "order_date": "2024-06-06"},
    {"order_id": 11, "customer_id": 3, "product_id": 5, "quantity": 3, "order_date": "2024-06-07"},
    {"order_id": 12, "customer_id": 2, "product_id": 4, "quantity": 2, "order_date": "2024-06-08"}
]

# Helper functions
def get_product_by_id(product_id):
    """Get product details by ID"""
    for product in products:
        if product["product_id"] == product_id:
            return product
    return None

def get_customer_by_id(customer_id):
    """Get customer details by ID"""
    for customer in customers:
        if customer["customer_id"] == customer_id:
            return customer
    return None

def convert_currency(amount, exchange_rate=0.85):
    """Convert USD to EUR (default rate)"""
    return round(amount * exchange_rate, 2)

def apply_discount(amount, discount_percent=10):
    """Apply discount to amount"""
    return round(amount * (1 - discount_percent/100), 2)

def simulate_new_orders():
    """Simulate new orders using lists and dictionaries"""
    print("🔄 Simulating New Orders...")
    
    new_orders = [
        {"customer_id": 6, "product_id": 1, "quantity": 5, "order_date": "2024-06-09"},
        {"customer_id": 3, "product_id": 6, "quantity": 2, "order_date": "2024-06-09"},
        {"customer_id": 4, "product_id": 8, "quantity": 3, "order_date": "2024-06-10"}
    ]
    
    print(f"   Adding {len(new_orders)} new orders...")
    
    # Add new orders to existing orders list
    next_order_id = max(order["order_id"] for order in orders) + 1
    
    for i, new_order in enumerate(new_orders):
        new_order["order_id"] = next_order_id + i
        orders.append(new_order)
        
        # Calculate order total
        product = get_product_by_id(new_order["product_id"])
        customer = get_customer_by_id(new_order["customer_id"])
        total = product["price"] * new_order["quantity"]
        
        print(f"   ✅ Order #{new_order['order_id']}: {customer['name']} - {product['product_name']} x{new_order['quantity']} = ${total:.2f}")

def flag_large_orders(threshold=100):
    """Flag orders with total > threshold"""
    print(f"\n🚩 Flagging Large Orders (> ${threshold})...")
    
    large_orders = []
    
    for order in orders:
        product = get_product_by_id(order["product_id"])
        customer = get_customer_by_id(order["customer_id"])
        total = product["price"] * order["quantity"]
        
        if total > threshold:
            large_orders.append({
                "order_id": order["order_id"],
                "customer_name": customer["name"],
                "product_name": product["product_name"],
                "quantity": order["quantity"],
                "total": total,
                "order_date": order["order_date"]
            })
    
    if large_orders:
        for order in large_orders:
            print(f"   🔥 LARGE ORDER: #{order['order_id']} - {order['customer_name']} - ${order['total']:.2f}")
    else:
        print("   No large orders found.")
    
    return large_orders

def currency_conversion_analysis():
    """Convert prices to EUR and apply conditional discounts"""
    print("\n💱 Currency Conversion & Discount Analysis...")
    
    eur_products = []
    
    for product in products:
        eur_price = convert_currency(product["price"])
        
        # Apply discount for expensive items (> €4)
        if eur_price > 4:
            discounted_price = apply_discount(eur_price, 15)  # 15% discount
            eur_products.append({
                "product_name": product["product_name"],
                "usd_price": product["price"],
                "eur_price": eur_price,
                "discounted_price": discounted_price,
                "discount_applied": True
            })
        else:
            eur_products.append({
                "product_name": product["product_name"],
                "usd_price": product["price"],
                "eur_price": eur_price,
                "discounted_price": eur_price,
                "discount_applied": False
            })
    
    for product in eur_products:
        discount_text = " (15% discount)" if product["discount_applied"] else ""
        print(f"   {product['product_name']}: ${product['usd_price']:.2f} → €{product['discounted_price']:.2f}{discount_text}")
    
    return eur_products

def generate_comprehensive_report():
    """Generate comprehensive analysis report"""
    print("\n📊 Generating Comprehensive Report...")
    
    # Calculate total products sold
    total_products_sold = sum(order["quantity"] for order in orders)
    
    # Find most popular product
    product_sales = defaultdict(int)
    product_revenue = defaultdict(float)
    
    for order in orders:
        product_sales[order["product_id"]] += order["quantity"]
        product = get_product_by_id(order["product_id"])
        product_revenue[order["product_id"]] += product["price"] * order["quantity"]
    
    most_popular_product_id = max(product_sales, key=product_sales.get)
    most_popular_product = get_product_by_id(most_popular_product_id)
    
    # Calculate revenue per customer
    customer_revenue = defaultdict(float)
    customer_order_count = defaultdict(int)
    
    for order in orders:
        product = get_product_by_id(order["product_id"])
        customer_revenue[order["customer_id"]] += product["price"] * order["quantity"]
        customer_order_count[order["customer_id"]] += 1
    
    # Calculate category performance
    category_performance = defaultdict(lambda: {"quantity": 0, "revenue": 0})
    
    for order in orders:
        product = get_product_by_id(order["product_id"])
        category_performance[product["category"]]["quantity"] += order["quantity"]
        category_performance[product["category"]]["revenue"] += product["price"] * order["quantity"]
    
    # Build comprehensive report
    report = {
        "report_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "total_orders": len(orders),
            "total_products_sold": total_products_sold,
            "total_revenue": sum(customer_revenue.values()),
            "total_customers": len(set(order["customer_id"] for order in orders)),
            "average_order_value": sum(customer_revenue.values()) / len(orders)
        },
        "most_popular_product": {
            "product_name": most_popular_product["product_name"],
            "category": most_popular_product["category"],
            "times_sold": product_sales[most_popular_product_id],
            "total_revenue": product_revenue[most_popular_product_id]
        },
        "customer_analysis": [],
        "category_performance": {},
        "top_products": []
    }
    
    # Add customer analysis
    for customer_id, revenue in customer_revenue.items():
        customer = get_customer_by_id(customer_id)
        report["customer_analysis"].append({
            "customer_name": customer["name"],
            "email": customer["email"],
            "total_spent": round(revenue, 2),
            "total_orders": customer_order_count[customer_id],
            "average_order_value": round(revenue / customer_order_count[customer_id], 2)
        })
    
    # Sort customers by total spent
    report["customer_analysis"].sort(key=lambda x: x["total_spent"], reverse=True)
    
    # Add category performance
    for category, data in category_performance.items():
        report["category_performance"][category] = {
            "total_quantity_sold": data["quantity"],
            "total_revenue": round(data["revenue"], 2),
            "average_price": round(data["revenue"] / data["quantity"], 2)
        }
    
    # Add top products by revenue
    for product_id, revenue in sorted(product_revenue.items(), key=lambda x: x[1], reverse=True):
        product = get_product_by_id(product_id)
        report["top_products"].append({
            "product_name": product["product_name"],
            "category": product["category"],
            "price": product["price"],
            "quantity_sold": product_sales[product_id],
            "total_revenue": round(revenue, 2)
        })
    
    return report

def print_formatted_report(report):
    """Print nicely formatted report summary"""
    print("\n" + "="*60)
    print("📈 MINI-MART ANALYSIS REPORT")
    print("="*60)
    print(f"Report Generated: {report['report_date']}")
    print()
    
    # Summary
    print("📋 SUMMARY")
    print("-" * 30)
    print(f"Total Orders: {report['summary']['total_orders']}")
    print(f"Total Products Sold: {report['summary']['total_products_sold']}")
    print(f"Total Revenue: ${report['summary']['total_revenue']:.2f}")
    print(f"Total Customers: {report['summary']['total_customers']}")
    print(f"Average Order Value: ${report['summary']['average_order_value']:.2f}")
    print()
    
    # Most Popular Product
    print("🏆 MOST POPULAR PRODUCT")
    print("-" * 30)
    pop_product = report['most_popular_product']
    print(f"Product: {pop_product['product_name']} ({pop_product['category']})")
    print(f"Times Sold: {pop_product['times_sold']}")
    print(f"Revenue Generated: ${pop_product['total_revenue']:.2f}")
    print()
    
    # Top 3 Customers
    print("👥 TOP 3 CUSTOMERS")
    print("-" * 30)
    for i, customer in enumerate(report['customer_analysis'][:3], 1):
        print(f"{i}. {customer['customer_name']}")
        print(f"   Total Spent: ${customer['total_spent']:.2f}")
        print(f"   Orders: {customer['total_orders']} (Avg: ${customer['average_order_value']:.2f})")
        print()
    
    # Category Performance
    print("📊 CATEGORY PERFORMANCE")
    print("-" * 30)
    for category, data in report['category_performance'].items():
        print(f"{category}: {data['total_quantity_sold']} items, ${data['total_revenue']:.2f} revenue")
    print()

def save_report_to_json(report, filename="minimart_analysis_report.json"):
    """Save report to JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
        print(f"✅ Report saved to {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving report: {e}")
        return False

def main():
    """Main execution function"""
    print("🏪 Mini-Mart Analysis System")
    print("="*40)
    
    # 1. Simulate new orders
    simulate_new_orders()
    
    # 2. Flag large orders
    large_orders = flag_large_orders(threshold=10)  # Lower threshold for demo
    
    # 3. Currency conversion and discount analysis
    eur_products = currency_conversion_analysis()
    
    # 4. Generate comprehensive report
    report = generate_comprehensive_report()
    
    # 5. Print formatted summary
    print_formatted_report(report)
    
    # 6. Save to JSON
    save_success = save_report_to_json(report)
    
    # 7. Additional analysis
    print("🔍 ADDITIONAL INSIGHTS")
    print("-" * 30)
    
    # Find customers who haven't ordered
    all_customer_ids = {customer["customer_id"] for customer in customers}
    ordering_customer_ids = {order["customer_id"] for order in orders}
    inactive_customers = all_customer_ids - ordering_customer_ids
    
    if inactive_customers:
        print("😴 Inactive Customers:")
        for customer_id in inactive_customers:
            customer = get_customer_by_id(customer_id)
            print(f"   - {customer['name']} ({customer['email']})")
    else:
        print("🎉 All customers have placed orders!")
    
    print()
    print("📈 Analysis Complete!")
    print("="*40)

if __name__ == "__main__":
    main()
