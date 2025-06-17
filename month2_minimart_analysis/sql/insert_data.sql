-- SQL script to insert sample data
INSERT INTO customers (name, email, join_date, phone) VALUES
('Opeyemi Ayeni', 'a.opeyemi@gmail.com', '2023-01-15','08165114690'),
('Michael Chinedu', 'michael.c@gmail.com', '2023-02-20','08166004690'),
('Emma Orunkoyi', 'emma.r@gmail.com', '2023-05-05','08175114690'), 
('Kim Dave', 'davidkim@yahoo.com', '2023-04-10','07065114690'),
('Ayeni Moyinoluwa', 'moyin@yahoo.com','2025-06-17','08165114100' );

INSERT INTO products (product_name, category, price) VALUES
('50g peak Milk', 'Dairy', 5000.00),
('Bokku Bread', 'Bakery', 1300.00),
('Egg', 'Dairy', 300.00),
('Apples', 'fruit', 1000.00),
('Coke 50cl', 'Drinks', 500.00),
('Table water', 'Drinks', 200.00);

INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 3, 2, '2023-11-01'),  
(2, 1, 1, '2024-10-02'),   
(3, 4, 3, '2023-11-02'),   
(1, 2, 2, '2024-11-03'),   
(4, 5, 6, '2024-11-03');
