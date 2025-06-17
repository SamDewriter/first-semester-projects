-- SQL script to insert sample data
INSERT INTO customers (name, email, join_date)
VALUES
('Alice Smith',      'alice.smith@example.com',   '2024-02-14'),
('Bob Johnson',      'bob.johnson@example.com',   '2024-03-21'),
('Charlie Davis',    'charlie.davis@example.com', '2024-05-10'),
('Diana Garcia',     'diana.garcia@example.com',  '2024-06-01'),
('Ethan Brown',      'ethan.brown@example.com',   '2024-06-15'),
('Fiona Lee',        'fiona.lee@example.com',     '2024-07-09'),
('George Clark',     'george.clark@example.com',  '2024-08-23'),
('Hannah Wilson',    'hannah.wilson@example.com', '2024-09-05'),
('Isaac Martinez',   'isaac.martinez@example.com','2024-10-11'),
('Julia Adams',      'julia.adams@example.com',   '2024-11-29'),
('Kevin Turner',     'kevin.turner@example.com',  '2025-01-03'),
('Laura Perez',      'laura.perez@example.com',   '2025-01-17'),
('Michael Scott',    'michael.scott@example.com', '2025-02-01'),
('Natalie King',     'natalie.king@example.com',  '2025-02-14'),
('Oliver Young',     'oliver.young@example.com',  '2025-03-02');

INSERT INTO products (product_name, category, price)
VALUES
('Laptop Pro 15',            'Electronics', 1299.99),
('Wireless Mouse',           'Electronics',   29.99),
('Office Desk',              'Furniture',    249.99),
('Ergonomic Chair',          'Furniture',    399.99),
('Noise‑Cancelling Headphones','Electronics',199.99),
('Smartphone X',             'Electronics',  999.99),
('Standing Desk Converter',  'Furniture',    159.99),
('4K Monitor 27"',           'Electronics',  449.99),
('Portable SSD 1TB',         'Electronics',  119.99),
('LED Desk Lamp',            'Home',          39.99),
('Bluetooth Speaker',        'Electronics',   79.99),
('Gaming Keyboard',          'Electronics',   89.99),
('Coffee Maker',             'Home',          59.99),
('Water Bottle Stainless',   'Sports',        24.99),
('Yoga Mat',                 'Sports',        34.99);

INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES
((SELECT customer_id FROM customers WHERE email = 'alice.smith@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Laptop Pro 15'),
 1, '2025-03-10'),

((SELECT customer_id FROM customers WHERE email = 'bob.johnson@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Wireless Mouse'),
 2, '2025-03-11'),

((SELECT customer_id FROM customers WHERE email = 'charlie.davis@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Ergonomic Chair'),
 1, '2025-03-12'),

((SELECT customer_id FROM customers WHERE email = 'diana.garcia@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = '4K Monitor 27"'),
 2, '2025-03-13'),

((SELECT customer_id FROM customers WHERE email = 'ethan.brown@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Smartphone X'),
 1, '2025-03-13'),

((SELECT customer_id FROM customers WHERE email = 'fiona.lee@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Noise‑Cancelling Headphones'),
 1, '2025-03-14'),

((SELECT customer_id FROM customers WHERE email = 'george.clark@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Office Desk'),
 1, '2025-03-15'),

((SELECT customer_id FROM customers WHERE email = 'hannah.wilson@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Portable SSD 1TB'),
 3, '2025-03-15'),

((SELECT customer_id FROM customers WHERE email = 'isaac.martinez@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Standing Desk Converter'),
 1, '2025-03-15'),

((SELECT customer_id FROM customers WHERE email = 'julia.adams@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'LED Desk Lamp'),
 2, '2025-03-16'),

((SELECT customer_id FROM customers WHERE email = 'kevin.turner@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Bluetooth Speaker'),
 1, '2025-03-16'),

((SELECT customer_id FROM customers WHERE email = 'laura.perez@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Gaming Keyboard'),
 1, '2025-03-16'),

((SELECT customer_id FROM customers WHERE email = 'michael.scott@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Coffee Maker'),
 1, '2025-03-17'),

((SELECT customer_id FROM customers WHERE email = 'natalie.king@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Water Bottle Stainless'),
 4, '2025-03-17'),

((SELECT customer_id FROM customers WHERE email = 'oliver.young@example.com'),
 (SELECT product_id  FROM products  WHERE product_name = 'Yoga Mat'),
 2, '2025-03-18');
