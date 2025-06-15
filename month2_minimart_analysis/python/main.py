import pandas as pd
from report_generator import generate_report
from utils import apply_discount, load_csvs
customers, products, orders, order_items = load_csvs()
products["price"] = products["price"].astype(str)
products["discounted_price"] = products["price"].apply(lambda p: apply_discount(p, 10))
report = generate_report(customers, products, orders, order_items)
print("\n\U0001F4CA MiniMart Sales Report:")
for key, value in report.items():
    print(f"{key}: {value}")
