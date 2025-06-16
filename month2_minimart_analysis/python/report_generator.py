# Code to generate dictionary summary reports
from utils import customers_df, products_df, orders_df
import json

# Total products sold
total_sold = orders_df['quantity'].sum()

# Most popular product
merged = orders_df.merge(products_df, on='product_id')
popular = merged.groupby('product_name')['quantity'].sum().idxmax()

# Revenue per customer
revenue_df = merged.copy()
revenue_df['revenue'] = revenue_df['price'] * revenue_df['quantity']
revenue_per_customer = revenue_df.groupby('customer_id')['revenue'].sum().to_dict()

# Report dictionary
report = {
    "total_products_sold": int(total_sold),
    "most_popular_product": popular,
    "revenue_per_customer": revenue_per_customer
}


# Save to JSON file
with open("sales_report.json", "w") as f:
    json.dump(report, f, indent=4)

