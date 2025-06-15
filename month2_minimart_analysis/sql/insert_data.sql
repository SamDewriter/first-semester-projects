-- SQL script to insert sample data
-- Insert sample data into customers with @gmail.com emails
INSERT INTO customers (name, email, join_date) VALUES
('John Doe', 'johndoe@gmail.com', '2022-01-15'),
('Jane Smith', 'janesmith@gmail.com', '2023-03-22'),
('Alice Johnson', 'alicej@gmail.com', '2021-11-05'),
('Bob Brown', 'bobbrown@gmail.com', '2024-02-10'),
('Emily Davis', 'emilyd@gmail.com', '2023-07-30');

-- Insert sample data into products
INSERT INTO products (product_name, category, price) VALUES
('Wireless Mouse', 'Electronics', 25.99),
('Bluetooth Headphones', 'Electronics', 79.49),
('Coffee Maker', 'Home Appliances', 49.95),
('Yoga Mat', 'Fitness', 20.00),
('Smartwatch', 'Electronics', 199.99);

-- Insert sample data into orders
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 2, 1, '2024-03-15'),
(2, 3, 2, '2024-04-01'),
(3, 1, 3, '2024-05-10'),
(4, 5, 1, '2024-06-05'),
(5, 4, 2, '2024-06-12');