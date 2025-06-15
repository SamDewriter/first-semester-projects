-- SQL queries for retrieving insights
-- ============================================
-- BASIC QUERIES
-- ============================================

-- Retrieve all customers
SELECT * FROM customers;

-- Retrieve all products
SELECT * FROM products;

-- Filter products by category (Example: 'Electronics')
SELECT * FROM products
WHERE category = 'Electronics';

-- List recent orders by order date descending
SELECT * FROM orders
ORDER BY order_date DESC;

-- ============================================
-- AGGREGATION QUERIES
-- ============================================

-- Find total number of orders
SELECT COUNT(*) AS total_orders FROM orders;

-- Calculate revenue per product
SELECT 
    p.product_id,
    p.product_name,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_id, p.product_name;

-- Find average product price
SELECT AVG(price) AS avg_price FROM products;

-- ============================================
-- JOIN QUERIES
-- ============================================

-- INNER JOIN: Detailed order information
SELECT 
    o.order_id,
    o.order_date,
    c.name AS customer_name,
    p.product_name,
    o.quantity,
    (o.quantity * p.price) AS total_price
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;

-- LEFT JOIN: List all customers with orders (if any)
SELECT 
    c.customer_id,
    c.name AS customer_name,
    o.order_id,
    o.order_date,
    o.quantity
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_id;

-- LEFT JOIN: Show products even if not ordered
SELECT 
    p.product_id,
    p.product_name,
    o.order_id,
    o.quantity
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id
ORDER BY p.product_id;