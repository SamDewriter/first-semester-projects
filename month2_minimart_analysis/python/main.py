# Entry point for the MiniMart data reporting system
from utils import get_transactions, convert_currency_get_discount
from report_generator import generate_sales_report
import json

while True:
    print("\n1. get transactions\n2. Convert Currency and Apply Discount\n3. Get Report\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1": # get transactions
        # define your products
        products = {
            1: {"name": "Organic Apples", "price": 3.50},
            2: {"name": "Whole Wheat Bread", "price": 4.25},
            3: {"name": "Cheddar Cheese Block", "price": 7.99},
            4: {"name": "Free-Range Eggs (Dozen)", "price": 5.49},
            5: {"name": "Natural Peanut Butter", "price": 6.00}
        }

        # define your orders
        customers_order = [
            {"customer_id": 5, "product_id": 1, "quantity": 30},
            {"customer_id": 2, "product_id": 3, "quantity": 2},
            {"customer_id": 1, "product_id": 5, "quantity": 5},
            {"customer_id": 3, "product_id": 2, "quantity": 10},
        ]

        get_transactions(products, customers_order)

    elif choice == "2": # currency conversion
        print("\n--- Applying Currency Conversions and Discounts ---")
        print("Enter Amount (USD): \n")
        amount = int(input())
        convert_currency_get_discount(amount)

    elif choice == "3": # reporting
        # Let's assume this is our full order history from the database

        order_history = [
            {'customer_id': 1, 'product_id': 2, 'quantity': 1},
            {'customer_id': 2, 'product_id': 5, 'quantity': 2},
            {'customer_id': 1, 'product_id': 4, 'quantity': 1},
            {'customer_id': 3, 'product_id': 1, 'quantity': 5},
            {'customer_id': 4, 'product_id': 3, 'quantity': 1}
        ]

        products = {
            1: {"name": "Organic Apples", "price": 3.50},
            2: {"name": "Whole Wheat Bread", "price": 4.25},
            3: {"name": "Cheddar Cheese Block", "price": 7.99},
            4: {"name": "Free-Range Eggs (Dozen)", "price": 5.49},
            5: {"name": "Natural Peanut Butter", "price": 6.00}
        }

        # --- Generate and display the report ---
        sales_report = generate_sales_report(order_history, products)

        print("\n--- Sales Report (JSON) ---")
        print(json.dumps(sales_report, indent=4))

        # Save the report to a .json file
        with open('report/sales_report.json', 'w') as f:
            json.dump(sales_report, f, indent=4)

        print("\nReport saved to sales_report.json")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Option.")

    
