# Utility functions for data conversion and filtering


# #### 🧩 Python Tasks

# - Simulate new orders using `lists` or `dictionaries`
# - Use conditionals to flag **large orders** (e.g., total > $100)
# - Convert product prices to another currency and apply conditional discounts
# - Generate a dictionary report including:
#   - ✅ Total products sold
#   - ✅ Most popular product
#   - ✅ Revenue per customer

import pandas as pd
import random



def append_new_order(orders_path, customers_df, products_df):
    # Load existing orders
    orders_df = pd.read_csv(orders_path)

    # Create a new random order
    new_order = {
        "order_id": orders_df["order_id"].max() + 1 if not orders_df.empty else 1,
        "customer_id": random.choice(customers_df["customer_id"]),
        "product_id": random.choice(products_df["product_id"]),
        "quantity": random.randint(1, 20),
        "order_date": pd.Timestamp.today().date()
    }

    # Append and save
    new_order_df = pd.DataFrame([new_order])
    updated_orders_df = pd.concat([orders_df, new_order_df], ignore_index=True)
    updated_orders_df.to_csv(orders_path, index=False)
    
    print("✅ New order added successfully.")



def flag_large_orders(orders_path, products_path, threshold=20000):
    """
    Flags and displays orders where total (quantity * price) exceeds the given threshold.
    """
    orders_df = pd.read_csv(orders_path)
    products_df = pd.read_csv(products_path)

    # Merge orders with products on product_id
    merged_df = pd.merge(orders_df, products_df, on="product_id")

    # Calculate total order value
    merged_df["total_value"] = merged_df["quantity"] * merged_df["price"]

    # Filter for large orders
    large_orders = merged_df[merged_df["total_value"] > threshold]

    # Display
    print(f"\n📦 Found {len(large_orders)} large order(s) over ${threshold}:\n")
    for _, row in large_orders.iterrows():
        print(f"- Order ID: {row['order_id']} | Product: {row['product_name']} | Qty: {row['quantity']} | Total: ${row['total_value']:.2f}")

    return large_orders




def convert_and_discount_prices(products_df, exchange_rate=0.85, discount_threshold=1000, discount_rate=0.1):
    """
    Converts product prices to another currency and applies conditional discounts.

    Args:
        products_df (pd.DataFrame): DataFrame containing product info with a 'price' column (in USD).
        exchange_rate (float): Conversion rate to target currency (e.g., 1 USD = 0.85 EUR).
        discount_threshold (float): Minimum price (in USD) to apply discount after conversion.
        discount_rate (float): Discount rate to apply (e.g., 0.1 = 10%).

    Returns:
        pd.DataFrame: Updated DataFrame with 'converted_price' and 'final_price' columns.
    """
    products_df = products_df.copy()

    # Step 1: Convert price
    products_df['converted_price'] = products_df['price'] * exchange_rate

    # Step 2: Apply discount conditionally
    products_df['final_price'] = products_df['converted_price'].apply(
        lambda x: x * (1 - discount_rate) if x > discount_threshold else x
    )
    
    return products_df



def generate_sales_report(orders_df, products_df, customers_df):
    """
    Generates a summary dictionary including:
    - Total products sold
    - Most popular product
    - Revenue per customer

    Args:
        orders_df (pd.DataFrame): Orders with 'product_id', 'customer_id', and 'quantity'
        products_df (pd.DataFrame): Products with 'product_id' and 'price'
        customers_df (pd.DataFrame): Customers with 'customer_id' and 'name'

    Returns:
        dict: Summary report
    """
    # Merge orders with product prices
    merged = orders_df.merge(products_df, on="product_id", how="left")

    # 1. Total products sold
    total_products_sold = merged["quantity"].sum()

    # 2. Most popular product by quantity
    most_popular_product_id = merged.groupby("product_id")["quantity"].sum().idxmax()
    most_popular_product_name = products_df.loc[
        products_df["product_id"] == most_popular_product_id, "product_name"
    ].values[0]

    # 3. Revenue per customer
    merged["total_value"] = merged["quantity"] * merged["price"]
    revenue_df = merged.groupby("customer_id")["total_value"].sum().reset_index()
    revenue_df = revenue_df.merge(customers_df, on="customer_id", how="left")

    revenue_per_customer = {
        row["name"]: round(row["total_value"], 2) for _, row in revenue_df.iterrows()
    }

    return {
        "total_products_sold": total_products_sold,
        "most_popular_product": most_popular_product_name,
        "revenue_per_customer": revenue_per_customer
    }