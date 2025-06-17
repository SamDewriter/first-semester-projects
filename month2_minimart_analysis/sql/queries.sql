-- SQL queries for retrieving insights
-- Basic Queries
-- Use SELECT to retrieve all customers or all products.
SELECT * FROM customers;
SELECT * FROM products;

-- Use WHERE to filter products by category (e.g., "Drinks").
SELECT * FROM products WHERE category = 'Electronics';

-- Use ORDER BY to list recent orders by date.
SELECT * FROM orders ORDER BY order_date DESC;


-- Aggregation Queries
-- Use COUNT() to find the number of total orders.
SELECT COUNT(*) AS total_orders FROM orders;

-- Use SUM() to calculate revenue per product (price × quantity).
SELECT p.product_name, SUM(p.price * o.quantity) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;


-- Use AVG() to find the average product price.
SELECT ROUND(AVG(price), 2) AS average_price FROM products;



-- JOINS
-- Use INNER JOIN to get detailed order information.
SELECT
    o.order_id,
    o.order_date,
    o.quantity,
    c.customer_id,
    c.name        AS customer_name,
    c.email,
    p.product_id,
    p.product_name,
    p.price
FROM orders    AS o
INNER JOIN customers AS c ON o.customer_id = c.customer_id
INNER JOIN products  AS p ON o.product_id  = p.product_id
ORDER BY o.order_date DESC;


-- Use LEFT JOIN to list all customers and include their orders (if any).
SELECT
    c.customer_id,
    c.name,
    c.email,
    o.order_id,
    o.order_date,
    o.quantity,
    p.product_name
FROM customers AS c
LEFT JOIN orders   AS o ON o.customer_id = c.customer_id
LEFT JOIN products AS p ON p.product_id  = o.product_id
ORDER BY c.customer_id, o.order_date;


-- Use LEFT JOIN to show products even if they haven’t been ordered.
SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    COALESCE(SUM(o.quantity), 0)                     AS total_units_sold,
    COALESCE(SUM(o.quantity * p.price), 0)::numeric  AS total_revenue
FROM products AS p
LEFT JOIN orders AS o ON o.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category, p.price
ORDER BY total_units_sold DESC;
