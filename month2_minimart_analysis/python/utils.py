# Utility functions for data conversion and filtering
import pandas as pd
import random
from datetime import datetime

customers_df = pd.read_csv("customers.csv")
products_df = pd.read_csv("products.csv")
orders_df = pd.read_csv("orders.csv")



# Sample new orders using dictionaries
new_orders = []
def new_order(): 
    for _ in range(5):
        order = {
            "customer_id": random.choice(customers_df['customer_id']),
            "product_id": random.choice(products_df['product_id']),
            "quantity": random.randint(1, 5),
            "order_date": datetime.now().date()
        }
    new_orders.append(order)


# Merge product prices into new_orders
def merge_product():    
    for order in new_orders:
        product_price = products_df.loc[products_df['product_id'] == order['product_id'], 'price'].values[0]
        order['total'] = order['quantity'] * product_price
        order['is_large_order'] = order['total'] > 100

#Convert product prices to another currency and apply conditional discounts
EXCHANGE_RATE = 1500  # e.g., USD to NGN
def convert_currency():
    for order in new_orders:
        order['total_ngn'] = order['total'] * EXCHANGE_RATE
        # Apply 10% discount if order > 200 in USD
        if order['total'] > 200:
            order['discount_applied'] = True
            order['discounted_total'] = order['total'] * 0.9
        else:
            order['discount_applied'] = False
            order['discounted_total'] = order['total']

