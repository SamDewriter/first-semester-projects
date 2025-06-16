# report.py
import pandas as pd
import json
import os

def generate_sales_report(
    orders_path,
    customers_df,
    products_df,
    output_file="/Users/home/Documents/Altschool_project/first-semester-projects/month2_minimart_analysis/sales_report.json"
):
    # Read the orders CSV
    orders_df = pd.read_csv(orders_path)

    # Merge orders with products and customers
    merged = orders_df.merge(products_df, on="product_id", how="left")
    merged = merged.merge(customers_df, on="customer_id", how="left")

    # Total products sold
    total_products_sold = int(merged["quantity"].sum())

    # Most popular product
    popular_product = merged.groupby("product_name")["quantity"].sum().idxmax()

    # Revenue per customer
    merged["revenue"] = merged["quantity"] * merged["price"]
    revenue_per_customer_df = (
        merged.groupby("customer_id")["revenue"].sum().reset_index()
    )
    detailed = revenue_per_customer_df.merge(customers_df, on="customer_id", how="left")

    # Convert to dict (name -> revenue) with float-safe values
    revenue_per_customer = {
        str(name): float(revenue)
        for name, revenue in zip(detailed["name"], detailed["revenue"])
    }

    # Final report dictionary
    report = {
        "total_products_sold": total_products_sold,
        "most_popular_product": popular_product,
        "revenue_per_customer": revenue_per_customer,
    }

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Save to JSON
    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)

    print(f"✅ Sales report saved to {output_file}")
