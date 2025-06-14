-- Use SELECT to retrieve all customers or all products.
SELECT * FROM customers;
SELECT * FROM products;

-- Use WHERE to filter products by category (e.g., 'Books').
SELECT * FROM products
WHERE category = 'Books';

-- Use ORDER BY to list recent orders by date.
SELECT * FROM orders
ORDER BY order_date DESC;

-- Use COUNT() to find the number of total orders.
SELECT COUNT(*) FROM orders;

-- Use SUM() to calculate revenue per product (price × quantity).
SELECT SUM(quantity * price) AS total_revenue
FROM orders
JOIN products ON orders.product_id = products.product_id;

-- Use AVG() to find the average product price.
SELECT AVG(price) AS average_price FROM products;

--Use INNER JOIN to get detailed order information (with customer and product details).
SELECT customers.name, products.product_name, orders.quantity
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id
INNER JOIN products ON orders.product_id = products.product_id
ORDER BY customers.name;

-- Use LEFT JOIN to list all customers and include their orders (if any).
SELECT * FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id;

--Use LEFT JOIN to show products even if they haven’t been ordered.
SELECT * FROM products p
LEFT JOIN orders o ON o.product_id = p.product_id;
