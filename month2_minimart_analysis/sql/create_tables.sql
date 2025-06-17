-- SQL script to create necessary tables
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY, 
    name VARCHAR(100) NOT NULL, 
    email VARCHAR(100) UNIQUE NOT NULL, 
    join_date DATE DEFAULT CURRENT_DATE
    );

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE orders (
    order_id     SERIAL PRIMARY KEY,
    customer_id  INT,
    product_id   INT,
    quantity     INT,
    order_date   DATE NOT NULL DEFAULT CURRENT_DATE,
    
 FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
 FOREIGN KEY (product_id) REFERENCES products(product_id)
 
 );
