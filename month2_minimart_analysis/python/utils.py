# Utility functions for data conversion and filtering
import pandas as pd
import random
from datetime import datetime


# Simulate new orders using lists or dictionaries
# Use conditionals to flag large orders (e.g., total > $100)
# Convert product prices to another currency and apply conditional discounts
# Generate a dictionary report including:
# ✅ Total products sold
# ✅ Most popular product
# ✅ Revenue per customer


customers_df = pd.read_csv("customers.csv")
products_df = pd.read_csv("products.csv")
orders_df = pd.read_csv("orders.csv")

new_orders = [ ]


## Simulate new orders using lists or dictionaries
def new_order():
    for _ in range(5):
        orders = {
            "customer_id": random.choice(customers_df['customer_id']),
            "product_id": random.choice(products_df['product_id']),
            "quantity": random.randint(1, 5),
            "order_date": datetime.now().date()
        }
        new_orders.append(orders)
    
    #  Save to CSV
    new_orders_df = pd.DataFrame(new_orders)
    new_orders_df[['customer_id', 'product_id', 'quantity', 'order_date']].to_csv(
    "orders.csv", mode='a', index=False)

   
#Convert product prices to another currency 
EXCHANGE_RATE = 1500  # e.g., USD to NGN
def convert_currency():
    for order in new_orders:
        order['total_ngn'] = order['total'] * EXCHANGE_RATE
    # Apply 10% discount if order > 200 in USD
    for order in new_orders:
        if order['total'] > 200:
                order['discount_applied'] = True
                order['discounted_total'] = order['total'] * 0.9
        else:
            order['discount_applied'] = False
            order['discounted_total'] = order['total']


#Use conditionals to flag large orders (e.g., total > $100)
def merge_product():    
    for order in new_orders:
        product_price = products_df.loc[products_df['product_id'] == order['product_id'], 'price']
        order['total'] = order['quantity'] * product_price
        order['is_large_order'] = order['total'] > 100




