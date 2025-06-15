-- SQL queries for retrieving insights

-- Get all customers
SELECT * FROM mini_mart.customers;

-- Get all products
SELECT  * FROM mini_mart.products;

-- Get products under Drinks category
SELECT * from mini_mart.products
WHERE category = 'Drinks';

-- Get recent orders by data
SELECT * from mini_mart.orders
ORDER BY order_date DESC;

-- Find the total orders
SELECT COUNT(order_id) AS total_customer_orders FROM mini_mart.orders;

-- Calculate the total revenue by customers
SELECT
    prod.product_name,
    sum(o.quantity * prod.price) AS total_revenue
FROM mini_mart.orders as o
JOIN mini_mart.products AS prod ON o.product_id = prod.product_id
GROUP BY prod.product_name
ORDER BY total_revenue DESC;

-- Calculate the average product price
SELECT round(avg(price), 2) AS average_product_price FROM mini_mart_db.mini_mart.products;


-- get detailed order information (with customer and product details).
SELECT
    o.order_id,
    c.name as customer_name,
    prod.product_name,
    prod.price,
    o.quantity,
    (o.quantity * prod.price)  AS Amount_Spent,
    o.order_date
FROM mini_mart.orders AS o
JOIN mini_mart.customers AS c ON o.customer_id = c.customer_id
JOIN mini_mart.products as prod ON o.product_id = prod.product_id;

-- list all customers and include their orders (if any).
-- use the customers table and the orders table.
-- customers name, order_id, product ordered
SELECT
     c.customer_id,
     c.name as customer_name,
     o.order_id,
     prod.product_name as item_ordered
 FROM mini_mart.customers as c
 LEFT JOIN mini_mart.orders as o ON c.customer_id = o.customer_id
 LEFT JOIN mini_mart.products as prod ON prod.product_id = o.product_id;

-- Show all products, even if they haven’t been ordered

SELECT
    p.product_id,
    p.product_name,
    COUNT(o.order_id) AS times_ordered
FROM mini_mart.products AS p
LEFT JOIN mini_mart.orders AS o ON p.product_id = o.product_id
GROUP BY p.product_id, p.product_name
ORDER BY p.product_id;