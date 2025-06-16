-- SQL queries for retrieving insights
--   * Use `WHERE` to filter products by category (e.g., `"Drinks"`).
select product_id, product_name from products
where category = 'cereal';


--  * Use `ORDER BY` to list recent orders by date.
select * from orders order by order_date;


/*Aggregation**

  * Use `COUNT()` to find the number of total orders.
  * Use `SUM()` to calculate revenue per product (price × quantity).
  * Use `AVG()` to find the average product price.

*/

select count(quantity) as total_orders from orders;

--   * Use `SUM()` to calculate revenue per product (price × quantity).
select p.product_id, p.product_name, sum(p.price * od.quantity) revenue_per_product from products p
join orders od
on p.product_id = od.product_id
group by p.product_id, p.product_name;

--  * Use `AVG()` to find the average product price.
select round(avg(price),2) as average_product_price from products;


/*
  * Use `INNER JOIN` to get detailed order information (with customer and product details).
  * Use `LEFT JOIN` to list all customers and include their orders (if any).
  * Use `LEFT JOIN` to show products even if they haven’t been ordered.

 */

--  Use `INNER JOIN` to get detailed order information (with customer and product details).
select c.name, p.product_name, p.price, od.*
from customers c
inner join orders od on c.customer_id = od.customer_id
inner join products p on od.product_id = p.product_id;


-- Use `LEFT JOIN` to list all customers and include their orders (if any).
select c.customer_id, c.name, od.order_id, od.quantity, od.order_date
from customers c 
left join orders od on c.customer_id = od.customer_id;


-- Use `LEFT JOIN` to show products even if they haven’t been ordered.
select p.product_id, p.product_name, od.order_id,  od.quantity, od.order_date
from products p
left join orders od on p.product_id = od.product_id;