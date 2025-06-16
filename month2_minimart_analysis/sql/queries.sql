-- INSERT QUERIES
-- -------------

-- Retrieve all customers
SELECT * FROM customers;

-- Retrieve all products
SELECT * FROM products;

-- Filter products by category (Drinks)
SELECT * FROM products WHERE category = 'Drinks';

-- List recent orders by date (most recent first)
SELECT * FROM orders ORDER BY order_date DESC;

-- AGGREGATION QUERIES
-- ------------------

-- Count total number of orders
SELECT COUNT(*) as total_orders FROM orders;

-- Calculate revenue per product (price × quantity)
SELECT 
    p.product_name,
    p.price,
    SUM(o.quantity) as total_quantity_sold,
    SUM(p.price * o.quantity) as total_revenue
FROM products p
JOIN orders o ON p.product_id = o.product_id
GROUP BY p.product_id, p.product_name, p.price
ORDER BY total_revenue DESC;

-- Find average product price
SELECT AVG(price) as average_price FROM products;

-- Find average product price by category
SELECT category, AVG(price) as average_price 
FROM products 
GROUP BY category;

-- JOIN QUERIES
-- -----------

-- INNER JOIN: Get detailed order information
SELECT 
    o.order_id,
    c.name as customer_name,
    p.product_name,
    p.category,
    o.quantity,
    p.price,
    (o.quantity * p.price) as total_amount,
    o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id
ORDER BY o.order_date DESC;

-- LEFT JOIN: List all customers and their orders (including customers with no orders)
SELECT 
    c.customer_id,
    c.name,
    c.email,
    o.order_id,
    o.order_date,
    COALESCE(SUM(p.price * o.quantity), 0) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.name, c.email, o.order_id, o.order_date
ORDER BY c.customer_id;

-- LEFT JOIN: Show all products, including those that haven't been ordered
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    COALESCE(SUM(o.quantity), 0) as times_ordered,
    COALESCE(SUM(p.price * o.quantity), 0) as total_revenue
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id
GROUP BY p.product_id, p.product_name, p.category, p.price
ORDER BY times_ordered DESC;

