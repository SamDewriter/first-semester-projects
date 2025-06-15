-- SQL script to create necessary tables

-- Create Database
CREATE DATABASE mini_mart_db;

-- Grant Permissions
GRANT ALL PRIVILEGES ON DATABASE mini_mart_db TO dubem_user;

-- Create customers Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    join_date TIMESTAMPTZ DEFAULT NOW()
);
    
-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    product_name TEXT NOT NULL UNIQUE, -- to aviod duplicate names
    category TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0)
);


-- Create orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    order_date TIMESTAMPTZ DEFAULT NOW()
);