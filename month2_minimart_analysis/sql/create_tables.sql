-- SQL script to create necessary tables
CREATE TABLE customers
(customer_id SERIAL PRIMARY KEY,
  name VARCHAR(125),
  email VARCHAR(125),
  join_date DATE)

CREATE TABLE products(
  product_id SERIAL PRIMARY KEY,
  product_name VARCHAR(125),
  category VARCHAR(125),
  price INT
  )

  ALTER TABLE products 
  ALTER COLUMN price FLOAT

CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  quantity INT,
  order_date DATE,
  Foreign Key customer_id REFERENCES customers(customer_id), 
  Foreign Key product_id REFERENCES products(product_id)
)