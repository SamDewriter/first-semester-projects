-- -- 2. INSERT SAMPLE DATA
-- ====================

-- Insert customers data
INSERT INTO customers (customer_id, name, email, join_date) VALUES
(1, 'Sarah Uko', 'sarah.uko@email.com', '2024-01-15'),
(2, 'Sarah Johnson', 'sarah.johnson@email.com', '2024-02-20'),
(3, 'Mike Brown', 'mike.brown@email.com', '2024-03-10'),
(4, 'Emily Davis', 'emily.davis@email.com', '2024-04-05'),
(5, 'David Wilson', 'david.wilson@email.com', '2024-05-12'),
(6, 'Lisa Anderson', 'lisa.anderson@email.com', '2024-06-01');

-- Insert products data
INSERT INTO products (product_id, product_name, category, price) VALUES
(1, 'Coca Cola', 'Drinks', 1.50),
(2, 'Pepsi', 'Drinks', 1.45),
(3, 'Bread Loaf', 'Bakery', 2.99),
(4, 'Milk Gallon', 'Dairy', 3.89),
(5, 'Chips', 'Snacks', 2.25),
(6, 'Orange Juice', 'Drinks', 4.50),
(7, 'Cookies', 'Snacks', 3.75),
(8, 'Cheese', 'Dairy', 5.99);

-- Insert orders data
INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date) VALUES
(1, 1, 1, 2, '2024-06-01'),
(2, 1, 3, 1, '2024-06-01'),
(3, 2, 2, 3, '2024-06-02'),
(4, 2, 5, 2, '2024-06-02'),
(5, 3, 4, 1, '2024-06-03'),
(6, 4, 6, 2, '2024-06-04'),
(7, 4, 7, 1, '2024-06-04'),
(8, 5, 1, 4, '2024-06-05'),
(9, 5, 8, 1, '2024-06-05'),
(10, 1, 2, 1, '2024-06-06'),
(11, 3, 5, 3, '2024-06-07'),
(12, 2, 4, 2, '2024-06-08');
