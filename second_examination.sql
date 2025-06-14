-- Task 1: Creating the tables
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    join_date DATE NOT NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Task 2: Altering one of the tables to add a new column
ALTER TABLE products ADD COLUMN stock INTEGER DEFAULT 0;

-- Task 3: Inserting at 5 rows into each table

-- Insert customers
INSERT INTO customers VALUES 
(1, 'Kola Aderoju', 'kolaaderoju@example.com', '2025-01-15'),
(2, 'Ishola Rokibat', 'isholarokibat@example.com', '2025-02-20'),
(3, 'Oladele Joseph', 'josephola@example.com', '2025-03-10'),
(4, 'Omotosho Mubarak', 'omotoshomubarak@example.com', '2025-04-05'),
(5, 'Abiade Zainab', 'abiadezainab@example.com', '2025-05-12');

-- Insert products
INSERT INTO products VALUES 
(1, 'Phone', 2.99, 'Telecommunications', 50),
(2, 'Cars', 1.99, 'Automobiles', 100),
(3, 'Eggs', 3.49, 'Dairy', 75),
(4, 'Corn', 0.99, 'Cereals', 200),
(5, 'Chicken', 5.99, 'Meat', 30);

-- Insert orders
INSERT INTO orders VALUES 
(1, 1, '2025-06-01'),
(2, 2, '2025-06-02'),
(3, 1, '2025-06-03'),
(4, 3, '2025-06-03'),
(5, 4, '2025-06-04');

-- Insert order items
INSERT INTO order_items VALUES 
(1, 1, 1, 2),
(2, 1, 2, 1),
(3, 2, 3, 1),
(4, 2, 4, 5),
(5, 3, 5, 2),
(6, 4, 1, 3),
(7, 5, 2, 2),
(8, 5, 3, 1);

-- Task 4: Retrieving all orders made by a specific customer
SELECT o.order_id, o.order_date 
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.name = 'Kola Aderoju';

-- Task 5: Get the total number of orders
SELECT COUNT(*) AS total_orders FROM orders;

-- Task 6: Calculate the total revenue from all orders
SELECT SUM(p.price * oi.quantity) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;

-- Task 7: Using INNER JOIN to show order details including customer and product names
SELECT c.name AS customer_name, 
       o.order_date, 
       p.name AS product_name, 
       oi.quantity, 
       p.price,
       (p.price * oi.quantity) AS item_total
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON oi.product_id = p.product_id;

-- Task 8: Using LEFT JOIN to show all products and any related order (even if not sold)
SELECT p.name AS product_name, 
       p.price, 
       COALESCE(SUM(oi.quantity), 0) AS total_quantity_sold,
       COALESCE(SUM(p.price * oi.quantity), 0) AS total_revenue
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.name, p.price;

