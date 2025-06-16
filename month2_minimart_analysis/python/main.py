# Entry point for the MiniMart data reporting system
# - Simulate new orders using `lists` or `dictionaries`
# - Use conditionals to flag **large orders** (e.g., total > $100)
# - Convert product prices to another currency and apply conditional discounts
# - Generate a dictionary report including:
#   - ✅ Total products sold
#   - ✅ Most popular product
#   - ✅ Revenue per customer


# main.py - MiniMart Order Management Entry Script

# Import necessary functions from utility and report modules
from utils import append_new_order, flag_large_orders, convert_and_discount_prices
from report_generator import generate_sales_report  
import pandas as pd
import json

# Load customer, product, and order data from CSV files
customers_df = pd.read_csv(r"/Users/home/Documents/Altschool_project/first-semester-projects/month2_minimart_analysis/sql/customers.csv")
products_df = pd.read_csv(r"/Users/home/Documents/Altschool_project/first-semester-projects/month2_minimart_analysis/sql/products.csv")
orders_df = pd.read_csv(r"/Users/home/Documents/Altschool_project/first-semester-projects/month2_minimart_analysis/sql/orders.csv")

# File paths (used by functions that operate directly on file-based input)
orders_path = "/Users/home/Documents/Altschool_project/first-semester-projects/month2_minimart_analysis/sql/orders.csv"
products_path = "/Users/home/Documents/Altschool_project/first-semester-projects/month2_minimart_analysis/sql/products.csv"

# Function to display the menu options
def show_menu():
    print("\n MiniMart Order Management Menu")
    print("1.  Add new order")
    print("2.  Flag large orders")
    print("3.  Convert prices & apply discounts")
    print("4.  Generate sales report")
    print("5.  Exit")

# Infinite loop to keep showing menu until user exits
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ").strip()

    # Option 1: Append a new order to the dataset
    if choice == "1":
        append_new_order(orders_path, customers_df, products_df)

    # Option 2: Identify and display orders with total value > threshold
    elif choice == "2":
        flag_large_orders(orders_path, products_path)

    # Option 3: Convert prices to another currency and apply discounts
    elif choice == "3":
        converted_df = convert_and_discount_prices(
            products_df,
            exchange_rate=0.9,        # Example rate (e.g., NGN to USD)
            discount_threshold=800,   # Discount for products over ₦800
            discount_rate=0.15        # 15% discount
        )
        print(converted_df[['product_name', 'price', 'converted_price', 'final_price']])
        
    # Option 4: Generate and save a sales summary report as JSON
    elif choice == "4":
        generate_sales_report(orders_path, customers_df, products_df)

    # Option 5: Exit the program
    elif choice == "5":
        print("Exiting. Goodbye!")
        break

    # Catch-all for invalid input
    else:
        print(" Invalid choice. Please enter a number between 1 and 5.")




