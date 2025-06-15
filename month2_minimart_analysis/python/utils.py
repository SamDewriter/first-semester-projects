import pandas as pd
import os

# Get the absolute directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def apply_discount(price_str, discount_pct):
    try:
        price = float(price_str)
        return price * (1 - discount_pct / 100)
    except:
        return 0.0

def load_csvs():
    customers = pd.read_csv(os.path.join(BASE_DIR, "customers.csv"))
    products = pd.read_csv(os.path.join(BASE_DIR, "products.csv"))
    orders = pd.read_csv(os.path.join(BASE_DIR, "orders.csv"))
    order_items = pd.read_csv(os.path.join(BASE_DIR, "order_items.csv"))
    return customers, products, orders, order_items

if __name__ == "__main__":
    # Example order
    new_order = {
        "customer_id": 3,
        "products": [
            {"product_id": 2, "quantity": 5},
            {"product_id": 5, "quantity": 3}
        ]
    }

    for item in new_order["products"]:
        if item["quantity"] > 4 or (item["product_id"] == 2 and item["quantity"] >= 3):
            print(f"Large order alert: Product ID {item['product_id']} - Quantity {item['quantity']}")
