import pandas as pd

def generate_report(customers, products, orders, order_items):
    order_items["total_price"] = order_items["unit_price"] * order_items["quantity"]

    total_products_sold = order_items["quantity"].sum()

    popular = order_items.groupby("product_id")["quantity"].sum().idxmax()
    most_popular = products.loc[products["product_id"] == popular, "name"].values[0]

    orders_with_customers = order_items.merge(orders, on="order_id") \
                                       .merge(customers, on="customer_id")
    revenue_per_customer = orders_with_customers.groupby("name")["total_price"].sum().to_dict()

    return {
        "Total Products Sold": total_products_sold,
        "Most Popular Product": most_popular,
        "Revenue per Customer": revenue_per_customer
    }