from faker import Faker
import pandas as pd
import random

fake = Faker()


def generate_customers(n=10):
    data = []
    for i in range(1, n + 1):
        name = fake.name()
        email = fake.email()
        join_date = fake.date_between(start_date='-2y', end_date='today')
        data.append({
            "customer_id": i,
            "name": name,
            "email": email,
            "join_date": join_date
        })
    return pd.DataFrame(data)


def generate_products(n=5):
    categories = ["Books", "Electronics", "Toys", "Books", "Books"]
    data = []
    for i in range(1, n + 1):
        product_name = fake.word().capitalize()
        category = random.choice(categories)
        price = round(random.uniform(10, 500), 2)
        data.append({
            "product_id": i,
            "product_name": product_name,
            "category": category,
            "price": price
        })
    return pd.DataFrame(data)


def generate_orders(customers_df, products_df, n=20):
    data = []
    for i in range(1, n + 1):
        customer_id = random.choice(customers_df["customer_id"].tolist())
        product_id = random.choice(products_df["product_id"].tolist())
        quantity = random.randint(1, 10)
        order_date = fake.date_between(start_date='-1y', end_date='today')
        data.append({
            "order_id": i,
            "customer_id": customer_id,
            "product_id": product_id,
            "quantity": quantity,
            "order_date": order_date
        })
    return pd.DataFrame(data)


customers_df = generate_customers(10)
products_df = generate_products(5)
orders_df = generate_orders(customers_df, products_df, 20)


customers_df.dropna(inplace=True)
products_df.dropna(inplace=True)
orders_df.dropna(inplace=True)


customers_df.to_csv("customers.csv", index=False)
products_df.to_csv("products.csv", index=False)
orders_df.to_csv("orders.csv", index=False)

print("✅ All data generated with no NULLs and saved as CSVs.")
